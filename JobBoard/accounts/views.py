from django.shortcuts import render, redirect
from .forms import SignupForm, UserForm, ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profile
from django.urls import reverse

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            passowrd = form.cleaned_data['password1']
            # authenticate(username=username, passowrd=passowrd)
            login(request, user)
            return redirect('/accounts/profile')
    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', context={'form':form})

def profile(request):
    profile = Profile.objects.get(user=request.user)
    print('sameeeer')
    print(request.user)
    return render(request, 'accounts/profile.html',context={'profile':profile})

def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES, instance=profile)

        if userform.is_valid() and profileform.is_valid():
            
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_edit.html', context={'userform':userform, 'profileform':profileform})