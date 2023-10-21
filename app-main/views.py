from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django import forms

class Userform(forms.Form):
    first_name = forms.CharField(max_length=100, min_length=1, label='имя:   ')
    last_name = forms.CharField(max_length=100, min_length=1, label='фамилия:')


def index(request):
    context = {
        'users': users
    }
    return render(request, 'app/index.html', context)


def add(request):
    if request.method == "GET":
        form_fields = Userform()
        context = {
            'form_fields': form_fields

        }
        return render(request, 'app/add.html', context)
    elif request.method == "POST":
        form_fields = Userform(request.POST)
        if form_fields.is_valid():
            first_name = form_fields.cleaned_data['first_name']
            last_name = form_fields.cleaned_data['first_name']
            user = first_name + ' ' last_name
            users.append(user)
            return redirect('app:index')
        else:
            return render(request, 'app/add.html', context)
    else:
        return HttpResponseNotAllowed(['POST', 'GET'], content='Ошибка этот метод не разрешен!')
    
    