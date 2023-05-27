from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView, ListView

class Registration(CreateView):
    form_class = UserCreationForm
    success_url = '/users/'
    template_name = 'registration.html'

class NewLoginForm(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse("users:user_list")

class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'user_list.html'

    def get_queryset(self):
        return User.objects.all()
    
#получение информации (GET)
class TvShow_View(generic.ListView):
    template_name = 'tvshow.html'
    queryset = models.TvShow.objects.all()

    def get_queryset(self):
        return models.TvShow.objects.all()


#get id
class TvShow_detail_view(generic.DetailView):
    template_name = 'tvshow_detail.html'

    def get_object(self, **kwargs):
        tvshow_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=tvshow_id)

# create TvShow
class TvShowCreateView(generic.CreateView):
    template_name = 'add_tv_show.html'
    form_class = forms.TvShowForm
    queryset = models.TvShow.objects.all()
    success_url = '/tvshow/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(TvShowCreateView, self).form_valid(form = form)

#update TvShow

class TvShowUpdateView(generic.UpdateView):
    template_name = 'tvshow_update.html'
    form_class = forms.TvShowForm
    success_url = '/tvshow/'

    def get_object(self, **kwargs):
        tvshow_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=tvshow_id)

    def form_valid(self, form):
        return super(TvShowUpdateView, self).form_valid(form=form)



#delete TvShow
class TvShowDeleteView(generic.DeleteView):
    template_name = 'tvshow_delete.html'
    success_url = '/tvshow/'

    def get_object(self, **kwargs):
        tvshow_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=tvshow_id)