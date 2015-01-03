import json
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

from taggit.models import Tag


def list_tags(request):
    try:
        #tempTags = Tag.objects.filter(name__icontains=request.GET['term']).values_list('name', flat=True)
        tempTags = Tag.objects.filter(name__istartswith=request.GET['term'])
        tags = set()
        for tagValues in tempTags:
            singleTags = tagValues.name.split(',')
            if len(singleTags) == 1:
                tags.add(singleTags[0])
    except MultiValueDictKeyError:
        pass
    tags = list(tags)
    return HttpResponse(json.dumps(tags), mimetype='text/javascript')
