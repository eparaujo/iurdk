from django.urls import path
from . import views


urlpatterns = [
    path('karatestyles/', views.KarateStyleCreateListAPIView.as_view(), name='karatestyle-create-list'),
    path('karatestyles/<int:pk>/',views.KarateStyleRetrieveUpdateDestroyAPIView.as_view(), name='karatestyle-details-view'),
]