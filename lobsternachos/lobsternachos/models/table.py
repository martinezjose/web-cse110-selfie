from google.appengine.ext import ndb


class Table(ndb.Model):
    name = ndb.StringProperty()
    pairingCode = ndb.IntegerProperty()

    @classmethod
    def get_key_from_name(cls, guestbook_name=None):
        return ndb.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')
