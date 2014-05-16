from google.appengine.ext import ndb


class OrderDetail(nndb.Model):

  order = nndb.ReferenceProperty(Order)

  dateAdded = nndb.DateTimeProperty(auto_now_add=True)
  dateRemoved = nndb.DateTimeProperty(auto_now_add=True)

  itemId = ReferenceProperty(Item)

  @classmethod
  def get_key_from_name(cls, guestbook_name=None):
      return nndb.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')
