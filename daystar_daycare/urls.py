"""
URL configuration for daystar_daycare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from pages.views import home, login, sitter, babies, shop, sitters, about, contact, baby, delete, erase, edit, update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='login'),
    path('index', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('sitter/', sitter, name='sitter'),
    path('sitters/', sitters, name='sitters'),
    path('babies/', babies, name='babies'),
    path('baby/', baby, name='baby'),
    path('shop/', shop, name='shop'),
    path('delete/<int:baby_id>', delete, name='delete'),
    path('erase/<int:sitter_id>', erase, name='erase'),
    path('edit/<int:baby_id>', edit, name='edit'),
    path('update/<int:sitter_id>', update, name='update'),
]
