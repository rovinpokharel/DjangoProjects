from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from .forms import RestaurantLocationModelForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView
# from .models import RestaurantLocation
from .models import RestaurantLocation
from django.db.models import Q
from django.urls import reverse_lazy
from django.http import Http404


# Create your views here.
# def hello(request):

#     context = {}
#     return render(request, "hello.html",context)

# def welcome(request):
#     context = {
#         "restaurant_name" : "Syanko Rolls",
#         "items" : ["katti roll" , "chicken roll"],
#         "Branches" : ["Pepsicola","Koteshower","Sankhamul"]
#     }
#     return render(request, "welcome.html", context)

# def contact(request):
#     context = {
#         "name": "Biraj Raut",
#         "Address": "Koteshower",
#         "Email": "birajraut777@gmail.com",
#         "Phone" : "9860384625"
#     }
#     return render(request, "contact.html",context)

# class AboutView(View):
#     # to define class name use capital letters in first word e.g class HelloWorld()
#     def get(self, request):
#         return render(request,"about.html")

# class HelloTemplateView(TemplateView):
#     template_name = "hello.html"
#
#     def get_context_data(self, **kwargs):
#         context = {}
#         return context

# class WelcomeTemplateView(TemplateView):
#     template_name = "welcome.html"
#
#     def get_context_data(self, **kwargs):
#         context = {
#                  "restaurant_name" : "Syanko Rolls",
#                  "items" : ["katti roll" , "chicken roll"],
#                  "Branches" : ["Pepsicola","Koteshower","Sankhamul"]
#              }
#         return context

# class ContactTemplateView(TemplateView):
#     template_name = "contact.html"
#
#     def get_context_data(self, **kwargs):
#         context = {
#                  "name": "Biraj Raut",
#                  "Address": "Koteshower",
#                  "Email": "birajraut777@gmail.com",
#                  "Phone" : "9860384625"
#              }
#         return context

# def restaurant_list(request):
#     template_name = "restaurants\\restaurantlocation_list.html"
#     query_set = RestaurantLocation.objects.all()
#     context = {"restaurants":query_set}
#     return render(request,template_name,context)

class RestaurantListView(LoginRequiredMixin,ListView):
    # LoginRequiredMixin le kei page kholnu agadi login garna parcha bhancha
    template_name = "restaurants\\restaurantlocation_list.html"
    login_url = reverse_lazy('userauth:login')

    # def get_queryset(self):
        # slug = self.kwargs.get("slug")
        # if not slug:
        #     queryset = RestaurantLocation.objects.all()
        # else:
            # queryset = RestaurantLocation.objects.filter(category__exact=slug)
            # queryset = RestaurantLocation.objects.filter(
                # Q(category__iexact=slug) |
                # Q(category__contains=slug) |
                # Q(location__contains=slug))
        # return queryset
    #
    # def get_success_url(self):
    #     return reverse_lazy('restaurants:list')

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = RestaurantLocation.objects.filter(owner__username__exact=user)
        else:
            raise Http404
        return queryset



class RestaurantDetailView(LoginRequiredMixin,DetailView):
    login_url = reverse_lazy('userauth:login')
    def get_object(self, queryset=None):
        # rest_id = self.kwargs.get("rest_id")
        slug = self.kwargs.get("slug")
        # obj = get_object_or_404(RestaurantLocation, id=rest_id)
        obj = get_object_or_404(RestaurantLocation,slug=slug)
        # obj = RestaurantLocation.objects.filter(id = rest_id)
        return obj
    def get_success_url(self):
        return reverse_lazy('restaurants:detail')


# class NonVegView(ListView):
#     queryset = RestaurantLocation.objects.filter(category__contains="non")
#     template_name = "restaurants\\restaurantlocation_list.html"

def restaurant_createview(request):
    form = RestaurantLocationModelForm(request.POST or None)
    errors = ""

    print("request.POST: ()".format(request.POST))
    print("request.GET: ()".format(request.GET))
    print("Form is valid: ()".format(form.is_valid))

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy('restaurants:list'))
    if form.errors:
        errors = form.errors

    template_name = 'restaurants/form.html'
    context = {"restaurant_form": form, "form_error":errors}
    return render(request,template_name,context)

class RestaurantCreateView(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('userauth:login')
    form_class = RestaurantLocationModelForm
    template_name = "restaurants/form.html"
    success_url = reverse_lazy('restaurants:list')

    def form_valid(self, form):
        instance = form.save(commit = False)
        instance.owner = self.request.user
        return super().form_valid(form)