from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm, ProfileForm
from .models import Profile
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy



def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to='index')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='index')
        else:
            return render(request, 'users/signup.html', context={"form": form})

    return render(request, 'users/signup.html', context={"form": RegisterForm()})

def loginuser(request):
    if request.user.is_authenticated:
       return redirect(to='index')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, "Ім'я користувача або пароль не збігаються")
            return redirect(to='/users/login')

        login(request, user)
        return redirect(to='index')

    return render(request, 'users/login.html', context={"form": LoginForm()})

@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='index')


@login_required
def profile(request):
    profile_instance, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=profile_instance
        )
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Ваш профіль успішно оновлено")
            return redirect(to="users:profile")

    profile_form = ProfileForm(instance=profile_instance)
    return render(request, "users/profile.html", {"profile_form": profile_form})


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    html_email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')
    success_message = "Електронний лист із інструкціями щодо зміни пароля надіслано на адресу %(email)s."
    subject_template_name = 'users/password_reset_subject.txt'