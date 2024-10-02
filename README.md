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


=====================================================================================================================================================================
## tugas 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery diperlukan dalam pengimplementasian sebuah platform karena dalam pengembangan suatu platform akan ada masa dimana kita perlu untuk mengirimkan data dari satu stack ke stack lainnya. Data yang dikirimkan bisa bermacam-macam bentuknya. Contoh dari format data yang umum digunakan antara lain adalah HTML, XML, dan JSON. Pada akhirnya Data delivery memungkinkan interaksi antara pengguna, sistem, dan data yang ada pada database.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya di antara XML atau JSON lebih baik antara satu dengan yang lainnya bergantung kepada kondisi. Ketika data memiliki struktur yang kompleks sehingga membutuhkan validasi data dengan level intensitas lebih tinggi seperti pada pertukaran data pada perbankan XML akan lebih unggul dikarenakan XML mendukung skema (XSD) yang mempermudah validasi struktur data. Namun XML perlu untuk diparse menggunakan XML parser sehingga tingkat fleksibilitasnya kurang baik dibandingkan JSON yang dapat diparse menggunakan fungsi JavaScript standar.

Namun ketika menghadapi data yang menggunakan struktur data yang tidak kompleks JSON akan lebih baik. Penyebabnya adalah JSON lebih efisien karena ukurannya yang lebih kecil dibanding XML sehingga menjadi lebih cepat ketika akan digunakan, penyebab lainnya adalah karena dalam komunikasi client-server JSON lebih ringan, sehingga memungkinkan pertukaran data yang lebih cepat baik pada peramban internet maupun pada perangkat mobile. Hal inilah yang menyebabkan JSON lebih popular dibandingkan XML.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Fungsi tersebut digunakan untuk memvalidasi isi input dari form tersebut sesuai atau tidak dengan jenis field yang diminta, sesuai atau tidak dengan jumlah maksimal char yang diminta. Ketika field yang diisi tidak mencapai kriteria yang terdapat pada field tersebut maka is_valid() akan mengembalikan false dan form tidak akan tersubmit atau tersimpan.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf_token adalah token yang berfungsi sebagai security. Token ini di-generate secara otomatis oleh Django untuk mencegah seragnan berbahaya. Selain itu token csrf juga digunakan untuk memverifikasi bahwa permintaan yang datang dari form benar-benar berasal dari pengguna yang dituju dan bukan dari sumber eksternal yang jahat. Jika tidak menambahkan csrf_token pada form di Django, Django tidak dapat memberifikasi permintaan yang masuk berasal dari halaman yang sah atau bukan.

Dengan tidak ditambahkannya token_csrf maka penyerang akan dapat melakukan serangan phishing yang mengakibatkan aplikasi yang kita bangun melakukan post yang bukan kita inginkan. Serangan-serangan lain pun dapat dilakukan oleh oknum-oknum yang jahat. Hal tersebut terjadi ketika penyerang memanfaatkan fakta bahwa pengguna mungkin telah login ke aplikasi web dan memiliki sesi yang aktif. Tanpa adanya token_csrf sesi aktif tersebut dapat digunakan oleh penyerang untuk melakukan banyak hal tidak bertanggung jawab.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Mengubah primary key yang pada awalnya incremental integer menjadi UUID untuk melindungi kita.Buat berkas baru pada direktori main dengan nama forms.py untuk membuat struktur form yang dapat menerima data Material Entry baru. Tambahkan fields dan juga model yang sesuai. Lalu melakukan from django.shortcuts import redirect dan melakukan import terhadap MaterialEntryForm yang sebelumnya sudah kita definisikan sebagai suatu class pada file forms.py, hal-hal tersebut diimplementasikan pada file views.py yang terdapat pada direktori main. Selannjutnya kita perlu menambahkan fungsi dengan parameter request untuk menampilkan form dan juga menyimpan form jika form sudah tervalidasi melalui request. Selanjutnya pada fungsi show_main() pada views.py kita ubah agar material_entries = MaterialEntry.objects.all() untuk mengobjektivikasi masukkan dari pengguna.

Selanjutnya import fungsi create_material_entry yang terdapat pada views.py pada direktori main ke urls.py yang juga terdapat pada direktori main. Untuk membuat routing kita menambahkan create_product_entry untuk mengisi parameter-parameter pada path baru untuk merouting.

langkah berikutnya, kita hanya perlu menambahkan create_material_entry.html pada direktori templates yang terdapat pada direktori main, file ini adalah template untuk form yang melakukan permintaan request terhadap create_material_entry(request) yang terdapat pada views.py.

langkah terakhir adalah untuk menambahkan 4 fungsi untuk view pada views.py
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

fungsi fungsi di atas digunakan untuk mengidentifikasi objek-objek yang telah menjadi baik xml maupun JSON. Fungsi yang melakukan show dengan menggunakan id dapat mengembalikan objek dengan menggunakan id. Lalu dilanjut dengan menambahkan path routing pada urls.py yang terdapat pada direktori main agar fungsi-fungsi tersebut dapat kita akses sesuai dengan url yang tercantum.

6. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md

   show_xml()
   ![image](https://github.com/user-attachments/assets/418146d4-1f2c-4d79-8e8f-e25e7d884994)


   show_json()
   ![image](https://github.com/user-attachments/assets/af7b1942-bfab-4981-aef1-ae8cca06cb98)


   show_xml_by_id()
   ![image](https://github.com/user-attachments/assets/03c18c6e-f740-4a28-8d32-fbd7a5d9cfe3)


   show_json_by_id()
   ![image](https://github.com/user-attachments/assets/a8cb908a-fe8e-4c18-9872-d16322fac892)


==============================================================================================================
## tugas 4

## Apa perbedaan antara HttpResponseRedirect() dan redirect()

### HttpResponseRedirect()
- **Definisi**: Respons HTTP yang secara eksplisit menginstruksikan browser untuk memuat ulang halaman yang berbeda. Ini merupakan metode standar dalam HTTP untuk mengalihkan pengguna ke URL lain.
- **Penggunaan**: Memerlukan URL tujuan secara eksplisit sebagai argumen. Ini memberikan kontrol penuh atas URL tujuan tetapi meningkatkan risiko kesalahan ketik.
- **Fleksibilitas**: Kurang fleksibel karena hanya berinteraksi dengan string URL. Ini membatasi penggunaannya dalam skenario di mana URL tujuan ditentukan secara dinamis.
- **Contoh Penggunaan**: response = HttpResponseRedirect(reverse("main:show_main"))
- **Keterbacaan Kode**: Kurang intuitif bagi pemula karena memerlukan penulisan URL secara manual. Ini dapat membuat kode kurang mudah dibaca dan dipahami.
- **Kemudahan Penentuan URL**: Memerlukan penulisan URL secara manual, yang dapat rentan terhadap kesalahan.
- **Mekanisme Internal**: Secara langsung menghasilkan objek `HttpResponseRedirect` yang berisi header HTTP `Location` dengan URL tujuan.

### Redirect()
- **Definisi**: Fungsi utilitas Django yang menyediakan cara yang lebih abstrak dan ringkas untuk membuat respons redirect. Fungsi ini menyembunyikan kompleksitas dalam pembuatan respons redirect HTTP.
- **Penggunaan**: Dapat diberikan URL tujuan, nama view, atau objek model sebagai argumen. Ini memberikan fleksibilitas yang lebih tinggi, terutama saat menggunakan URL yang dinamis atau terkait dengan model data.
- **Fleksibilitas**: Lebih fleksibel karena mendukung berbagai cara untuk menentukan URL tujuan. Ini memungkinkan integrasi yang lebih baik dengan struktur aplikasi Django.
- **Contoh Penggunaan**: return redirect('main:show_main')
- **Keterbacaan Kode**: Lebih intuitif dan mudah dibaca karena menggunakan nama view atau objek model yang lebih bermakna. Ini membuat kode lebih berorientasi pada konsep daripada detail implementasi.
- **Kemudahan Penentuan URL**: Otomatis menangani penentuan URL ketika menggunakan nama view atau objek model. Ini mengurangi kemungkinan kesalahan dan meningkatkan produktivitas.
- **Mekanisme Internal**: Membungkus logika pembuatan objek `HttpResponseRedirect` dan menyederhanakan proses bagi pengembang.

### Kesimpulan:
- **HttpResponseRedirect()** memberikan kontrol penuh atas URL tujuan tetapi kurang fleksibel dan lebih merepotkan dalam penggunaannya.
- **redirect()** lebih mudah digunakan, lebih fleksibel, dan lebih sesuai dengan prinsip-prinsip pemrograman Django.


## Jelaskan cara kerja penghubungan model Product dengan User!

Mendefinisikan Relasi pada models.py dilakukan dengan melakukan from django.contrib.auth.models import User, yang merupakan model bawaan Django untuk manajemen pengguna.

    user = models.ForeignKey(User, on_delete=models.CASCADE)

ForeignKey: Menunjukkan bahwa untuk semua objek Product terhubung dengan satu objek User. Namun, satu User dapat memiliki banyak Product

on_delete=models.CASCADE: Jika pengguna (User) dihapus, maka semua produk yang dimiliki olehh pengguna tersebut juga akan dihapus dari database. Ini mengamankan integritas data dengan memastikan bahwa produk tidak memiliki referensi pengguna yang sudah tidak ada.

    material_entries = MaterialEntry.objects.filter(user=request.user)

digunakan untuk mendapatkan semua produk yang dimiliki oleh pengguna yang sedang login. Hal tersebut dilakukan dengan menyaring seluruh objek dan hanya mengambil Material Entry yang dimana field user terisi dengan objek User yang sama dengan pengguna yang sedang login

        material_entry.user = request.user

Pada views.py perintah di atas digunakan untuk menetapkan user sebagai pengguna yang sedang login


## Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

from django.contrib.auth import authenticate, login, logout


1. **Authentication pada Django**
- Django menggunakan middleware otentikasi bawaan (`django.contrib.auth`) yang menyediakan fungsi login, logout, dan sistem manajemen pengguna.

from django.contrib.auth import authenticate, login, logout


login(request, user)


Django menyediakan fitur otentiikasi bawaan seperti pada perintah di atas. fitur login di atas adalah salah satunya. Fitur di atas memungkinkan pengguna untuk memulai session.

2. **Authorization di Django**
- Django mengatur izin dengan menggunakan model `Permissions` dan grup yang dapat diberikan kepada pengguna.

@login_required(login_url='/login')


potongan kode di atas terdapat di atas fungsi show_main yang berarti halaman show_main hanya akan dapat diakses oleh pengguna yang sudah terautentikasi, dalam hal ini login.

## Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?


