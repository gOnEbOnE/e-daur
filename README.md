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