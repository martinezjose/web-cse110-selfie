from google.appengine.ext import ndb

class Item(ndb.Model):
    name = ndb.StringProperty()
    price = ndb.FloatProperty()
    likes = ndb.IntegerProperty()
    active = ndb. BooleanProperty()
    calories = ndb.IntegerProperty()
    description = ndb.StringProperty()
    dailySpecial = ndb.BooleanProperty()

    """
    Images is a list of blob keys. the first image will be the thumbnail
    Image path will be taken care of in appengine
    """
    images = ndb.ListProperty(blobstore.BlobKey)

    category = ndb.ReferenceProperty(Category)

    """ checking newest """
    lastUpdated = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def get_key_from_name(cls, guestbook_name=None):
        return ndb.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')
