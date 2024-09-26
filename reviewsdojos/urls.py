from django.urls import path
from . import views

urlpatterns = [
    path('reviewsdojos/', views.ReviewDojoListCreateAPIView.as_view(), name='reviewdojo-list-view'),
    path('reviewdojos/<int:pk>/', views.ReviewDojoRetrieveUpdareDestroyAPIView.as_view(), name='reviewdojo-detail-view'),
]