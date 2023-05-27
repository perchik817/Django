from django.urls import path
from . import views

app_name = 'parse'

urlpatterns = [
	path('parser_film_info/', views.Parser_view.as_view(), name='parse_view'),
	path('parser_film/', views.Parser_form_view.as_view(), name='parse_func')
	]