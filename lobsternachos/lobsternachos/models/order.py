from google.appengine.ext import ndb


class Order(ndb.Model):

  table = ndb.ReferenceProperty(Table)

  ratings = ndb.IntegerProperty()
  statusId = ndb.IntegerProperty()
  dateAdded = ndb.DateTimeProperty(auto_now_add=True)
  dateRemoved = ndb.DateTimeProperty(auto_now_add=True)

  @classmethod
  def get_key_from_name(cls, guestbook_name=None):
      return ndb.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')
