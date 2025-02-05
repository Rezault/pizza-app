from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html")


@login_required
def profile(request):
    if request.user.is_authenticated:
        return render(request, "profile.html")
    else:
        return redirect("login")
    

def signup(request):
    if request.user.is_authenticated:
        return redirect("profile")

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Creates the user
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})