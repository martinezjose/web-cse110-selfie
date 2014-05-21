from google.appengine.ext import ndb
from random import randint

DEFAULT_CATALOG_NAME = 'default_catalog'

def GlobalAncestor():
    """Constructs a Datastore key for a LobsterNachos entity with default_catalog."""
    return ndb.Key('Catalog', DEFAULT_CATALOG_NAME)

class Category(ndb.Model):
    CategoryName = ndb.StringProperty(required=True)
    Created = ndb.DateTimeProperty(auto_now_add=True,required=True)
    LastUpdated = ndb.DateTimeProperty(auto_now=True,required=True)

class Item(ndb.Model):

    """Properties in creation template:
    ItemName. Description. Calories. Price. DailySpecial. Active.
    """
    ItemName = ndb.StringProperty(required=True)
    Price = ndb.FloatProperty(required=True)
    Likes = ndb.IntegerProperty(required=True)
    Active = ndb. BooleanProperty(required=True)
    Calories = ndb.IntegerProperty(required=True)

    """ checking newest """
    Created = ndb.DateTimeProperty(auto_now_add=True,required=True)
    LastUpdated = ndb.DateTimeProperty(auto_now=True,required=True)

    Description = ndb.StringProperty(required=True)
    DailySpecial = ndb.BooleanProperty(required=True)

    """
    Images is a list of blob keys. the first image will be the thumbnail
    Image path will be taken care of in appengine
    """
    ImagePath = ndb.BlobKeyProperty(repeated=True)
    Thumbnail = ndb.BlobKeyProperty()

    CategoryID = ndb.KeyProperty(kind=Category,required=True)

class Table(ndb.Model):
  TableName = ndb.StringProperty(required=True)
  PairingCode = ndb.ComputedProperty(lambda self: self.get_unique_pairing_code)
  Created = ndb.DateTimeProperty(auto_now_add=True,required=True)
  LastUpdated = ndb.DateTimeProperty(auto_now=True,required=True)

  @classmethod
  def get__unique_pairing_code(cls):
      ''' Generate initial pairing code '''
      pairingCode = randint(1000,9999)
      ''' While it already exists within a table, generate another one '''
      while Table.query(PairingCode=pairingCode) is not NONE:
        pairingCode = randint(1000,9999)
      return pairingCode

class Ping(ndb.Model):
  TableID =  ndb.KeyProperty(kind=Table,required=True)
  StatusID = ndb.IntegerProperty(required=True)
  Created = ndb.DateTimeProperty(auto_now_add=True,required=True)
  LastUpdated = ndb.DateTimeProperty(auto_now=True,required=True)

class Recommendation(ndb.Model):
    ItemID =  ndb.KeyProperty(kind=Item,required=True)
    RecommendedItemID =  ndb.KeyProperty(kind=Item,required=True)
    Created = ndb.DateTimeProperty(auto_now_add=True,required=True)
    LastUpdated = ndb.DateTimeProperty(auto_now=True,required=True)

class Order(ndb.Model):
  TableID =  ndb.KeyProperty(kind=Table,required=True)
  StatusID = ndb.IntegerProperty(required=True)
  Created = ndb.DateTimeProperty(auto_now_add=True,required=True)
  LastUpdated = ndb.DateTimeProperty(auto_now=True,required=True)
  DateClosed = ndb.DateTimeProperty()

class OrderDetail(ndb.Model):
  OrderID =  ndb.KeyProperty(kind=Order,required=True)
  ItemID =  ndb.KeyProperty(kind=Item,required=True)
  Created = ndb.DateTimeProperty(auto_now_add=True,required=True)
  LastUpdated = ndb.DateTimeProperty(auto_now=True,required=True)
  Quantity = ndb.IntegerProperty(required=True)
