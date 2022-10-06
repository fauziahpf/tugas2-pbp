# Tugas 5 PBP: Web Design Using HTML, CSS, and CSS Framework

Fauziah Putri Fajrianti - 2106707435 - EZ

Kelas PBP A
<br></br>

# Link Heroku: 
https://tugas-2-sissy.herokuapp.com/todolist/ <br> </br>


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
3. __Class Selector__ :s elector untuk menambah styling pada elemen dengan class tertentu. Misal untuk class `card` didefinisikan dengan cara: 
    ```
    .card {  
        ...
    }
    ```
<br></br>


# 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- 
- 
- 
- 
- 