from google.appengine.ext import ndb

class Category(ndb.Model):
    name = ndb.StringProperty()
    lastUpdated = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def get_key_from_name(cls, guestbook_name=None):
        return ndb.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')
