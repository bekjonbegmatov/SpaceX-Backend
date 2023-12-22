from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import models , serializers


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            "ABOUT"
        },
        {
            'Developer': 'Begmatov Behruz',
            'Phone number': '+79516311117',
            'Git Hub': 'https://github.com/bekjonbegmatov',
            'Telegram': 'https://t.me/behruz_begmatov',
            'Email': 'behruzbegmatov28@gmail.com',
        },
        {
            "ROUTES"
        },
        {
            'Endpoint': 'api/menuitems',
            'method': 'GET',
            'body': None,
            'description': 'Returns a list of menu items'
        },
        {
            'Endpoint': 'api/advantages',
            'method': 'GET',
            'body': None,
            'description': 'Returns a list of benefits is returned.'
        },
        {
            'Endpoint': 'api/main_page',
            'method': 'GET',
            'body': None,
            'description': 'Returns a page elements : logo , background , title'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def main_menu_items(request):
    mitems = models.Menu_Items_Model.objects.all()
    serializer = serializers.Menu_Items_Serializer(mitems , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def advantages(request):
    adv = models.Advantages_Model.objects.all()
    serializer = serializers.Advantages_Serializer(adv , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def main_page(request):
    data = models.Main_Page_Model.objects.all()
    serializer = serializers.Main_Page_Serializer(data , many=True)
    return Response(serializer.data[0])