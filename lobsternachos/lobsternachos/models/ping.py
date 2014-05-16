from google.appengine.ext import ndb


class Ping(ndb.Model):

    """ Ping has parent table """

    time = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def get_key_from_name(cls, guestbook_name=None):
        return ndb.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')
