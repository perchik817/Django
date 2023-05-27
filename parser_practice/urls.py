from django.urls import path
from . import views

app_name = 'parser'

urlpatterns = [
	path('parser_news/', views.Parser_view.as_view(), name='parse_view'),
	path('parser/', views.Parser_form_view.as_view(), name='parse_func')
	]