from django.urls import path
from . import views

urlpatterns = [
    path('senseis/', views.SenseiListCreateAPIView.as_view(), name='sensei-create-list'),
    path('senseis/<int:pk>/', views.SenseiRetrireveUpdateDestroyAPIView.as_view(), name='sensei-detail-vies'),    
]