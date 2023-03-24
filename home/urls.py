from django.urls import path

from . import views

urlpatterns = [
    path('', views.FeedsListView.as_view(), name='index'),
]
