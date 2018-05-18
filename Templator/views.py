# -*- coding: utf-8 -*-
from django.views.generic.edit import FormView, CreateView
from django.shortcuts import render
from django.http import *
from .forms import FIOForms
from .models import Record
from .scripts import formToDocx


class ContactView(CreateView):
    model = Record
    form_class = FIOForms
    template_name = 'Templator/homePage.html'
    success_url = 'Templator/success.html'


def index(request):
    form_class = FIOForms
    # if request is not post, initialize an empty form
    form = form_class(request.POST, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            formToDocx.generate(data['first_name'], data['last_name'], data['father_name'], data['sex'], data['specialization'], data['groupNum'], data['excellentPercent'], data['ok_semesters'], data['achievementsList'])
        return HttpResponseRedirect('success.html')
    else:
        form = FIOForms()
    return render(request, 'Templator/homePage.html', {'form': form})


def success(request):
    return render(request, 'Templator/success.html')