from google.appengine.api.images import get_serving_url

class GoogleBackend(object):
    """Use Google Apps's Images service for generating thumbnails"""
    def url(self, fileobj):
        return get_serving_url(fileobj.file.blobstore_info)   

    def thumbnail_url(self, fileobj, size=200):
        return get_serving_url(fileobj.file.blobstore_info, size)