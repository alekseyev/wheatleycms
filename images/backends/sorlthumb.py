from sorl.thumbnail import get_thumbnail

class SorlThumbnailBackend(object):
    """Use Google Apps's Images service for generating thumbnails"""
    def url(self, fileobj):
        return fileobj.url

    def thumbnail_url(self, fileobj, size=200):
        return get_thumbnail(fileobj, str(size)).url
