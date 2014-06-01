import os
import urllib
import webapp2
import json

from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers


class MainHandler(webapp2.RequestHandler):
  def get(self):
    uploadUrl = blobstore.create_upload_url('/blobstore/upload')
    self.response.headers['Content-Type'] = 'application/json'
    self.response.out.write(json.dumps({
        'uploadUrl': uploadUrl,
    }))

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
  def post(self):
    upload_files = self.get_uploads('file')  # 'file' is file upload field in the form
    blob_info = upload_files[0]
    self.response.out.write(blob_info.key())

class ServeHandler(blobstore_handlers.BlobstoreDownloadHandler):
  def get(self, resource):
    resource = str(urllib.unquote(resource))
    blob_info = blobstore.BlobInfo.get(resource)
    self.send_blob(blob_info)

class DeleteHandler(webapp2.RequestHandler):
  def post(self,resource):
    blob_key = str(urllib.unquote(resource))
    blobstore.delete(blob_key)
    self.response.out.write(json.dumps({
        'result': "ok",
    }))

application = webapp2.WSGIApplication([('/blobstore/', MainHandler),
                               ('/blobstore/upload', UploadHandler),
                               ('/blobstore/serve/([^/]+)?', ServeHandler),
                               ('/blobstore/delete/([^/]+)?', DeleteHandler)],

                              debug=True)
