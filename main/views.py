from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama' : 'kotak pensil',
        'harga': 'Rp 0',
        'description': 'kotak pensil',
        'rating': '1'
    }

    return render(request, "main.html", context)