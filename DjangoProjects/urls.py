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
from django.contrib.auth.views import LogoutView
from django.urls import include

from restaurants.views import (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView,
)
from userauth.views import SignUpView, UserProfileView, UserLoginView, UserProfileUpdateView


from restaurants.views import RestaurantListView, RestaurantDetailView,restaurant_createview,RestaurantCreateView
from userauth.views import UserLoginView,SignUpView,UserProfileView,UserProfileUpdateView
from django.contrib.auth.views import LogoutView
# from restaurants.views import restaurant_list


# urlpatterns = [
    # path('admin/', admin.site.urls),
    # path ('home/',TemplateView.as_view(template_name="hello.html")),
    # path ('about/',TemplateView.as_view(template_name="about.html")),
    # path ('restaurant/',RestaurantListView.as_view()),
    # # path('restaurant/<str:slug>',RestaurantListView.as_view()),
    # path('restaurant/<int:rest_id>/',RestaurantDetailView.as_view()),
    # path('restaurant/<str:slug>',RestaurantDetailView.as_view()),
    # # path('restaurant/create/',restaurant_createview),
    # path('restaurant/create/',RestaurantCreateView.as_view()),
    # path('login/',CustomLoginView.as_view()),
    # path('logout/',LogoutView.as_view(next_page='/login/')),
    # path('signup/',SignUpView.as_view()),
    # path('user-profile/',UserProfileView.as_view()),
    # path('user-profile/update/',UserProfileUpdateView.as_view()),
    # ]
    # path('home/', hello), #home page open by calling function or html file hello
    # path('welcome/', welcome),
    # path('contact/', contact),
    # path('about/', AboutView.as_view()),
    # class call garna .as_view() add garnaparcha
#     path('home/', HelloTemplateView.as_view()),
#     path('welcome/', WelcomeTemplateView.as_view()),
#     path('contact/', ContactTemplateView.as_view()),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("userauth.urls", namespace="userauth")),
    path('restaurant/', include("restaurants.urls", namespace="restaurants")),
    path('home/', TemplateView.as_view(template_name="hello.html"), name="home"),
    path('about/', TemplateView.as_view(template_name="about.html"), name="about"),
    path('items/', include("fooditem.urls", namespace="fooditem")),
]
