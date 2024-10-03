from django.urls import path
from . import views


urlpatterns = [  
    path('gengraduations/', views.GraduationCreateListAPIView.as_view(), name='graduation-create-list'),
    path('graduations/<int:pk>/', views.GraduationRetrieveUpdateDestroyAPIView.as_view(), name='graduation-detail-view'),
]