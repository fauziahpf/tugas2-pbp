# Tugas 3 PBP - Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

Fauziah Putri Fajrianti - 2106707435 - EZ

Kelas PBP A


# Link Heroku: 
https://tugas-2-sissy.herokuapp.com/todolist/


# 1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
{% csrf_token %} merupakan token yang dibentuk pada setiap *user session* berupa suatu *random value* yang sulit untuk ditebak. {% csrf_token %} pada elemen <form> berguna untuk membentuk token dan memeriksa kembali untuk setiap permintaan yang masuk dengan cara membandingkan *value*-nya saat memasuki <form> dan setelah pengguna mengirim *request* untuk men-*submit* data. Apabila *value*-nya berbeda, server akan menolak *request* tersebut. Karena {% csrf_token %} juga berguna untuk mencegah CSRF Attack, *user session* tersebut akan dihapus dan dicatat sebagai potensi CSRF Attack. 

Jika tidak ada potongan kode {% csrf_token %} pada elemen <form>, *website* tetap bisa berjalan, tetapi akan terdapat beberapa route link sensitif yang dapat diakses oleh orang lain (contohnya *logout* dan *delete account*). Akun pengguna dapat dikendalikan orang lain (di-*logout* atau dihapus) tanpa izin pengguna.


# 2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Kita dapat membuat elemen secara manual (tanpa menggunakan *generator* seperti {{ form.as_table }}). Untuk membuat *form* tersebut, digunakan *tag form* untuk HTML dan digunakan method POST. Di dalamnya, dibuat *tag* input sesuai kebutuhan. Dalam *tag input* ini, menggunakan atribut *text* dan *submit*, form akan menerima input dari pengguna berupa text untuk di-*submit*. Dibuat pula tombol untuk pengguna tekan agar bisa dikirim data *input* ke *server*.


# 3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML. 
Pada laman form, pengguna akan memasukkan data pada input field yang telah disediakan dan melalui tombol submit akan dikirim. Selanjutnya, terdapat function dalam views.py yang akan mengakses data dari form tersebut dengan membuat variabel berisi `request.POST.get(input name)`. Lalu, dibuat database untuk menyimpan data tersebut melalui `(model name).objects.create(attributes = variabel)`. Dari database, objek data tersebut di-deliver kembali ke context untuk kemudian di-render ke target HTML. Objek dari context bisa diiterasi dalam loop dan ditampilkan per attribut nya. Dengan ini, data akan muncul ke tampilan HTML yang diakses oleh pengguna.


# 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Membuat suatu aplikasi baru bernama todolist di proyek repositori tugas 2 lalu melalui perintah ` python manage.py startapp todolist `
- Menambahkan kode ` path('todolist/', include('todolist.urls')) ` ke urlspatterns di project_django/urls.py
- Membuat sebuah model Task di todolist/models.py dengan atribut dan field sesuai dengan ketentuan tugas.
- Membuat fungsi register, login_user, dan logout_user di todolist/views.py serta membuat login.html dan register.html di folder templates
- Membuat taskform.html berisi form untuk mengambil input dari pengguna berupa judul task dan deskripsi task, serta tombol submit untuk kirim data. 
- Membuat fungsi add_task untuk mengakses data dari form dengan membuat variabel berisi ` request.POST.get(input name) `. Lalu, dibuat database untuk menyimpan data tersebut melalui ` (model name).objects.create(attributes = variabel) `.
- Membuat restriksi untuk fungsi selain register, login_user, dan logout_user dengan menambahkan @login_required(login_url='/todolist/login/') diatas fungsinya.
- Pada todolist.html, yakni halaman untuk menampilkan To-Do List pengguna, hasil render dari fungsi show_todo dipetakan ke dalam HTML ini menggunakan sintaks khusus dari Django. Contohnya, username pengguna ditampilkan menggunakan sintaks {{username}}. Dibuat juga tabel berisi data task milik pengguna (yang sudah tersimpan di database setelah submit di form) dan dua tombol untuk tambah task baru dan logout. 
- Menambahkan kode berikut ke urlspatterns di mywatchlist/urls.py:
    ```
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('task/', add_task, name='add_task'),
    ```
    agar pengguna dapat meregistrasi akun, login dan logout, serta menambahkan task baru di url yang sesuai
- Deploy ke Heroku dan membuat dua pengguna dengan tiga dummy data untuk masing-masing pengguna.