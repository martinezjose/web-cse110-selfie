from lobsternachos.models import *
import json
from google.appengine.ext import ndb
from lobsternachos.helpers import Encoder
from django.http import HttpResponse


def get_all(request):
	if request.method == 'GET':
		validRecommendations =[]
		recs = Recommendation.query(ancestor=GetAncestor()).fetch()
		for rec in recs:
			# Try to get item
			item = Item.get_by_id(rec.ItemID.integer_id(),
			parent = GetAncestor())

			itemR = Item.get_by_id(rec.RecommendedItemID.integer_id(),
			parent = GetAncestor())
			# Check if exist
			if item and itemR:
				if item.Active and itemR.Active:
					validRecommendations.append(rec)

		data = json.dumps([{
		'ItemID':p.ItemID.integer_id(),
		'RecommendedItemID':p.RecommendedItemID.integer_id(),
	  'Created':p.Created,
	  'LastUpdated':p.LastUpdated}
	   for p in validRecommendations], cls = Encoder)

		return HttpResponse(data, content_type="application/json")
