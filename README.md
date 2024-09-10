## http://christopher-matthew31-daurelektronik.pbp.cs.ui.ac.id/
## Christopher Matthew Hendarson
## Tugas 2
## 2306245592

1.bagaimana cara kamu mengimplementasikan checklist?

- Membuat sebuah proyek Django baru dilakukan dengan membuat direktori utama yang bernama E-DAUR, pada direktori tersebut saya membuka terminal shell lalu membuat virtual environment dengan perintah "python -m venv env". Virtual environment berguna untuk mengisolasi package serta depencdencies dari aplikasi agar tidak bertabrakan dengan versi lain yang ada pada komputer saya. Dilanjutkan dengan melakukan instalasi terhadap dependencies yang ada dengan menginstall requirements.txt. lalu membuat proyek Django yang bernama e_daur. dengan perintah "django-admin startproject e_daur ."
<br>
- Mambuat aplikasi dengan nama main pada proyek tersebut
saya membuat aplikasi dengan nama main pada proyek tersebut dengan menggunakan perintah "python manage.py startapp main" setelah perintah tersebut dijalankan, direktori dengan nama main akan terbentuk. Direktori tersebut berisi struktur awal untuk aplikasi Django saya.
<br>
-Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
Dilakukan dengan cara menambahkan 'main' ke dalam daftar aplikasi yang terdaftar di INSTALLED_APPSs pada berkas settings.py yang ada di direktori proyek e_daur.
<br>
- Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib(name, price, description)

Mengubah berkas models.py yang terdapat di dalam direkori aplikasi main untuk mendefinisikan model baru. Saya menambahkan beberapa atribut berupa name, price, description, rating, dan juga image yang memiliki field yang sudah disesuaikan dengan fungsi masing-masing.

Lalu dilanjutkan dengan melakukan migrasi model agar Django dapat melacak perubahan pada model basis data yang saya miliki.
<br>
-Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
Langkah pertama adalah membuka berkas views.py yang terletak di dalam berkas aplikasi main. Langkah selanjutnya adalah menambahkan fungsi show_main yang berisi context yang merupakan dictionary yang berisi data nama web, nama saya, NPM saya,nama produk, price(harga) produk, deskripsi(description) dari produk, rating fungsionalitas dari produk, dan gambar dari produk tersebut(image). Lalu mengembalikan render tampilan kotakpensil.html dengan menggunakan fungsi render dengan kode "return render(request, "kotakpensil.html", context).
<br>
-Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
Langkah pertama adalah membuka berkas urls.py di dalam direktori proyek e_daur lalu menambahkan impor fungsi include dari django.urls. Lalu menambahkan rute URL 'path('', include('main.urls')' pada urlpatterns untuk mengarahkan tampilan main di dalam variabel urlpatterns.
<br>
-Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet
Membuat proyek baru pada https://pbp.cs.ui.ac.id/ dengan nama daurelektronik lalu pada settings.py di proyek Django tadi saya menambahkan URL deployment PWS("christopher-matthew31-daurelektronik.pbp.cs.ui.ac.id") pada ALLOWED_HOSTS. Lalu saya melakukan git add, commit, push perubahan yang terjadi ke repositori GitHub saya. Selanjutnya menjalankan perintah yang terdapat pada informasi Project Command pada halaman PWS.
<br>
-Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
Menambahkan README.md pada direktori proyek e-daur
<br>

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.








