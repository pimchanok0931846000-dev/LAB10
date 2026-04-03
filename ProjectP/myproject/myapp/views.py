from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Person

# Create your views here.
def index(request):
    all_persons = Person.objects.all()
    return render(request, 'index.html', {'all_persons': all_persons})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'form.html')

def add_person(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        Person.objects.create(name=name, age=age)
        return redirect('index')
    return render(request, 'form.html')

def edit_person(request, id):
    person = get_object_or_404(Person, id=id)
    if request.method == 'POST':
        person.name = request.POST.get('name')
        person.age = request.POST.get('age')
        person.save()
        return redirect('index')
    return render(request, 'edit.html', {'person': person})

def delete_person(request, id):
    person = get_object_or_404(Person, id=id)
    person.delete()
    return redirect('index')
