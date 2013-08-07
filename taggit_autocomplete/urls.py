from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'taggit_autocomplete.views',
    url(r'^list$', 'list_tags', name='taggit_autocomplete-list'),
)
