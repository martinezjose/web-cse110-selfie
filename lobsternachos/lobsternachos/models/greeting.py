from google.appengine.ext import ndb

class Greeting(ndb.Model):
    """Models an individual Guestbook entry with author, content, and date."""
    author = ndb.UserProperty()
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

    def guestbook_key(guestbook_name='default_guestbook'):
        """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
        return ndb.Key('Guestbook', guestbook_name)
