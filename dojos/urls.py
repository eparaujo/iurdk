from django.urls import path
from . import views

urlpatterns = [
    path('dojos/', views.DojoCreateListAPIView.as_view(), name='dojo-create-list'),
    path('dojos/<int:pk>/', views.DojoRetrieveUpdateDesctroyAPIView.as_view(), name='dojo-detail-vies'),
    path('dojos/stats/', views.DojoStatsView.as_view(), name='dojo-stats-view'),
]