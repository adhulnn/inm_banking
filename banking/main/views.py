from django.shortcuts import render,redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import ContinueRegisterForm
from django.http import JsonResponse
from django.views import View
from .models import *
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.contrib import messages

# Create your views here.


def index(req):
    return render(req, 'home.html')

# def index(request):
#     success_message = request.GET.get('success', None)
#     return render(request, 'home.html', {'success_message': success_message})

# ---------------------------------

@login_required
def after_login(request):
    if request.method == 'POST':
        form = ContinueRegisterForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            success_message = 'Your application has been submitted successfully.'
            return render(request, 'home.html', {'success_message': success_message})
        else:
            messages.error(request, 'There was an error in your submission. Please check the form.')
    else:
        form = ContinueRegisterForm()

    return render(request, 'after_login.html', {'form': form})

def load_branches(request):
    district_id = request.GET.get('district')
    branches = Branch.objects.filter(district_id=district_id)
    return render(request, 'branch_options.html', {'branches': branches})
   

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('after_login')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
