from django.urls import path
from . import views

urlpatterns = [
    path('times/', views.TimeCreateListAPIView.as_view(), name='time-create-list'),
    path('times/<int:pk>/', views.TimeRetrieveUpdateDestroyAPIView.as_view(), name='time-details-view'),
]