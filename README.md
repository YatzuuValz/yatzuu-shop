# Yatzuu-Shop
Link: [https://yahya-muhandar-yatzuushop.pbp.cs.ui.ac.id](https://yahya-muhandar-yatzuushop.pbp.cs.ui.ac.id)

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