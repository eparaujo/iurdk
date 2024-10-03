from django.urls import path
from . import views


urlpatterns = [  
    path('weekdays/', views.WeekDayCreateListAPIView.as_view(), name='weekday-create-list'),
    path('weekdays/<int:pk>/', views.WeekDayRetrieveUpdateDestroyAPIView.as_view(), name='weekday-detail-view'),
]