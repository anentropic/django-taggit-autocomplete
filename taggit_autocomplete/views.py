from django.http import HttpResponse
from django.core import serializers
from taggit.models import Tag
from django.utils import simplejson
from django.utils.datastructures import MultiValueDictKeyError

def list_tags(request):
	try:
		tags = Tag.objects.filter(name__istartswith=request.GET['q']).values_list('name', flat=True)
		data = [{'value': t, 'name': t} for t in tags]
	except MultiValueDictKeyError:
		data = []
	
	return HttpResponse(simplejson.dumps(data), mimetype='application/json')
