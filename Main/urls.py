from django.urls import path 
from Main import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 

    path('', views.index, name="index"),

    path('download_my_cv', views.download_my_cv, name='download_my_cv'),
    path('my_cv', views.my_cv, name="my_cv"),
    path('language_learn', views.language_learn, name="language_learn"),
    path('my_profile', views.my_profile, name="my_profile"),
    
    path('ios_details/<int:id>/', views.ios_detail, name="ios_details"),
    path('android_details/<int:id>/', views.android_detail, name="android_details"),
    path('python_details/<int:id>/', views.python_detail, name="python_details"),

    path('ios_projects', views.all_ios_projects, name="ios_projects"),
    path('android_projects', views.all_android_projects, name="android_projects"),
    path('python_projects', views.all_python_projects, name="python_projects"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)