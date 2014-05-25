from lobsternachos.models import *
from google.appengine.ext import ndb
import unittest
from google.appengine.ext import testbed


class ItemTestCase(unittest.TestCase):

'''

TableName = ndb.StringProperty(required=True)
PairingCode = ndb.ComputedProperty(lambda self: self.get_unique_pairing_code)
Created = ndb.DateTimeProperty(auto_now_add=True,required=True)
LastUpdated = ndb.DateTimeProperty(auto_now=True,required=True)

@classmethod
def get__unique_pairing_code(cls):
    Generate initial pairing code
    pairingCode = randint(1000,9999)
    While it already exists within a table, generate another one
    while Table.query(PairingCode=pairingCode) is not NONE:
      pairingCode = randint(1000,9999)
    return pairingCode

'''
    def setUp(self):
      # First, create an instance of the Testbed class.
      self.testbed = testbed.Testbed()
      # Then activate the testbed, which prepares the service stubs for use.
      self.testbed.activate()
      # Next, declare which service stubs you want to use.
      self.testbed.init_datastore_v3_stub()
      self.testbed.init_memcache_stub()
      Table(TableName="A").put()
      Table(TableName="B").put()

  def test_get_all(self):
      # From last to first
      tableList = Table.query().order(-Table.Created).fetch(2)

      last = tableList[0]
      first = tableList[1]

      self.assertEqual(first.TableName, 'A')

      self.assertEqual(last.TableName, 'B')
