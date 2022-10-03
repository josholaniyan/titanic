from django.urls import path
from titanicapp import views


urlpatterns = [
   path('',views.home,name='home'), 
   path('result/',views.result,name='result'),
   path('error/',views.error,name='error'),
   
]