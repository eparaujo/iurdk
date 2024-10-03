from django.urls import path
from . import views


urlpatterns = [  
    path('turnos/', views.TurnoCreateListAPIView.as_view(), name='Turno-create-list'),
    path('turnos/<int:pk>/', views.TurnoRetrieveUpdateDestroyAPIView.as_view(), name='turno-detail-view'),
]