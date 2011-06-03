from django import forms
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.safestring import mark_safe

from utils import edit_string_for_tags


class TagAutocomplete(forms.TextInput):
	input_type = 'text'
	
	def render(self, name, value, attrs=None):
		list_view = reverse('taggit_autocomplete-list')
		if value is not None and not isinstance(value, basestring):
			value = edit_string_for_tags(
					[o.tag for o in value.select_related("tag")])
		html = super(TagAutocomplete, self).render(name, value, attrs)
		
		return mark_safe(html)

	class Media:
		js_base_url = getattr(settings, 'TAGGIT_AUTOCOMPLETE_JS_BASE_URL',
							  '%s/jquery-autocomplete' % settings.MEDIA_URL)
		js = (
			'%s/autocomplete.js' % js_base_url,
		)