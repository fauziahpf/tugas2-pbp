# Tugas 6 PBP: Javascript dan AJAX

Fauziah Putri Fajrianti - 2106707435
<br></br>

## Link Heroku: 
Tekan [link ini](https://tugas-2-sissy.herokuapp.com/todolist/) untuk menuju ke aplikasi To-Do List di Heroku. <br> </br>


## 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Melalui synchronus programming, program dijalankan dalam instructions yang berurut, ditentukan oleh instruksinya. Artinya, pemrograman ini digunakan ketika program harus menunggu event tertentu selesai sebelum melanjutkan ke event lain. Contohnya, sebuah program yang perlu menunggu pengguna selesai mengetikkan nama ke dalam kolom teks sebelum mengerjakan task lain. Di sisi lain, asynchronous programming memungkinkan banyak instructions terjadi secara bersamaan. Saat memulai suatu task, program tetap terus berjalan. Ketika task selesai, program diinformasikan dan mendapatkan akses ke hasilnya (misalnya, membaca data dari disk).
Synchronus programming memblokir instructions lain hingga task selesai, sementara operasi dalam asynchronus programming dapat dijalankan tanpa memblokir instructions lain. 
<br></br>

## 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-Driven Programming merupakan paradigma pemrograman yang berdasar pada kemunculan event untuk menentukan aliran kontrol program. Program dengan paradigma ini aplikasi ini dirancang untuk mendeteksi event yang terjadi, menggunakan event-handler yang tepat untuk menanganinya, dan biasanya menggunakan function atau callback methods. Suatu event dapat berbentuk klik tombol, pesan yang dikirimkan, atau tindakan lain apa pun dalam program yang dapat diabstraksikan menjadi "event".
<br></br>
Contoh penerapan event-driven programming pada tugas ini adalah pada penggunaan method AJAX POST untuk menambahkan tasks. Function JavaScript createTask() saya buat untuk menggunakan method POST. Function ini menerima var berupa data task, di mana data tersebut diambil dari submisi form. Form yang dimaksud adalah form yang melalui modal memiliki button submit dengan tag ` onclick="createTask()" `, artinya function createTask() dijalankan ketika button tersebut ditekan.  
<br></br>

## 3. Jelaskan penerapan asynchronous programming pada AJAX.
Dalam penerapan asynchronus programming pada AJAX, web server mengirim dan mengambil data dari server secara asinkron arau dari balik layar. Browser tidak perlu me-refresh halaman setiap kali data dimanipulasi atau diperbarui. AJAX memungkinkan halaman web untuk secara dinamis mengubah isi database tanpa perlu memuat ulang seluruh halaman. AJAX akan mengirim callback sebagai response dari event-driven programming agar data diubah secara asinkronus. Contoh implementasinya adalah AJAX POST dan AJAX GET yang mana akan ditrigger ketika function yang menggunakan method tersebut ditangkap pada event-handler.
<br></br>

## 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1) Membuat view show_json yang mengembalikan data task user dalam bentuk JSON.
2) Membuat routing path /todolist/json yang mengarah ke view tersebut.
3) Membuat JS function yang bernama handleCards() untuk mengambil dan merender cards dari database JSON melalui method GET yang diarahkan ke halaman todolist/json/.
4) Menampilkan halaman utama todolist yang telah merender task cards melalui function (document).ready
5) Membuat view todolist_ajax, kemudian membuat routing path todolist/add/ yang mengarah ke view tersebut.
6) Membuat modal Bootstrap dengan form untuk menambahkan task.
7) Membuat JS function bersama createTask() yang melalui method POST mengambil data input dengan type submit dari form pembuatan task. Data tersebutkan diarahkan ke todolist/add/, memanggil fungsi todolist_ajax yang ada pada views.py, dan menampilkan response secara asinkronus tanpa reload page.