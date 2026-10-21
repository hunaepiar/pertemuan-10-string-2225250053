Pertemuan 10 — String dan Pengolahan Teks Python

Identitas Mahasiswa

- Nama: Khunaepi
- NIM: 2225250053
- Kelas: 3B
- Mata Kuliah: Algoritma dan Pemrograman

1. Tujuan Praktikum

Praktikum ini bertujuan untuk memahami penggunaan string dalam Python, yaitu:

1. Mengenal dasar-dasar string dan panjang teks.
2. Memahami indeks dan slicing pada string.
3. Menggunakan method string seperti "upper()", "lower()", "title()", dan "strip()".
4. Membersihkan teks dari spasi berlebih.
5. Memisahkan dan menggabungkan kata menggunakan "split()" dan "join()".
6. Melakukan pencarian kata menggunakan "in", "count()", dan "find()".
7. Membuat program normalisasi data mahasiswa.

2. Struktur Folder

pertemuan-10-string-2225250053/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_dasar_string.py
│   ├── 02_indeks_slicing.py
│   ├── 03_method_string.py
│   ├── 04_bersihkan_teks.py
│   ├── 05_split_join.py
│   └── 06_pencarian_kata.py
├── tugas/
│   └── normalisasi_data_mahasiswa.py
├── kuis/
│   └── kuis_pertemuan_10.py
└── exit_ticket/
    └── exit_ticket_pertemuan_10.md

3. Cara Menjalankan Program

Program dijalankan melalui terminal VS Code menggunakan Python versi 3.12 dengan perintah "uv run --python 3.12".

Latihan 1 — Dasar String

uv run --python 3.12 latihan/01_dasar_string.py

Latihan 2 — Indeks dan Slicing

uv run --python 3.12 latihan/02_indeks_slicing.py

Latihan 3 — Method String

uv run --python 3.12 latihan/03_method_string.py

Latihan 4 — Membersihkan Teks

uv run --python 3.12 latihan/04_bersihkan_teks.py

Latihan 5 — Split dan Join

uv run --python 3.12 latihan/05_split_join.py

Latihan 6 — Pencarian Kata

uv run --python 3.12 latihan/06_pencarian_kata.py

Tugas — Normalisasi Data Mahasiswa

uv run --python 3.12 tugas/normalisasi_data_mahasiswa.py

Kuis Pertemuan 10

uv run --python 3.12 kuis/kuis_pertemuan_10.py

4. Algoritma Tugas

Langkah-langkah program normalisasi data mahasiswa:

1. Memasukkan nama mahasiswa dan kode kelas.
2. Menghapus spasi berlebih pada nama menggunakan "strip()" dan "split()".
3. Merapikan penulisan nama menggunakan "title()".
4. Mengubah kode kelas menjadi huruf kapital menggunakan "upper()".
5. Mengganti spasi pada kode kelas dengan tanda hubung menggunakan "join()".
6. Menghitung jumlah kata pada nama mahasiswa.
7. Mengambil huruf pertama setiap kata untuk membentuk inisial.
8. Menampilkan nama bersih, kode kelas, jumlah kata, dan inisial.

5. Hasil Pengujian

Pengujian dilakukan menggunakan empat variasi nama mahasiswa dan kode kelas.

No.| Nama Input| Kode Kelas Input| Hasil Nama| Hasil Kode| Jumlah Kata| Inisial
1| fATHIYYAH mUTHMAINAH| kelas b| Fathiyyah Muthmainah| KELAS-B| 2| FM
2| khunaepi| pmat a 2026| Khunaepi| PMAT-A-2026| 1| K
3| alex| pmat b 2026| Alex| PMAT-B-2026| 1| A
4| BUDI| pmtk 01| Budi| PMTK-01| 1| B

Berdasarkan pengujian tersebut, program diharapkan dapat merapikan penulisan nama, mengubah kode kelas menjadi huruf kapital dengan pemisah tanda hubung, menghitung jumlah kata, dan menghasilkan inisial nama.

Catatan: Pengujian dinyatakan berhasil apabila hasil keluaran aktual sesuai dengan hasil yang diharapkan.

6. Kuis Formatif Pertemuan 10

1. Apa perbedaan string dan list pada Python?

Jawaban: String menyimpan urutan karakter teks, sedangkan list menyimpan kumpulan elemen yang dapat memiliki berbagai tipe data.

2. Mengapa string disebut immutable?

Jawaban: Karena karakter string tidak dapat diubah secara langsung melalui indeks.

3. Apa hasil dari "'Python'[1:4]"?

Jawaban: "yth", karena slicing mengambil karakter dari indeks 1 sampai sebelum indeks 4.

4. Apa fungsi "strip()"?

Jawaban: Menghapus spasi atau whitespace di awal dan akhir string.

5. Apa perbedaan "lower()" dan "title()"?

Jawaban: "lower()" mengubah teks menjadi huruf kecil, sedangkan "title()" membuat huruf awal setiap kata menjadi kapital.

6. Apa perbedaan "split()" dan "join()"?

Jawaban: "split()" memisahkan string menjadi list, sedangkan "join()" menggabungkan kumpulan string menjadi satu string.

7. Bagaimana cara memeriksa apakah kata "data" terdapat dalam string?

Jawaban: Menggunakan operator "'data' in teks".

8. Apa arti hasil "-1" dari method "find()"?

Jawaban: Artinya substring yang dicari tidak ditemukan.

9. Mengapa normalisasi teks diperlukan sebelum perbandingan data?

Jawaban: Agar perbedaan spasi dan huruf kapital tidak menyebabkan data yang seharusnya sama dianggap berbeda.

10. Perintah apa yang digunakan untuk mengirim commit ke GitHub?

Jawaban: Menggunakan perintah "git push".

File kuis disimpan di "kuis/kuis_pertemuan_10.py" dan dapat dijalankan melalui terminal VS Code.

7. Exit Ticket

Jawaban exit ticket disimpan dalam file "exit_ticket/exit_ticket_pertemuan_10.md".

Hal-hal yang direfleksikan:

1. Operasi string yang paling berguna dan alasannya.
2. Kesalahan yang mungkin terjadi saat mengolah teks dan cara memperbaikinya.
3. Hubungan antara string dan list.
4. Konsep Pertemuan 10 yang berguna untuk mempelajari materi Pertemuan 11.

8. Refleksi

Melalui praktikum ini, saya mempelajari bahwa string dapat digunakan untuk mengolah dan membersihkan data teks. Method seperti "strip()", "title()", "split()", dan "join()" membantu menghasilkan data yang lebih rapi. Saya juga memahami cara mencari kata serta membuat program sederhana untuk menormalisasi data mahasiswa.

9. Kesimpulan

String merupakan tipe data penting dalam Python untuk mengolah teks. Dengan memahami indeks, slicing, method string, dan pencarian kata, pengolahan teks dapat dilakukan secara lebih terstruktur. Praktikum ini juga melatih penerapan konsep string dalam program normalisasi data mahasiswa.

10. Pengelolaan Proyek dengan Git dan GitHub

Git digunakan untuk mencatat perubahan program, sedangkan GitHub digunakan untuk menyimpan repositori secara daring.

Perintah dasar yang digunakan:

git status
git add .
git commit -m "feat: menyelesaikan praktikum string"
git push

Untuk melihat riwayat commit:

git log --oneline --decorate -5

11. Sumber

Bahan Ajar Pertemuan 10 — String dan Pengolahan Teks Python, mata kuliah Algoritma dan Pemrograman.