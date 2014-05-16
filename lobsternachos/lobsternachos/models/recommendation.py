from google.appengine.ext import ndb


class Recommendation(ndb.Model):
  item = ndb.ReferenceProperty(Item)
  recoItem = ndb.ReferenceProperty(Item)

  lastUpdated = ndb.DateTimeProperty(auto_now_add=True)

  @classmethod
  def get_key_from_name(cls, guestbook_name=None):
  return ndb.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')
