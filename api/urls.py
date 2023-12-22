from django.urls import path
from .views import * 

urlpatterns = [
    path('', getRoutes , name="getRoutes"),

    path('api/menuitems', main_menu_items , name="MenuItem"),
    path('api/advantages', advantages , name="advantages"),
    path('api/main_page', main_page , name="main_page"),
]