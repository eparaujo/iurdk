from django.urls import path
from . import views


urlpatterns = [  
    path('karatecas/', views.KaratecaCreateListAPIView.as_view(), name='karateca-create-lis'),
    path('karatecas/<int:pk>/', views.KaratecaRetrieveUpdateDestroyAPIView.as_view(), name='karateca-detail-view'),
]