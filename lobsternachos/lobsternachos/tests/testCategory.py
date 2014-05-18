from lobsternachos.models import *
from google.appengine.ext import ndb
import unittest
from google.appengine.ext import testbed

class CategoryTestCase(unittest.TestCase):

    '''
    PROPS:
    CategoryName = ndb.StringProperty(required=True)
    LastUpdated = ndb.DateTimeProperty(auto_now_add=True,required=True)
    Created = ndb.DateTimeProperty(auto_now=True,required=True)
    '''
    def setUp(self):
        # First, create an instance of the Testbed class.
        self.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        self.testbed.activate()
        # Next, declare which service stubs you want to use.
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        Category(CategoryName='Appetizers').put()
        Category(CategoryName='Hamburguers').put()

    def test_get_all(self):
        # From last to first
        catList = Category.query().order(-Category.Created).fetch(2)
        last = catList[0]
        first = catList[1]
        self.assertEqual(last.CategoryName, 'Hamburguers')
        self.assertEqual(first.CategoryName, 'Appetizers')


    def test_get_by_id(self):
        # Get by cat name
        appetizer = Category.query(Category.CategoryName=='Appetizers').fetch()[0]
        # Get id based on appetizer object
        appetizer2 = Category.get_by_id( appetizer.key.id())

        self.assertEqual(appetizer.key.id, appetizer2.key.id)
        self.assertEqual(appetizer2.CategoryName, 'Appetizers')

    def test_update(self):

        # From last to first
        catList = Category.query().order(-Category.Created).fetch(2)

        # Save key and last updated
        key = catList[0].key
        lastU = catList[0].LastUpdated

        catList[0].CategoryName = 'Drinks'
        catList[1].CategoryName = 'Drinks'

        # Update
        catList[0].put()
        catList[1].put()

        # Get again
        catList2 = Category.query().order(-Category.Created).fetch(2)

        self.assertEqual(catList2[0].CategoryName, 'Drinks')
        self.assertEqual(catList2[1].CategoryName, 'Drinks')

        # Key is same and updated object LastUpdated property is greater than
        # before
        self.assertEqual(catList2[0].key, key)
        self.assertGreater(catList2[0].LastUpdated, lastU)

    def test_delete(self):
        catList = Category.query().order(-Category.Created).fetch(2)
        self.assertTrue(len(catList) is 2)
        for category in catList:
          category.key.delete()
        catList = Category.query().order(-Category.Created).fetch(2)
        self.assertTrue(len(catList) is 0)

    def tearDown(self):
        self.testbed.deactivate()
