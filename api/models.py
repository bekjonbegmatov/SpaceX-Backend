from django.db import models

# Create your models here.

class Menu_Items_Model(models.Model):

    name = models.CharField(max_length=50)
    link = models.URLField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Menu_Items_Model")
        verbose_name_plural = ("Menu_Items_Models")

    def __str__(self):
        return self.name

class Advantages_Model(models.Model):
 
    text1 = models.CharField(max_length=50)
    number = models.IntegerField()
    is_percent = models.BooleanField()
    text2 = models.CharField(max_length=50)
 
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
         verbose_name = ("Advantages_Model")
         verbose_name_plural = ("Advantages_Models")
 
    def __str__(self):
         return f"{self.text1} {self.number} {self.text2}"
 
class Main_Page_Model(models.Model):

    title = models.CharField(max_length=250)

    btn_text = models.CharField(max_length=50 , blank=True)
    btn_url = models.URLField(max_length=200)

    logo = models.ImageField(upload_to ='mainpage/logo' , height_field=None, width_field=None, max_length=None)
    background = models.ImageField(upload_to ='mainpage/background' , height_field=None, width_field=None, max_length=None)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Main_Page_model")
        verbose_name_plural = ("Main_Page_Models")
    
    def __str__(self):
        return self.title