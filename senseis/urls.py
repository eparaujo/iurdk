from django.urls import path
from . import views


urlpatterns = [  
    path('senseis/', views.SenseiCreateListAPIView.as_view(), name='sensei-create-list'),
    path('senseis/<int:pk>/', views.SenseiRetrieveUpdateDestroyAPIView.as_view(), name='sensei-detail-view'),
]