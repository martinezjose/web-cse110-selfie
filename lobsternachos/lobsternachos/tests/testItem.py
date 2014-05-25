from lobsternachos.models import *
from google.appengine.ext import ndb
import unittest
from google.appengine.ext import testbed


class ItemTestCase(unittest.TestCase):
    '''

    PROPS:
    ItemName = ndb.StringProperty(required=True)
    Price = ndb.FloatProperty(required=True)
    Likes = ndb.IntegerProperty(required=True)
    Active = ndb. BooleanProperty(required=True)
    Calories = ndb.IntegerProperty(required=True)

    Created = ndb.DateTimeProperty(auto_now_add=True,required=True)
    LastUpdated = ndb.DateTimeProperty(auto_now=True,required=True)

    Description = ndb.StringProperty(required=True)
    DailySpecial = ndb.BooleanProperty(required=True)

    ImagePath is a list of blob keys.
    Image path will be taken care of in appengine
    ImagePath = ndb.BlobKeyProperty(repeated=True)
    Thumbnail = ndb.BlobKeyProperty()

    CategoryID = ndb.KeyProperty(kind=Category,required=True)


    '''

    def setUp(self):
        # First, create an instance of the Testbed class.
        self.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        self.testbed.activate()
        # Next, declare which service stubs you want to use.
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()

        keyAppetizer = Category(CategoryName='Appetizer').put()
        keyDish = Category(CategoryName='Dish').put()

        Item(ItemName='Lobster',
          Price=10.99,
          Likes=999,
          Active=True,
          Calories=987,
          Description='Very yummi, wow',
          DailySpecial=False,
          CategoryID=keyDish).put()

        Item(ItemName='Nachos',
          Price=4.99,
          Likes=123,
          Active=False,
          Calories=12345,
          Description='So yummi, much cheese, mega wow',
          DailySpecial=True,
          CategoryID=keyAppetizer).put()


    def test_get_all(self):
        # From last to first
        itemList = Item.query().order(-Item.Created).fetch(2)
        last = itemList[0]
        first = itemList[1]
        self.assertEqual(first.ItemName, 'Lobster')
        self.assertEqual(first.Price, 10.99)
        self.assertEqual(first.Likes, 999)
        self.assertEqual(first.Active, True)
        self.assertEqual(first.Calories, 987)
        self.assertEqual(first.Description, 'Very yummi, wow')
        self.assertEqual(first.DailySpecial, False)
        keyDish = Category.query(Category.CategoryName=='Dish').fetch()[0].key
        self.assertEqual(first.CategoryID, keyDish)


        self.assertEqual(last.ItemName, 'Nachos')
        self.assertEqual(last.Price, 4.99)
        self.assertEqual(last.Likes, 123)
        self.assertEqual(last.Active, False)
        self.assertEqual(last.Calories, 12345)
        self.assertEqual(last.Description, 'So yummi, much cheese, mega wow')
        self.assertEqual(last.DailySpecial, True)
        keyAppetizer = Category.query(Category.CategoryName=='Appetizer').fetch()[0].key
        self.assertEqual(last.CategoryID, keyAppetizer)

    def test_get_by_id(self):
        # Get by cat name
        nachos = Item.query(Item.ItemName=='Nachos').fetch()[0]
        # Get id based on appetizer object
        nachos2 = Item.get_by_id( nachos.key.id())

        self.assertEqual(nachos.key.id, nachos2.key.id)
        self.assertEqual(nachos2.ItemName, 'Nachos')
        self.assertEqual(nachos2.Price, 4.99)
        self.assertEqual(nachos2.Likes, 123)
        self.assertEqual(nachos2.Active, False)
        self.assertEqual(nachos2.Calories, 12345)
        self.assertEqual(nachos2.Description, 'So yummi, much cheese, mega wow')
        self.assertEqual(nachos2.DailySpecial, True)
        keyAppetizer = Category.query(Category.CategoryName=='Appetizer').fetch()[0].key
        self.assertEqual(nachos2.CategoryID, keyAppetizer)

    def test_update(self):
        # First
        itemList = Item.query().order(Item.Created).fetch(1)

        # Save key and last updated
        key = itemList[0].key
        lastU = itemList[0].LastUpdated

        itemList[0].ItemName = 'Super Duper Wow Lobstar'
        itemList[0].Price = 3636434636
        itemList[0].Likes = 1
        itemList[0].Active = False
        itemList[0].Calories = 534
        itemList[0].Description = 'New description'
        itemList[0].DailySpecial = True
        keyApp = Category.query(Category.CategoryName=='Appetizer').fetch()[0].key
        itemList[0].CategoryID = keyApp


        # Update
        itemList[0].put()

        # Get again
        itemList2 = Item.query().order(Item.Created).fetch(2)

        self.assertEqual(itemList2[0].ItemName, 'Super Duper Wow Lobstar')
        self.assertEqual(itemList2[0].Price, 3636434636)
        self.assertEqual(itemList2[0].Likes, 1)
        self.assertEqual(itemList2[0].Active, False)
        self.assertEqual(itemList2[0].Calories, 534)
        self.assertEqual(itemList2[0].Description, 'New description')
        self.assertEqual(itemList2[0].DailySpecial, True)
        self.assertEqual(itemList2[0].CategoryID, keyApp)

        # Key is same and updated object LastUpdated property is greater than
        # before
        self.assertEqual(itemList2[0].key, key)
        self.assertGreater(itemList2[0].LastUpdated, lastU)

    def test_delete(self):
        itemList = Item.query().order(Item.Created).fetch(2)
        self.assertTrue(len(itemList) is 2)
        for item in itemList:
          item.key.delete()
        itemList = Item.query().order(Item.Created).fetch(2)
        self.assertTrue(len(itemList) is 0)

    def tearDown(self):
        self.testbed.deactivate()
