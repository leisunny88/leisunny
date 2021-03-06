from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth import authenticate, login
from .forms import LoginFrom, RegistrationFrom, UserProfileForm


def user_login(request):
    if request.method == "POST":
        login_form = LoginFrom(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return HttpResponse("Wellcome You. You have been authenticated successfully")
            else:
                return HttpResponse("Sorry. You username or password is not right")
        else:
            return HttpResponse("Invalid login")

    if request.method == "GET":
        login_form = LoginFrom()
        return render(request, "account/login.html", {"form": login_form})


def register(request):
    if request.method == 'POST':
        user_form = RegistrationFrom(request.POST)
        user_profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and user_profile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = user_profile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return HttpResponse('successfully')

        else:
            return HttpResponse('sorry, you can not register')

    else:
        user_form = RegistrationFrom()
        user_profile_form = UserProfileForm()
        return render(request, 'account/register.html', {'form': user_form, 'profile': user_profile_form})


