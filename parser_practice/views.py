from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView, FormView
from . import parser, models,forms

class Parser_view(ListView):
	model = models.Kaktus_media_parser
	template_name = 'kaktus_parser.html'
	
	def get_queryset(self):
		return models.Kaktus_media_parser.objects.all()

class Parser_form_view(FormView):
	template_name = 'parser_kaktus.html'
	form_class = forms.Parser_form
	
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.parser_data()
			return HttpResponse('<h1>Data is got</h1>')
		else:
			return super(Parser_form_view, self).post(request, *args, **kwargs)