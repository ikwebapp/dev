"""
URL configuration for ikweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index" ),
    path('info/', views.info, name="info" ),
    path('hpc/', views.hpc, name="hpc" ),
    path('Performance/', views.Performance, name="Performance" ),
     path('Applications/', views.Applications, name="Applications" ),
    path('signup/', views.sign_up, name="signup"),
    path('login/', views.user_login, name="login"),
    path('profile/', views.user_profile, name="profile"),   
    path('logout/', views.user_logout, name="logout"),  
    path('changepass/', views.user_changepass, name="changepass"), 
    path('changepass1/', views.user_changepass1, name="changepass1"),
    path('user_details/<int:id>', views.user_details, name="user_details")

]
