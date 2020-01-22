"""DjangoProjects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from restaurants.views import hello
# from restaurants.views import welcome
# from restaurants.views import contact
# from restaurants.views import AboutView
# from restaurants.views import HelloTemplateView
# from restaurants.views import WelcomeTemplateView
# from restaurants.views import ContactTemplateView
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from restaurants.views import RestaurantListView, RestaurantDetailView,restaurant_createview,RestaurantCreateView
from userauth.views import UserLoginView,SignUpView,UserProfileView,UserProfileUpdateView
from django.contrib.auth.views import LogoutView
# from restaurants.views import restaurant_list

from django.urls import path
from django.contrib.auth.views import LogoutView

from userauth.views import SignUpView, UserProfileView, UserLoginView, UserProfileUpdateView
app_name= "userauth"
urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="/login/"), name="logout"),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('user-profile/', UserProfileView.as_view(), name="profile"),
    path('user-profile/update/', UserProfileUpdateView.as_view(), name="update"),
]
