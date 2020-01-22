from django.urls import path
from .views import FoodItemListView, FoodItemDetailView,FoodItemCreateView,FoodItemUpdateView

app_name = 'fooditem'

urlpatterns = [
    path('',FoodItemListView.as_view(),name="list"),
    path('create/', FoodItemCreateView.as_view(), name="create"),
    path('<str:pk>/',FoodItemDetailView.as_view(),name="detail"),
    path('<str:pk>/update/',FoodItemUpdateView.as_view(), name="update"),
]