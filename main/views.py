from django.shortcuts import render, redirect, reverse
from main.forms import MaterialEntryForm
from main.models import MaterialEntry
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def delete_material(request, id):
    # Get mood berdasarkan id
    material = MaterialEntry.objects.get(pk = id)
    # Hapus mood
    material.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

def edit_material(request, id):
    # Get mood entry berdasarkan id
    material = MaterialEntry.objects.get(pk = id)

    # Set mood entry sebagai instance dari form
    form = MaterialEntryForm(request.POST or None, instance=material)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_material.html", context)
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def show_xml(request):
    data = MaterialEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MaterialEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MaterialEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MaterialEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login')
def show_main(request):
    material_entries = MaterialEntry.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'class' : 'C',
        'web' : 'E-Daur',
        'fullname' : 'Christopher Matthew Hendarson',
        'npm' : '2306245592',
        'item_name' : 'kotak pensil',
        'price': 'Rp 0',
        'description': 'kotak pensil',
        'material_entries' : material_entries,
        'image': 'https://i.imgur.com/fHwFRmz.jpeg',
        'last_login': request.COOKIES['last_login'],

    }

    return render(request, "main.html", context)

def create_material_entry(request):
    form = MaterialEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        material_entry = form.save(commit=False)
        material_entry.user = request.user
        material_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_material_entry.html", context)

