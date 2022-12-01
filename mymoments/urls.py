from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('moments/', views.AllMoments.as_view(), name='all_moments'),
    path('mymoments/', views.MyMoments.as_view(), name='my_moments'),
    path('moment/<int:pk>', views.Moment.as_view(), name='moment'),

    path('signup/', views.signup, name='signup'),
]
