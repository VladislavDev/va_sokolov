from django.shortcuts import render
from django.views import generic

from .models import Project


class ListView(generic.ListView):

    model = Project

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        return context