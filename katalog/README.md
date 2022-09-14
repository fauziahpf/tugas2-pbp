# Tugas 2 PBP - Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

Fauziah Putri Fajrianti - 2106707435 - EZ

Kelas PBP A


# Link Heroku: 
https://tugas-2-sissy.herokuapp.com  

https://tugas-2-sissy.herokuapp.com/katalog 


# 1. Bagan
(Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html)
    
![Gambar]('../../bagan.png?raw=true')
    
Client mengirim request yang masuk ke server Django untuk kemudian diterima oleh urls.py. Request tersebut oleh urls.py diteruskan ke views.py dan fungsi yang berada dalam views.py akan dijalankan. Dalam prosesnya, views.py akan mengambil query dari models.py lalu database akan mengembalikan hasil query-nya. Hasil data tersebut akan di-render ke templates dalam berkas HTML untuk diperlihatkan ke user atau client sebagai respons.


# 2. Virtual Environment

(Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?)

Virtual environment digunakan untuk mengelola dan membangun environment terpisah untuk proyek tertentu dengan mengisolasi package serta dependencies dari aplikasi yang dibangun sehingga tidak berbenturan dengan versi lain yang ada pada perangkat kita. Dengan itu, menggunakan virtual environment memungkinkan kita untuk menghindari menginstal paket Python secara global yang dapat merusak package dan dependencis proyek lain di penyimpanan perangkat kita.
Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi hal tersebut dapat secara otomatis meng-update packages dan dependencies di proyek lain di penyimpanan kita yang dapat mengakibatkan perbedaan versi-versi data.


# 3. Poin 1 - 4        

(Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.)
    
## Poin 1 

    (membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML).

Dalam folder katalog, dibuat terlebih dahulu sebuah fungsi show_katalog pada views.py yang menerima parameter request, lalu dibuat list untuk mengambil data dari database serta dibuat context yang berisi variable data dari database, serta variable lainnya seperti nama, dan ID, sehingga data tersebut dapat ikut di-render oleh Django.
Fungsi ini mengembalikan hasil render untuk dibawa ke HTML.

## Poin 2

    (membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py).

Dalam file katalog/urls.py:
1) Import path dan show_katalog (dari views.py)
2) Variable app_name disesuaikan dengan nama app yang dibuat (yakni katalog)
3) Membuat routing untuk memetakan fungsi show_katalog dengan menambahkan path('', show_katalog, name='show_katalog') pada variable urlpatterns

Dalam file project_django/urls.py:
1) Menambahkan path('katalog/', include('katalog.urls')) pada variable urlpatterns untuk melakukan me-routing '/katalog' dengan katalog/urls.py untuk bisa menggunakan fungsi show_katalog yang ada di katalog.views.py

## Poin 3

    (memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.)

Hasil render dari fungsi show_katalog di katalog/views.py akan dibawa ke templates/katalog.html. Dilakukan mapping data ke dalam HTML dengan menggunakan sintaks khusus dari Django, yakni {{data}} pada file templates/katalog.html.
Untuk menampilkan nama dan npm, digunakansintaks {{nama}} dan {{id}}. Untuk menampilkan seluruh data barang katalog, dibuat for loop yang mengambil data dari list_barang.

## Poin 4

    (melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-teman melalui Internet.)

1) Membuat *new app* pada Heroku, kemudian menyalin API Key dari akun milik sendiri. API Key beserta informasi tentang aplikasi Heroku pada file teks. 
2) Membuka konfigurasi repositori GitHub dan bagian Secrets untuk GitHub Actions, kemudian menambahkan variabel repository secret baru, yakni variabel untuk API Key dan nama App.
3) Menjalankan workflow kembali

