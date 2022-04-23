from django.urls import path

from .import views

urlpatterns = [
    path('',views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'), #pagal id rasti po viena saraso nr
    path('search', views.search, name='search'),
]