from django.urls import path
from . import views

app_name = 'place_to_go'
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('place_list/', views.place_list, name='place_list'), #place_to_go:place_list
    path('add_place/', views.add_place_form, name='add_place'), #place_to_go:add_place
]