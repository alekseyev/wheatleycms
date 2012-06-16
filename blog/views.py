from datetime import datetime
from django.conf import settings
from django.contrib.syndication.views import Feed
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.feedgenerator import Atom1Feed
from django.views.generic import ListView, UpdateView, DeleteView
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import permission_required

from .models import Blog, Post
from .forms import PostForm

def review(request, review_key):
    post = get_object_or_404(Post, review_key=review_key)
    return show_post(request, post, review=True)

def show_post(request, post, review=False):
    recent_posts = Post.objects.filter(blog=post.blog, published=True)
    recent_posts = recent_posts.order_by('-published_on')[:6]
    return render(request, 'blog/post_detail.html',
        {'post': post, 'blog': post.blog, 'recent_posts': recent_posts,
         'review': review})

class BrowseView(ListView):
    paginate_by = 8

    def dispatch(self, request, blog):
        if request.GET.get('page') == '1':
            return HttpResponseRedirect(request.path)
        return super(BrowseView, self).dispatch(request, blog=blog)

    def get_queryset(self):
        query = Post.objects.filter(blog=self.kwargs['blog'], published=True)
        # TODO: add select_related('author')
        return query.order_by('-published_on')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BrowseView, self).get_context_data(**kwargs)
        context.update({'blog': self.kwargs['blog'],
                        'recent_posts': self.get_queryset()[:6],
                        'browse_posts': True})
        return context

browse = BrowseView.as_view()

def feedburner(feed):
    """Converts a feed into a FeedBurner-aware feed."""
    def _feed(request, blog):
        if not blog.feed_redirect_url or \
                request.META['HTTP_USER_AGENT'].startswith('FeedBurner') or \
                request.GET.get('override-redirect') == '1':
            return feed(request, blog=blog)
        return HttpResponseRedirect(blog.feed_redirect_url)
    return _feed

class LatestEntriesFeed(Feed):
    feed_type = Atom1Feed

    def get_object(self, request, blog):
        return blog

    def title(self, blog):
        return blog.title

    def link(self, blog):
        return blog.get_absolute_url()

    def subtitle(self, blog):
        return blog.description

    def item_title(self, post):
        return post.title

    def item_description(self, post):
        url = 'http%s://%s%s' % ('s' if self._request.is_secure() else '',
                                 self._request.get_host(),
                                 post.get_absolute_url())
        footer = '<p><a href="%s#disqus_thread">Leave a comment</a></p>' % url
        return post.rendered_content + footer

    def item_author_name(self, post):
        return post.author.get_full_name()

    def item_pubdate(self, post):
        return post.published_on

    def items(self, blog):
        query = Post.objects.filter(blog=blog, published=True).order_by(
            '-published_on')
        # TODO: add select_related('author') once it's supported
        return query[:100]

@feedburner
def latest_entries_feed(request, *args, **kwargs):
    feed = LatestEntriesFeed()
    feed._request = request
    return feed(request, *args, **kwargs)

@permission_required('blog.add_post')
def add_post(request, blog_url):
    blog = get_object_or_404(Blog, url=blog_url)
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.instance.blog = blog
        form.instance.author = request.user
        form.save()
        return redirect(blog.url)
    else:
        return render(
            request,
            'form.html',
            {
                'form': form,
                'title': _('Add post to %(title)s') % {'title': blog.title},
            })

@permission_required('blog.change_post')
def update_post(request, pk):
    class UpdatePost(UpdateView):
        model = Post
        form_class = PostForm
        template_name = 'form.html'

        def get_context_data(self, **kwargs):
            context = super(UpdatePost, self).get_context_data(**kwargs)
            context['title'] = _('Editing post %(title)s') % {'title': self.object.title}
            context['submit_caption'] = _('Save')
            return context

    return UpdatePost.as_view()(request, pk=pk)

@permission_required('blog.delete_post')
def delete_post(request, pk):
    class DeletePost(DeleteView):
        model = Post
        template_name = 'confirm.html'

        def get_context_data(self, **kwargs):
            context = super(DeletePost, self).get_context_data(**kwargs)
            context['title'] = _('Deleting post %(title)s') % {'title': self.object.title}
            context['message'] = _('Are you sure you want to delete post %(title)s?') % \
                {'title': self.object.title}
            return context

        def get_success_url(self, obj):
            return obj.blog.get_absolute_url()

    return DeletePost.as_view()(request, pk=pk)
