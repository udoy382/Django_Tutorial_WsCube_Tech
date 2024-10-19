"""
URL configuration for mySite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('', views.home, name="home"),
    path('about/', views.aboutUs, name="about"),
    path('contect/', views.contectUs, name="contect"),
    path('course/', views.course, name="course"),
    path('course/<slug:courseid>', views.courseDetaild),
    path('submitform/', views.submitform, name="submitform"),
    path('calculator/', views.calculator, name="calculator"),
    path('even-odd/', views.even_odd, name="even_odd"),
    path('marksheet/', views.marksheet, name="marksheet"),
    path('news/<slug>', views.news, name="news"),
    path('forms', views.forms, name="forms"),
]

if settings.DEBUG:
    urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)