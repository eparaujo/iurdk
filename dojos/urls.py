from django.urls import path
from . import views


urlpatterns = [  
    path('dojos/', views.DojoCreateListAPIView.as_view(), name='dojo-create-list'),
    path('dojos/<int:pk>/', views.GenreRetrieveUpdateDestroyAPIView.as_view(), name='dojo-detail-view'),
]