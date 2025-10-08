# Yatzuu-Shop
Link: [https://yahya-muhandar-yatzuushop.pbp.cs.ui.ac.id](https://yahya-muhandar-yatzuushop.pbp.cs.ui.ac.id)

# tugas 5
### 1. Apa perbedaan antara synchronous request dan asynchronous request?
- Synchronous request berarti ketika browser mengirim permintaan ke server, halaman akan menunggu sampai server memberikan respons.Selama proses itu, pengguna tidak bisa berinteraksi dengan halaman — biasanya halaman akan reload sepenuhnya.

- Asynchronous request (AJAX) berarti browser bisa mengirim dan menerima data dari server tanpa me-reload halaman.
Prosesnya berjalan di latar belakang, sehingga pengguna tetap bisa berinteraksi dengan halaman sementara data dikirim atau diterima.
---
### 2. Bagaimana AJAX bekerja di Django (alur request–response)?
1. Pengguna melakukan aksi di halaman (misalnya klik tombol “Tambah Produk”).
2. JavaScript menjalankan fungsi fetch() atau XMLHttpRequest() untuk mengirim data ke URL Django tertentu (biasanya view berbasis JsonResponse).
3. Django menerima request tersebut di views.py, memproses data (misalnya menyimpan ke database), lalu mengembalikan response dalam format JSON.
4. JavaScript di browser menerima data JSON itu, lalu memperbarui tampilan halaman (DOM) tanpa reload.


---
### 3.  Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
- Tidak perlu reload halaman, sehingga terasa lebih cepat dan interaktif.
- Hemat bandwidth, karena hanya data yang dikirim/diterima, bukan seluruh halaman HTML.
- User experience lebih halus, misalnya saat menambah atau menghapus item langsung muncul di layar.
- Memungkinkan fitur real-time, seperti notifikasi atau live update.
---
### 4.  Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
Gunakan CSRF Token di setiap AJAX POST request. Django memiliki middleware csrf_token yang harus dikirim dalam header request (X-CSRFToken).
Validasi input di server-side, jangan hanya di JavaScript.
Gunakan HTTPS agar data (termasuk password) terenkripsi selama pengiriman.
Batasi endpoint hanya untuk method tertentu (POST untuk login/register, bukan GET).

### 5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
- Memberikan pengalaman yang lebih cepat dan responsif, karena tidak perlu memuat ulang seluruh halaman.
- Interaksi terasa lebih mulus dan natural, mirip seperti aplikasi mobile.
- Pengguna bisa melakukan banyak aksi secara langsung (misalnya edit, delete, tambah) tanpa gangguan.
- Namun, jika tidak ditangani dengan baik (misalnya error handling buruk), pengguna bisa bingung karena tidak ada feedback yang jelas.

# tugas 5
### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
urutan css selector adalah sebagai berikut
1. inline css
karena css ini ditetap kan ditag nya itu sendiri jadi hanya tag itu saja yang terpengaruhi
2. id selector
sama dengan inline css dimana hanya 1 tag saja yang terpengaruhi. namun karena css di tetapkan di file berbeda atau menggunakan tag <style></style> selector ini jadi priortoas kedua
3. Class selector
bisa banyak tag dengan dan elemen berbeda beda. asalkan elemen tersebut memiliki class yang sesuai
4. element selector
semua elemen yang di selec akan terpengaruhi oleh dan tidak memandang id maupun class. oleh karena itu selector ini jadi last priority
jadi css akan menerapkan styling dari priority terbawah dan menimpa dengan higher pririty jika ada style yang ditimpa

---
### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
responsive penting karena kita tidak tau user akan menggunakan perangkat apa, sedangkan kita butuh agar user senyaman mungkin menggunakan website yang kita buat. oleh karena itu tampilan yang diberikan untuk setiap device harus dapat menyesuaikan.
contoh responsive:
twitter(web),tokopedia, shopee. jika kita buka websitenya di hp dan di desktop tampilanya akan terlihat berbeda. nampak dari jumlah gridnya, headernya, dll

contoh tidak responsive:
kebanyakan dari website sekarang sudah pasti responsive. namun biasanya yang tidak responsivee adalah website situs pemerintah yang sudah lama belum di update. website tokokecil. jadi jika kita buk di hp website ini tulisanya tidak membesar layoutnya tetap seperti desktop atau sebaliknya


---
### 3.  Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin: adalah space yang diberikan untuk diluar box atau elemen
border: adalah garis tepi yang ada pada elemen berada di antara margin dan padding
padding:adalah space antara elemen itu dengan elemen didalamnya seperti text div lain atau apapun itu.
implementasi
margin= css:margin: 0px atau margin-top/bottom/left/right: 0px tailwind:m-10 mt/b/l/r/x/y-10 
margin= css:`border-width:2px; border-style:solid; border-color:black; `tailwind: `border-2 border-solid border-black`
padding= css:padding: 0px atau padding-top/bottom/left/right: 0px tailwind:p-10 pt/b/l/r/x/y-10 

---
### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
flexbox: berfungsi untuk mengatur 1 dimensi saja. elemen yang berada didalam flexbox akan bisa di atur posisinya dengan flexible seperti ditengah elemen di kanan atas atau bawah kiri.

kegunaan: flexbox biasanya digunakan untuk membuat navbar menyusun elemen yang ada di dalam sebuah div atau elemen apapun. seperti pada `card_product.html` 

grid: grid berfungsi seperti 2 dimensi. mengatur 1 dimensi, berarti dimensi yang ke 2 nya mengikuti. grid digunakan untuk menetapkan sebuah div berapa coloumn atau row yang bisa ditampung. jika ditetapkan 3 buah row maka untuk column nya bisa sebanyak mungkin dan sebaliknya.

kegunaan: biasanya digunakan ketika membuat sebuah layout yang banyak seperti vidio vidio yang ada di youtube atau digunakan pada project footballnews dibagian menunjukan berbagai news

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
1. tambahkan tailwind ke project dengan menambahkan `<script src="https://cdn.tailwindcss.com"> </script>` ke base.html
2. menambahkan function `edit_product` dan `delete_product`
3. membuat file `edit_product.html` sekalian dengan tailwind classnya
4. menghubungkan function editnews dan delete news ke html melalui `urls.py`
5. membuat file `navbar.html` didalam  folder templates disebelah `base.html` dengan tailwind classnya
6. membuat folder static di main root. setelah itu diisi dengan folder css dan image
7. menambahkan file global.css di folder `/static/css`
8. menambahkan pada `setting.py` logic agar folder static atau file yang ada di folder static dapat di detect di app
9. styling html yang lain menggunakan tailwind. terlebih di bagian main, card_product dan product_detail



# tugas 4
### 1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
AuthenticationForm di Django adalah form bawaan untuk login yang memvalidasi username dan password. Kelebihannya mudah digunakan, sudah terhubung dengan sistem autentikasi Django, dan bisa dikustomisasi, sedangkan kekurangannya kurang fleksibel untuk metode login khusus dan tidak menyediakan pembatasan percobaan login.

---
### 2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi adalah proses memverifikasi identitas pengguna, sedangkan otorisasi menentukan hak akses setelah identitas diverifikasi. Django mengelola autentikasi dengan authenticate dan login, lalu menerapkan otorisasi lewat permission, group, dan decorator seperti @permission_required.

---
### 3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Cookies menyimpan state di sisi klien, ringan, dan tidak membebani server, tetapi kapasitasnya kecil dan rentan dicuri. Session lebih aman karena data disimpan di server, namun menambah beban server dan memerlukan sinkronisasi jika menggunakan banyak server.

---
### 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
cookies tidak otomatis aman ada beberapa risiko nyata seperti pencurian lewat XSS (JavaScript membaca cookie), penyadapan lewat koneksi non-HTTPS, CSRF karena browser mengirim cookie otomatis ke domain yang sesuai, serta risiko replay atau session fixation bila cookie persisten tidak dikelola dengan benar. Jadi penggunaan cookie perlu diperlakukan sebagai permukaan serangan yang harus dilindungi, bukan solusi “aman” tanpa konfigurasi tambahan.

Django membantu mengurangi banyak risiko itu dengan beberapa mekanisme: secara umum session di Django menyimpan data di server dan hanya meletakkan session ID di cookie sehingga data sensitif tidak terekspos ke klien, ada middleware CSRF yang memaksa penggunaan token untuk permintaan berbahaya; tersedia pengaturan cookie keamanan (mis. opsi untuk HttpOnly, Secure, dan SameSite) serta SecurityMiddleware untuk pengaturan seperti HSTS dan redirect ke HTTPS. Namun beberapa cookie (mis. cookie CSRF untuk akses AJAX) sengaja tidak dibuat HttpOnly, sehingga masih perlu perhatian developer.

---
### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. import beberapa library di `views.py` seperti UserCreationForm, messages, AuthenticationForm, authenticate, login, logout, login_required, HttpResponseRedirect, reverse, datetime 
2. tambahkan method method di `views.py` seperti register, logout_user, login_user, form.is_valid, 
3. tambahkan @login_required pada showmain dan showproduct di `views.py`
4. import User di models.py
5. tambahkan di dalam class product di models.py
   ```bash 
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   ```
6. lakukan migrate untuk models
7. git push ke github dan pws

---

- show xml
![alt text](<Screenshot 2025-09-17 103421.png>)
- show json
![alt text](<Screenshot 2025-09-17 103436.png>)
- show xml by id
![alt text](<Screenshot 2025-09-17 103457.png>)
-show json by id
![alt text](<Screenshot 2025-09-17 103504.png>)








# tugas 3
### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery diperlukan agar data bisa dikirim dan diterima dengan format yang konsisten antara client, server, dan layanan lain. Ini memungkinkan interaksi pengguna yang dinamis, pemisahan logika dan tampilan, integrasi antar sistem, menjaga keamanan, serta memudahkan pengembangan dan skalabilitas platform.

---
### 2.Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, JSON lebih mudah dibaca karena strukturnya mirip objek, tidak seperti XML yang terlihat seperti HTML. Sementara itu, JSON lebih populer dibandingkan XML karena formatnya lebih ringkas, mudah dibaca, cepat diproses oleh JavaScript tanpa parsing tambahan, dan lebih efisien untuk pertukaran data, sedangkan XML biasanya hanya dipakai untuk sistem lama atau kebutuhan struktur dokumen yang lebih kompleks.

---
### 3.Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form Django berfungsi untuk memeriksa apakah data yang dikirim melalui form sudah lengkap dan sesuai format yang ditentukan; jika valid akan mengembalikan True dan menyimpan data bersih di cleaned_data, sedangkan jika tidak valid akan mengembalikan False serta menyimpan pesan error. Kita memerlukan method ini untuk memastikan keamanan, menjaga kualitas data yang masuk ke database, memberikan umpan balik kesalahan kepada pengguna, dan memudahkan pengembang karena Django sudah menyediakan mekanisme validasi otomatis.

---
### 4.Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Kita membutuhkan {% csrf_token %} untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF), yaitu serangan yang memanfaatkan sesi login pengguna untuk melakukan aksi tanpa sepengetahuan mereka. Token ini memastikan setiap permintaan POST benar-benar berasal dari form sah di situs kita, bukan dari situs berbahaya.

Jika kita tidak menambahkan csrf_token, Django secara default akan menolak permintaan POST tersebut dan menampilkan error 403 Forbidden karena menganggap request tidak sah. Namun, jika proteksi CSRF dinonaktifkan atau dilewati, form akan menjadi rentan terhadap serangan.

Penyerang dapat membuat halaman web jahat yang secara diam-diam mengirim permintaan ke server menggunakan cookie sesi pengguna yang masih aktif. Dengan cara ini, mereka bisa memanfaatkan akun korban untuk melakukan aksi berbahaya seperti mengubah data, menghapus akun, atau bahkan melakukan transaksi tanpa izin.

---
### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. buat directori `templates` di directory utama dan tambahkan file `base.html`
2. tambahkan pada `settings.py` di variable TEMPLATES untuk backend, dirs,app_dirs agar `base.html` terdeteksi
3. tambahkan kode ini pada awal dan akhir `main.html` agar menjadi menandakan itu akan digunakan di `base.html`
   ```bash
      {% extends 'base.html' %}
      {% block content %}

      {% endblock content %}
   ```
4. buat file `forms.py` dan buat class untuk form dan model yang digunakan serta fields yang ada pada model itu
5. tambahkan function create_product dan show_product pada `views.py`
6. tambahkan path pada `urls.py` di variable urlpatterns untuk routing
7. sesuaikan `main.html` agar dapat menunjukan product yang sudah di add
8. membuat berkas html `create_product.html` dan `product_detail.html` untuk page yang dibuka ketika user menuju ke salah satu path yang sudah kita tambahkan di `urls.py`
9. menambahkan variable `CSRF_TRUSTED_ORIGINS` pada file settings.py agar dapat melakukan POST dan untuk keamanan
10. menambahkan function `show_xml` dan `show_json` dan menambahkan path nya
11. menambahkan function `show_xml_by_id` dan `show_json_by_id` dan menambahkan path nya

---
### 6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Mungkin untuk feedback dari saya, penjelasan tentang csrf_token di Tutorial 2 terasa terlalu singkat, sehingga beberapa mahasiswa mungkin tidak sepenuhnya memahami fungsinya atau alasan penggunaannya. Akan lebih baik jika disertakan penjelasan lebih mendalam atau contoh kasus nyata agar mahasiswa lebih paham konteks dan pentingnya csrf_token.

---
### 7. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
- show xml
![alt text](<Screenshot 2025-09-17 103421.png>)
- show json
![alt text](<Screenshot 2025-09-17 103436.png>)
- show xml by id
![alt text](<Screenshot 2025-09-17 103457.png>)
-show json by id
![alt text](<Screenshot 2025-09-17 103504.png>)


# tugas2
---
### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
step by step yang saya lakukan adalah seagai berikut:
1. membuat repo baru digithub dengan readMe
2. clone repo dari github ke vscode
3. membuat virtual environment dan mengaktifkanya
4. membuat file requirements.txt yang berisi dependencies
5. menginstal dependescies yang ada di requirements.txt dengan menjalankan comand
    ```bash
   pip install -r requirements.txt
   ```
6. mengkonfigurasi variabel environment dengan membuat file .env dan .env.prod
7. Modifikasi file settings.py untuk menggunakan environment variables.
8. membuat file .gitignore agar file sensitif tidak masuk kedalam repository
9. membuat proyek django dengan nama football_shop
   ```bash
   django-admin startproject football_shop
   ```
10. mengkonfigurasi variabel environment dengan membuat file .env dan .env.prod
11. membuat aplikasi main didalam proyek menggunakan comand
   ```bash
   python manage.py startapp main
   ```
12. mendaftarkan aplikasi main kedalam variable INSTALLED_APPS pada file settings.py
13. membuat template yang berisikan main.html
14. Melengkapi logic pada file
   - `models.py`
   - `views.py`
   - `urls.py`
15. karena ada perubahan pada `models.py` maka saya jalankan
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
16. melakukan push ke github dengan git add, commit, push
17. membuat project baru di PWS dan menyamakan environs PWS dengan yang ada di .env.prod
---
### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

<img width="725" height="525" alt="image" src="https://github.com/user-attachments/assets/f1514745-82a5-4bda-b1ab-b70c0317fabb" />

sumber: Forum Diskusi Minggu Kedua - "Alur Django" - Course PBP SCELE

- yang pertama client melakukan request melalui URL tertentu
- lalu URL tersebut di proses oleh `urls.py`. jika cocok maka request di teruskan ke `views.py`
- `views.py` memproses request dari  url dan melakukan logic dan mengambil data dari `models.py`
- setelah `view.py` selesai memproses data, `views.py` akan merender HTML yang sesuai dari folder `templates`
- terakhir browser mendapatkan response HTML yang dilihat oleh client
---
### Jelaskan peran settings.py dalam proyek Django!
settings.py berfungsi sebagai pusat konfigurasi proyek Django. File ini mengatur berbagai hal penting seperti:

- Environment: memuat variabel dari .env agar konfigurasi bisa dibedakan antara development dan production.

- Database: menentukan koneksi (SQLite untuk dev, PostgreSQL untuk production).

- Keamanan: mengatur ALLOWED_HOSTS agar hanya domain tertentu yang bisa mengakses.

- Static files: mengatur lokasi file statis (CSS, JS, gambar) untuk pengembangan maupun deployment
---
### Bagaimana cara kerja migrasi database di Django?
migrasi data base dilakukan ketika kita melakukan perubahan pada `models.py`. fungsinya adalah untuk melacak perubahan
- ```bash
   python manage.py makemigrations
   ```
   djanggo akan membaca perubahan dan membuat file migrasi di folder migrations/
-  ```bash
   python manage.py migrate
   ```
   django mengeksekusi file migrasi tersebut agar database mengikuti struktur baru

### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django dijadikan permulaan pembelajaran karena framework ini lengkap, terstruktur, dan “batteries-included”. Django sudah menyediakan fitur penting seperti manajemen database (ORM), autentikasi, sistem template, hingga keamanan dasar tanpa harus memasang banyak library tambahan. Dengan pola Model–View–Template (MVT) yang jelas, pemula dapat memahami alur kerja aplikasi web modern secara runtut. Selain itu, dokumentasi Django sangat lengkap sehingga memudahkan mahasiswa atau pengembang baru untuk belajar praktik terbaik pengembangan perangkat lunak dari awal.

### Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

menurut saya tutorial yang diberikan pada tutorial 1 sudah lengkap dengan penjelasan yang ada di setia codenya tetapi agak sulit untuk memahami apa yang sedang terjadi lebih dalam. saya hanya memahami apa yang suatu kode lakukan, jadi saya tetap harus mencari lebih dalam tentang programnya.