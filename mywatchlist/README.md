# Tugas 3 PBP - Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

Fauziah Putri Fajrianti - 2106707435 - EZ

Kelas PBP A

# Link Heroku: 
https://tugas-2-sissy.herokuapp.com/mywatchlist/html/

https://tugas-2-sissy.herokuapp.com/mywatchlist/xml/

https://tugas-2-sissy.herokuapp.com/mywatchlist/json/ 


# 1. Perbedaan antara JSON, XML, dan HTML!
    
- JSON adalah singkatan dari JavaScript Object Notation, sehingga diturunkan dari JavaScript. JSON menggunakan teks yang dapat dibaca untuk menyimpan dan mengirimkan data yang terdiri dari array dan attribute pair values (keys dan valuenya). JSON digunakan untuk menyimpan informasi secara terorganisir dan mudah diakses.

- XML adalah Extensive Markup Language dan dibuat untuk membawa data. XML mendefinisikan beberapa set aturan standar dalam encoding file ke dalam format yang readable. XML memiliki dua cara untuk menangani data, yaitu tags dan attributes. XML bersifat dinamis dan digunakan untuk mengangkut data, bukan untuk menampilkan data.

- HTML adalah singkatan dari Hypertext Markup Language yang menampilkan data dan mendeskripsikan struktur suatu web page. Digunakan untuk menampilkan data dan bukan untuk mengangkut data, HTML bersifat statis. HTML juga terdiri dari berbagai elemen yang berupa tags beserta kontennya.


# 2. Mengapa kita memerlukan data delivery dalam mengimplementasi sebuah platform
Dalam mengimplementasi sebuah platform yang berhubungan erat dengan data, kita akan perlu melakukan penerusan atau pengiriman data. Melalui data delivery, penerusan atau pengiriman data tersebut dapat diproses menggunakan beberapa format. Umumnya, format-format tersebut meliputi JSON, XML, dan HTML. Ketiga format tersebut merupakan beberapa bahasa yang mudah untuk dipahami sehingga dapat mempermudah programmer dalam mengembangkan suatu platform.


# 3. Cara mengimplementasikan checklist tugas   
1) Membuat suatu aplikasi baru bernama mywatchlist di proyek repositori tugas 2 lalu melalui perintah `python manage.py startapp mywatchlist`

2) Dibuat sebuah model MyWatchList di mywatchlist/models.py dengan attribut watched, title, rating, release_date, dan review. 

3) Menjalankan perintah ` python manage.py makemigrations ` dan ` python manage.py migrate ` untuk mempersiapkan dan menerapkan migrasi model.

4) Menambahkan 10 data untuk objek MyWatchList yang sudah dibuat di atas pada mywatchlist/fixtures/initial_mywatchlist_data.json, kemudian menjalankan perintah ` python manage.py loaddata initial_mywatchlist_data.json `

5) Membuat fungsi baru yang menerima parameter request dan mengembalikan HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi HTML, XML, dan JSON (yaitu function show_html, show_xml, dan show_json)

6) Menambahkan kode ` path('mywatchlist/', include('mywatchlist.urls')) ` ke urlspatterns di project_django/urls.py dan menambahkan kode berikut ke urlspatterns di mywatchlist/urls.py:
    ```
    path('html/', show_html, name='show_html'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    ```
    agar pengguna dapat mengakses http://localhost:8000/mywatchlist/html/, http://localhost:8000/mywatchlist/json/, dan http://localhost:8000/mywatchlist/xml/


# Postman
## HTML
![Gambar]('../../postmanhtml.png?raw=true')

## XML
![Gambar]('../../postmanxml.png?raw=true')

## JSON
![Gambar]('../../postmanjson.png?raw=true')
