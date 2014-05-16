from google.appengine.ext import ndb


class Tablet(ndb.Model):
    macAdress = ndb.StringProperty()

    @classmethod
    def get_key_from_name(cls, guestbook_name=None):
        return ndb.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')
