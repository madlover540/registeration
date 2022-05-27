from django.urls import path, include
from basicapp import views


app_name = 'basicapp'
urlpatterns=[
    path('', views.index, name='index'),
    path('other/',views.other, name='other'),
    path('relative/', views.relative_url, name ='relative'),
    path('register/', views.register, name ='register'),
    path('user_login/', views.user_login, name ='user_login'),

]
