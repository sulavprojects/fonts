from django.urls import path
from .views import *

from re import template
from . import views
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('' , fonts , name="fonts"),
    path('<slug:slug>/' , fonts_details , name="fonts_details"),
    path('fonts' , fonts , name="arabic fonts"),
    path('allfonts' , allfonts , name="allfonts"),
    path('contact' , contact , name="contact"),
    path('termsandcondition' , termsandcondition , name="termsandcondition"),
    path('privacypolicy' , privacypolicy , name="privacypolicy"),
    path('pages' , pages , name="our_page"),
    path('aboutus' , aboutus , name="aboutus"),
    

]