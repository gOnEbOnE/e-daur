from django.shortcuts import render, redirect
from main.forms import MaterialEntryForm
from main.models import MaterialEntry
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
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

def show_main(request):
    material_entries = MaterialEntry.objects.all()
    context = {
        'web' : 'E-Daur',
        'fullname' : 'Christopher Matthew Hendarson',
        'npm' : '2306245592',
        'name' : 'kotak pensil',
        'price': 'Rp 0',
        'description': 'kotak pensil',
        'rating': '1',
        'material_entries' : material_entries,
        'image': 'https://i.imgur.com/fHwFRmz.jpeg'
    }

    return render(request, "main.html", context)

def create_material_entry(request):
    form = MaterialEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_material_entry.html", context)

