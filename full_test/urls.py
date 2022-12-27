from django.urls import path, re_path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings



app_name='full_test'

search_patterns=[
    path('', views.searchByGet, name='searchByGet'),
    #re_path(r'^\?=(?P<search_query>.*)$', views.searchByUrl, name='searchByUrl'),
]

VideoPage_patterns=[
    path('', views.VideoPage, name='VideoPage'),
    path('ajax/comment/', views.ajax_comment, name='ajax_comment'),
    path('ajax/getComment/', views.ajax_getComment, name='ajax_getComment'),
]

urlpatterns=[
    path('', views.index, name='index'),
    path('videoUpload/', views.videoUpload, name='VideoUpload'),
    #path('VideoPage/<int:id>/', views.VideoPage, name='VideoPage'),
    #path('VideoPage/<int:id>/ajax/comment/', views.ajax_comment, name='ajax_comment'),
    path('VideoPage/<int:id>/', include(VideoPage_patterns)),
    
    path('search/', include(search_patterns)),
    path('ajax/', views.ajax_result, name='ajax_result' ),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)