from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # show all moments as root
    path('moments/', views.index, name='all_moments'),
    path('mymoments/', views.MyMoments.as_view(), name='my_moments'),
    path('moment/<int:pk>', views.moment, name='moment'),

    path('new_moment/', views.new_moment, name='new_moment'),
    path('moment/<int:pk>/update/', views.update_moment, name='update_moment'),
    path('moment/<int:pk>/destroy/', views.destroy_moment, name='destroy_moment'),
    path('signup/', views.register, name='signup'),
]
