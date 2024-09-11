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
Langkah pertama adalah membuka berkas views.py yang terletak di dalam berkas aplikasi main. Langkah selanjutnya adalah menambahkan fungsi show_main yang berisi context yang merupakan dictionary yang berisi data nama web, nama saya, NPM saya,nama produk, price(harga) produk, deskripsi(description) dari produk, rating fungsionalitas dari produk, dan gambar dari produk tersebut(image). Lalu mengembalikan render tampilan main.html dengan menggunakan fungsi render dengan kode "return render(request, "main.html", context).
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

![Blank diagram](https://github.com/user-attachments/assets/fa2600fb-73fc-4c3f-8e37-5e04329f7948)

Ketika user melakukan permintaan HTTP yang dilakukan melalui peramban web, alamat HTTP akan dikonfirmasi kebenarannya(sesuai atau tidak dengan url yang berada pada urls.py). Ketika sesuai permintaan akan dilanjutkan ke file views.py yang terdapat pada direktori main. Lalu permintaan tersebut akan disesuaikan dengan atribut-atribut yang terdapat pada models.py. Selanjutnya data dan atribut yang ada pada models.py dibaca dan juga ditulis ulang lalu disesuaikan dengan main.html yang terdapat pada direktori templates yang terdapat pada main. Pada template data tersebut akan disesuaikan lalu dilakukan render data input dari user sehingga tersesuaikan denngan template. Hasil tersebut dikirimkan kembali ke views.py lalu dikirimkan kembali oleh urls.py lalu dikembalikan sebagai tampilan web yang sudah tersesuaikan antara input dari user dan juga template yang sudah dibangun.

<br>
3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

Git digunakan untuk mengelola dan melacak perubahan dalam proyek pengembangan perangkat lunak. Dengan adanya Git pada pengembangan perangkat lunak, pelacakan perubahan kode, kolaborasi antar tim, dan juga perubahan versi ataupun riwayat pada proyek akan lebih mudah dilacak sehingga pengguna dapat kembali ke versi-versi sebelumnya jika ada sesuatu hal tidak terduga terjadi.

<br>
4.Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Menurut saya framework Django dijadikan sebagai permulaan pembelajaran pengembangan perangkat lunak salah satunya adalah karena dokumentasinya yang lengkap. Pada pembelajaran di kelas Bu Arawinda selalu meng-encourage mahasiswa untuk memerhatikan dan juga mempelajari dokumentasi Django. Karena Django juga ditulis dengan Python yang merupakan sintaks yang mudah dipelajari pada akhirnya mengakibbatkan Django lebih memungkinkan digunakan sebagai portal ataupun pintu masuk ke pembelajaran pengembangan web. Hal lainnya adalah juga karena Django merupakan full-stack, yang berarti Django sudah menyiapkan segala peralatan yang diperlukan pengembangan web baik dari sisi server maupun dari sisi klien. Ini memberi pemula seperti kami mahasiswa pengalaman pengembangan perangkat lunak yang lengkap, mulai dari mengelola database, menulis API, hingga merancang interface user.

<br>
5. Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM (Object-Relational Mapping) salah satunya adalah karena model ini menghubungkan antara dunia objek dalam Python dengan dunia tabel di basis data yang berhubungan(relational Database) yang merupakan jenis basis data yang menyimpan, mengelola dan mengorgaisasi data dalam bentuk tabel (sering disebut relasi). ORM memungkinkan interaksii dengan basis data tanpa harus menulis SQL secara langsung.







