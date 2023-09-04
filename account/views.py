from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib import messages


def register(request):
    register_form = CreateUserForm()

    if request.method == 'POST':
        register_form = CreateUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('store:store')
    context = {
        'form': register_form,
    }
    return render(request, template_name='account/registration/register.html', context=context)
