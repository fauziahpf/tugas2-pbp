# Tugas 5 PBP: Web Design Using HTML, CSS, and CSS Framework

Fauziah Putri Fajrianti - 2106707435 - EZ

Kelas PBP A
<br></br>

# Link Heroku: 
Tekan [link ini](ttps://tugas-2-sissy.herokuapp.com/todolist/) untuk menuju ke aplikasi To-Do List dalam Heroku. <br> </br>


# 1.  Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
__Perbedaan__
- __Inline CSS__: bentuk CSS yang ditempatkan ke tag HTML sebagai suatu attribute, digunakan untuk memberi style tertentu khusus pada bagian tag HTML tersebut. Contoh `<p style="font-size: 14px"> Ye </p>` akan memberi style ukuran font 14px ke elemen paragraph berisi Y tersebut.
- __Internal CSS__: bentuk CSS yang dikhususkan untuk dokumen tertentu, ditempatkan dalam tag HTML `<head>` dan didefinisikan dalam tag `<style>`. Contoh:
    ```
    <head> 
        <style>
            body {
                background-color: blue;
            }
        </style>
    </head>
    <!-- -> akan memberi warna latar belakang biru pada khusus halaman HTML itu pada bagian body. -->
    ```

- __External CSS__: bentuk CSS yang didefinisikan pada file CSS external yang diimport ke file HTML yang membutuhkannya. 
---
__Inline CSS__
- __Kelebihan Inline CSS:__ dapat memberi styling tersendiri untuk elemen tag tertentu agar beda dari elemen lain dengan tag yang sama 
- __Kekurangan Inline CSS:__ sulit untuk dibaca jika banyak style yang diterapkan serta cukup boros apabila ingin memberi style sama pada elemen-elemen berbeda  

__Internal CSS__
- __Kelebihan Internal CSS:__ efisien untuk memberi styling pada hanya suatu dokumen HTML tertentu dan tidak perlu mengimport file lain
- __Kekurangan Internal CSS:__ cukup *time-consuming* jika untuk memberi styling pada banyak dokumen HTML karena harus ditambahkan ke masing-masing dokumen serta menambah ukuran dokumen  

__External CSS__
- __Kelebihan External CSS:__ efisien untuk memberi styling yang seragam pada banyak dokumen HTML
- __Kekurangan External CSS:__ harus melakukan import terlebih dahulu ke setiap dokumen HTML yang membutuhkan styling CSS tersebut
<br/><br/>

# 2. Jelaskan tag HTML5 yang kamu ketahui.
- `<a>     `: tag untuk mendefinisikan suatu hyperlink
- `<header>`: tag yang merepresentasikan header dari laman atau dokumen HTML
- `<div>   `: tag untuk mendefinisikan section atau bagian spesifik dalam dokumen
- `<footer>`: tag yang meprepresentasikan header dari laman atau dokumen HTML
- `<p>     `: tag yang mendefinisikan suatu paragraf

<br/><br/>

# 3.  Jelaskan tipe-tipe CSS selector yang kamu ketahui.
1. __Element Selector__ : selector untuk menambahkan styling pada elemen tag tertentu. Misal untuk tag `<h1>` didefinisikan dengan cara: 
    ```
    h1 {
        ...
    }
    ```
2. __ID Selector__ : selector untuk menambah styling pada elemen tertentu menggunakan ID. Misal untuk ID `<an-id>` didefinisikan dengan cara: 
    ```
    #an-id {
         ...
    }
    ```
3. __Class Selector__ : selector untuk menambah styling pada elemen dengan class tertentu. Misal untuk class `card` didefinisikan dengan cara: 
    ```
    .card {  
        ...
    }
    ```
<br></br>


# 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Agar dapat menggunakan __CSS framework Bootstrap__ untuk aplikasi todolist ini, ditambahkan barisan kode berikut dalam tag `<head>` di setiap dokumen HTML aplikasi:
    ```
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
    ```
- dan barisan kode berikut dalam tag `<body> `:
    ```
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
    ```
- Membuat file ` static/css/style.css ` untuk keperluan External CSS.
- Kostumisasi halaman __login__ dengan menerapkan class `card` yang berisi elemen-elemen untuk keperluan login, menggunakan class `btn` untuk tombol-tombol yang ada, menambahkan `card-footer`, serta mengkostumisasi warna-warna, posisi elemen, dan styling lainnya menggunakan Bootstrap classes, Inline CSS, Internal CSS, atau External CSS.
- Kostumisasi halaman __register__ dengan menerapkan class `card` yang berisi elemen-elemen untuk keperluan register, menggunakan class `btn` untuk tombol-tombol daftar, serta mengkostumisasi warna-warna, posisi elemen, dan styling lainnya menggunakan Bootstrap classes, Inline CSS, Internal CSS, atau External CSS.
- Kostumisasi halaman __create-task__ dengan menerapkan class `card` yang berisi elemen-elemen untuk keperluan membuat task baru, menggunakan class `btn` untuk tombol-tombol yang ada, membuat navigation bar dengan menerapkan class `navbar`, menambahkan gambar melalui tag `<img>`, membuat card tersebut bisa berbentuk horizontal atau vertical (tergantung pada device yang digunakan), serta mengkostumisasi warna-warna, posisi elemen, dan styling lainnya menggunakan Bootstrap classes, Inline CSS, Internal CSS, atau External CSS.
- Kostumisasi halaman __todolist__ dengan menerapkan class `card` untuk masing-masing task pengguna, menambahkan `card-header` untuk memperlihat status task, membuat navigation bar dengan menerapkan class `navbar`, menggunakan class `btn` untuk tombol-tombol yang ada, serta mengkostumisasi warna-warna, posisi elemen, dan styling lainnya menggunakan Bootstrap classes, Inline CSS, Internal CSS, atau External CSS.
- __(Bonus)__ Menambahkan efek ketika melakukan hover pada cards dengan menambahkan :hover pada class card dalam file External CSS:
    ```
    .card{
        transition: .3s transform cubic-bezier(.155,1.105,.295,1.12),.3s box-shadow,.3s -webkit-transform cubic-bezier(.155,1.105,.295,1.12);
        cursor: pointer;
    }

    .card:hover{
        transform: scale(1.03);
    }
    ```