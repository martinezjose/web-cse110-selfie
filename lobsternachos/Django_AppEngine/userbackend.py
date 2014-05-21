from django.contrib.auth.models import User

class CustomUser (User):

    def save (self):
        """saving to DB disabled"""
        pass

    objects = None # we cannot really use this w/o local DB

    username = ""  # and all the other properties likewise.
                   # They're defined as model.CharField or similar,
                   # and we can't allow that

    def get_group_permissions (self):
        """If you don't make your own permissions module,
           the default also will use the DB. Throw it away"""
        return [] # likewise with the other permission defs

    def get_and_delete_messages (self):
        """Messages are stored in the DB. Darn!"""
        return []

from django.contrib.auth.backends import RemoteUserBackend

class CustomRemoteUserBackend (RemoteUserBackend):
    # Create a User object if not already in the database?
    create_unknown_user = False

    def createUser (self, myUser, user_id):
        user = CustomUser();
        user.username = user_id
        return user

    def get_user (self, user_id):
        user = self.createUser (CustomUser, user_id)
        return user

    def authenticate (self, **credentials):
        #check_credentials ()
        user = self.createUser (CustomUser, credentials)
        return user
