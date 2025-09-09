# Yatzuu-Shop
Link: [https://yahya-muhandar-footballshop.pbp.cs.ui.ac.id](https://yahya-muhandar-footballshop.pbp.cs.ui.ac.id)

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
step by step yang saya lakukan adalah seagai berikut:
1. membuat repo baru digithub dengan readMe
2. clone repo dari github ke vscode
3. membuat env dan mengaktifkanya
4. membuat file requirements.txt yang berisi dependencies
5. menginstal dependescies yang ada di requirements.txt dengan menjalankan comand
    ```bash
   pip install -r requirements.txt
   ```
6. membuat proyek django dengan nama football_shop
   ```bash
   django-admin startproject football_shop
   ```
7. mengkonfigurasi variabel environment dengan membuat file .env dan .env.prod
8. membuat aplikasi main didalam proyek menggunakan comand
   ```bash
   python manage.py startapp main
   ```
9. mendaftarkan aplikasi main kedalam variable INSTALLED_APPS pada file settings.py
10. membuat template yang berisikan main.html
10. Melengkapi logic pada file
   - models.py
   - views.py
   - urls.py
11. karena ada perubahan pada models.py maka saya jalankan
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
