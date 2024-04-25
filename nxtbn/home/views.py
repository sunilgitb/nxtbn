from django.shortcuts import render, redirect
from django.urls import reverse

def home(request):
    if request.user.is_authenticated:
        return redirect(reverse('api_playground'))
    else:
        return redirect(reverse('account_login'))
