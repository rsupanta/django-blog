from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import (
    UserRegistrationForm,
    UserUpdateForm,
    ProfileUpdateForm,
    ProfileNameUpdateForm,
    ProfileImageUpdateForm,
)
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'{username}, Your account has been created successfully! You can log in now.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':

        p_img_form = ProfileImageUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        p_n_form = ProfileNameUpdateForm(
            request.POST,
            instance=request.user.profile
        )

        u_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )

        p_form = ProfileUpdateForm(
            request.POST,
            instance=request.user.profile
        )

        if p_img_form.is_valid() and p_n_form.is_valid() and u_form.is_valid() and p_form.is_valid():
            p_img_form.save()
            p_n_form.save()
            u_form.save()
            p_form.save()
            messages.success(
                request, f'Your account has been updated successfully!')
            return redirect('profile')

    else:
        p_img_form = ProfileImageUpdateForm(instance=request.user.profile)
        p_n_form = ProfileNameUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    full_name = request.user.profile.first_name + \
        ' ' + request.user.profile.last_name

    context = {
        'p_img_form': p_img_form,
        'full_name': full_name,
        'p_n_form': p_n_form,
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)
