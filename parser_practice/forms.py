from django import forms
from . import parser, models

class Parser_form(forms.Form):
	MEDIA_CHOICES = (('NEWS', 'NEWS'),)
	media_type = forms.ChoiceField(choices = MEDIA_CHOICES)
	
	class Meta:
		field = ['media_type', ]
	
	def parser_data(self):
		if self.data['media_type'] == 'NEWS':
			kaktus_parser = parser.parser()
			for i in kaktus_parser:
				models.Kaktus_media_parser.objects.create(**i)