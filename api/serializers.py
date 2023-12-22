from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import *

class Menu_Items_Serializer(ModelSerializer):
    class Meta:
        model = Menu_Items_Model
        fields = '__all__'
    
class Advantages_Serializer(ModelSerializer):
    class Meta:
        model = Advantages_Model
        fields = '__all__'
    
class Main_Page_Serializer(ModelSerializer):
    class Meta:
        model = Main_Page_Model
        fields = '__all__'
    