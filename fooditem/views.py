from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .models import FoodItem
from .forms import FoodItemForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class FoodItemListView(LoginRequiredMixin,ListView):
    login_url = reverse_lazy("userauth:login")
    template_name = r"fooditem\list.html"
    def get_queryset(self):
        return FoodItem.objects.filter(user__username__exact=self.request.user)

class FoodItemDetailView(LoginRequiredMixin,DetailView):
    login_url = reverse_lazy("userauth:login")
    template_name = r"fooditem\detail.html"
    def get_queryset(self):
        return FoodItem.objects.filter(user__username__exact=self.request.user)

class FoodItemCreateView(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy("userauth:login")
    form_class = FoodItemForm
    template_name = r"fooditem\form.html"
    success_url = reverse_lazy("fooditem:list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self,form):
        instance = form.save(commit = False)
        instance.user = self.request.user
        return super().form_valid(form)

class FoodItemUpdateView(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy("userauth:login")
    template_name = r"fooditem\form.html"
    form_class = FoodItemForm
    success_url = reverse_lazy("fooditem:list")

    def get_queryset(self):
        return FoodItem.objects.filter(user=self.request.user)

    def get_object(self,queryset = None):
        item_id = self.kwargs.get("pk")
        item_detail = get_object_or_404(FoodItem, pk = item_id)
        return item_detail

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs