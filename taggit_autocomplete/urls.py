try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('taggit_autocomplete.views',
    url(r'^list$', 'list_tags', name='taggit_autocomplete-list'),
)
