from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'app/product_list.html'

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'app/product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'category']
    template_name = 'app/product_create.html'

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'category']
    template_name = 'app/product_update.html'

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'app/product_delete.html'
    success_url = reverse_lazy('product')



def review_page(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        description = request.POST.get('description')
        
        
        return redirect('home')
    
    return render(request, 'app/review.html')



def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        
        
        return HttpResponse("Thank you for your message. We'll get back to you soon!")
    
    return render(request, 'app/contact.html')


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'app/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        return render(request, 'app/login.html', {'form': form})

class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'app/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'app/signup.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')



class PaymentView(View):
    def get(self, request):
        return render(request, 'app/payment.html')

    def post(self, request):
        payment_method = request.POST.get('payment_method')
        payment_details = request.POST.get('payment_details')
        amount = request.POST.get('amount')

        
        print(f"Payment Method: {payment_method}")
        print(f"Payment Details: {payment_details}")
        print(f"Amount: {amount}")

        
        return redirect('home')
    
    