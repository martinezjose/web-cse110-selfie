from lobsternachos.models import *
import json
from google.appengine.ext import ndb
from lobsternachos.helpers import Encoder
from django.http import HttpResponse

# Get all items from database, and return the list as a json string
def get_all(request):


	data = json.dumps([{
	'ItemID':p.key.integer_id(),
	'ItemName':p.ItemName,
	'Price':p.Price,
	'CategoryID':p.CategoryID.integer_id(),
	'Likes':p.Likes,
	'Active':p.Active,
	'Calories':p.Calories,
	'Created':p.Created,
	'LastUpdated':p.LastUpdated,
	'DailySpecial':p.DailySpecial,
	'Description':p.Description,
	'ImagePath':["lobster-nachos.appspot.com/blobstore/serve/"+str(p.ImagePath[0]),"lobster-nachos.appspot.com/blobstore/serve/"+str(p.ImagePath[1])]
	}
  for p in Item.query(ancestor=GetAncestor()).fetch()], cls = Encoder)

	return HttpResponse(data, content_type="application/json")
