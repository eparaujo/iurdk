from django.urls import path
from . import views

urlpatterns = [
    path('katas/', views.KataCreateListAPIView.as_view(), name='kata-create-list'),
    path('katas/<int:pk>/', views.KataRetrieveUpdateDestroyAPIView.as_view(), name='kata-detail-vies'),    
    path('katas/stats/', views.KataStatsView.as_view(), name='kata-stats-view'),
]