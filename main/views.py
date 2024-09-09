from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'web' : 'E-Daur',
        'fullname' : 'Christopher Matthew Hendarson',
        'npm' : '2306245592',
        'nama' : 'kotak pensil',
        'harga': 'Rp 0',
        'description': 'kotak pensil',
        'rating': '1',
        'image': 'https://i.imgur.com/fHwFRmz.jpeg'
    }

    return render(request, "main.html", context)