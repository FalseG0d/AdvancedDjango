from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/admin')
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect('/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'changepassword.html', {
            'form': form
        })