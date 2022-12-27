from django.urls import path, re_path, include
from . import views

app_name='users'


homepage_patterns=[
    path('', views.userHomepage.as_view(), name='Homepage'),
    #path('history/', views.history.as_view(), name='userHistory'),     not turned on yet
    path('settings/', views.userSettings, name='userSettings'),
    path('myvideo/', views.userVideos, name='userVideos'),
    #path('collections/', views.userCollections, name='userCollections),  not turned on yet
]


urlpatterns=[
    path('Homepage/<slug:username>/',include(homepage_patterns)), #profile/


    path('login/', views.userLogin, name='userLogin'),
    path('logout/', views.userLogout, name='userLogout'),
    path('register/', views.userRegister, name='userRegister'),
]


'''
urlpatterns+=[
    path('formTest/', views.formTest),
]
'''
