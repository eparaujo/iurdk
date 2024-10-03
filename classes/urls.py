from django.urls import path
from . import views


urlpatterns = [  
    path('aulas/', views.AulaCreateListAPIView.as_view(), name='aula-create-list'),
    path('aulas/<int:pk>/', views.AulaRetrieveUpdateDestroyAPIView.as_view(), name='aula-detail-view'),
]