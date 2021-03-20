from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('about', views.about,name='about'),
    path('prediction', views.prediction,name='prediction'),
    path('schemes', views.schemes,name='schemes'),
    #path('latestnews', views.latestnews,name='latestnews'),
    path('latestnews', views.latestnews,name='latestnews'),

    path('livefeedpage', views.livefeedpage,name='livefeedpage'),
    path('community', views.community,name='community'),
    path('contact', views.contact,name='contact'),
    path('calculate/', views.index1, name="calculate"),
]

