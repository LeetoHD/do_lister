from email.mime import message
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import CustomRegisterForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New user added")) 
            return redirect('register')
    else:
        register_form = CustomRegisterForm()
    return render(request, 'user.html', {'register_form': register_form})