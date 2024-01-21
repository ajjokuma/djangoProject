from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Eatery

def home(request):
    context = {
        'eateries': Eatery.objects.all()
    }
    return render(request, 'halalweb/home.html', context)

class EateryListView(ListView):
    model = Eatery
    template_name = 'halalweb/home.html'
    context_object_name = 'eateries'
    ordering = ['-date_posted']

    def get_queryset(self):
        return Eatery.objects.filter(approved=True).order_by('-date_posted')

class EateryDetailView(DetailView):
    model = Eatery

class EateryCreateView(LoginRequiredMixin, CreateView):
    model = Eatery
    fields = ['title', 'description', 'address']

    def form_valid(self, form):
        form.instance.author = self.request.user
        if self.request.user.is_superuser:
            form.instance.approved = True
        else:
            form.instance.approved = False
        return super().form_valid(form)

class EateryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Eatery
    fields = ['title', 'description', 'address']

    def form_valid(self, form):
        form.instance.author = self.request.user
        if self.request.user.is_superuser:
            form.instance.approved = True
        else:
            form.instance.approved = False
        return super().form_valid(form)
    
    def test_func(self):
        eatery = self.get_object()
        if self.request.user == eatery.author and eatery.approved == False and self.request.user.is_superuser == False:
            return True
        elif self.request.user.is_superuser == True:
            return True
        return False
    
class EateryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Eatery
    success_url = '/'

    def test_func(self):
        if self.request.user.is_superuser == True:
            return True
        return False
    
class UserEateryListView(ListView):
    model = Eatery
    template_name = 'halalweb/user_eatery.html'
    context_object_name = 'eateries'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Eatery.objects.filter(author=user).order_by('-date_posted')
    
class AdminEateryListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Eatery
    template_name = 'halalweb/admin_eatery.html'
    context_object_name = 'eateries'

    def get_queryset(self):
        return Eatery.objects.filter(approved=False).order_by('-date_posted')
    
    def test_func(self):
        if self.request.user.is_superuser == True:
            return True
        return False
    
class EateryApproveView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Eatery
    fields = ['approved']
    template_name = 'halalweb/confirm_approve.html'
    success_url = '/'
    
    def test_func(self):
        if self.request.user.is_superuser == True:
            return True
        return False

def about(request):
    return render(request, 'halalweb/about.html', {'title': 'About'})