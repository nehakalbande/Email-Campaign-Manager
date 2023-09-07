from django.urls import path
from . import views

urlpatterns = [
    path('add-subscriber/', views.add_subscriber, name='add_subscriber'),
    path('unsubscribe/<str:email>/', views.unsubscribe, name='unsubscribe'),
    path('send-campaign/<int:campaign_id>/', views.send_campaign, name='send_campaign'),
]
