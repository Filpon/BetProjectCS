"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from pastmatchs.views import pastmatchsget, Cesvpastmatchs_upload, tablepastmatchs
from currentmatchs.views import currentmatchsget, Cesvcurrentmatchs_upload, tablecurrentmatchs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('pastmatchsget/', pastmatchsget, name="pastmatchsget"),
    path('upload-pastcsv/', Cesvpastmatchs_upload, name="Cesvpastmatchs_upload"),
    path('tablepastmatchs/', tablepastmatchs, name="tableslist"),
    path('currentmatchsget/', currentmatchsget, name="currentmatchsget"),
    path('upload-currentcsv/', Cesvcurrentmatchs_upload, name="Cesvcurrentmatchs_upload"),
    path('currentmatchstable/', tablecurrentmatchs, name="tablecurrentmatchs")
]