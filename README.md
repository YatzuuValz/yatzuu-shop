# Yatzuu-Shop
Link: [https://yahya-muhandar-footballshop.pbp.cs.ui.ac.id](https://yahya-muhandar-footballshop.pbp.cs.ui.ac.id)
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