from lobsternachos.models import *
import json
from google.appengine.ext import ndb
from lobsternachos.helpers import Encoder
from django.http import HttpResponse
from google.appengine.api import images


# Get all items from database, and return the list as a json string
def get_all(request):
	if request.method == 'GET':


		data = json.dumps([{
		'Thumbnail': images.get_serving_url(p.ImagePath[0],200),
		'ItemID':p.key.integer_id(),
		'RemoteID':p.key.integer_id(),
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
		'ImagePath':[images.get_serving_url(p.ImagePath[0],480),images.get_serving_url(p.ImagePath[1],480)]
		}
	  for p in Item.query(Item.Active == True,ancestor=GetAncestor()).fetch()], cls = Encoder)

		return HttpResponse(data, content_type="application/json")
