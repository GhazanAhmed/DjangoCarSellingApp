from django.urls import path
from . import views

app_name = 'CarCity'

urlpatterns = [
    path('', views.ad_list, name='ad_list'),
    path('post-ad/', views.post_ad, name='post_ad'),
    path('ad/<int:ad_id>/', views.ad_detail, name='ad_detail'),
    path('filter_ads/', views.filter_ads, name='filter_ads'), 
    path('sort_ads/', views.sort_ads, name='sort_ads'),  
]