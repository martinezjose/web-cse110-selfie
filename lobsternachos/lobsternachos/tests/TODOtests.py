

class PingTestCase(TestCase):
'''

PROPS:
TableID =  ndb.KeyProperty(kind=Table,required=True)
StatusID = ndb.IntegerProperty(required=True)
Created = ndb.DateTimeProperty(auto_now_add=True,required=True)
LastUpdated = ndb.DateTimeProperty(auto_now=True,required=True)


'''
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')


class RecommendationTestCase(TestCase):
'''

PROPS:
ItemID =  ndb.KeyProperty(kind=Item,required=True)
RecommendedItemID =  ndb.KeyProperty(kind=Item,required=True)
Created = ndb.DateTimeProperty(auto_now_add=True,required=True)
LastUpdated = ndb.DateTimeProperty(auto_now=True,required=True)


'''
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')


class OrderTestCase(TestCase):
'''

PROPS:
TableID =  ndb.KeyProperty(kind=Table,required=True)
Rating = ndb.IntegerProperty(required=True)
StatusID = ndb.IntegerProperty(required=True)
Created = ndb.DateTimeProperty(auto_now_add=True,required=True)
LastUpdated = ndb.DateTimeProperty(auto_now=True,required=True)
DateClosed = ndb.DateTimeProperty()


'''
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')

class OrderDetailTestCase(TestCase):
'''

PROPS:
OrderID =  ndb.KeyProperty(kind=Order,required=True)
ItemID =  ndb.KeyProperty(kind=Item,required=True)

Created = ndb.DateTimeProperty(auto_now_add=True,required=True)
LastUpdated = ndb.DateTimeProperty(auto_now=True,required=True)
Quantity = ndb.IntegerProperty(required=True)


'''
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
