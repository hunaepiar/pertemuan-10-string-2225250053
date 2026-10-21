kuis = [
    (
        "Apa perbedaan string dan list pada Python?",
        "String menyimpan urutan karakter teks, sedangkan list "
        "menyimpan kumpulan elemen yang dapat memiliki berbagai tipe data."
    ),
    (
        "Mengapa string disebut immutable?",
        "Karena karakter string tidak dapat diubah langsung melalui indeks."
    ),
    (
        "Apa hasil dari 'Python'[1:4]?",
        "yth"
    ),
    (
        "Apa fungsi strip()?",
        "Menghapus spasi atau whitespace di awal dan akhir string."
    ),
    (
        "Kapan lower() lebih tepat daripada title()?",
        "Saat seluruh teks perlu diubah menjadi huruf kecil."
    ),
    (
        "Apa perbedaan split() dan join()?",
        "split() memecah string menjadi list, sedangkan join() "
        "menggabungkan kumpulan string menjadi satu string."
    ),
    (
        "Bagaimana memeriksa apakah kata 'data' terdapat dalam string?",
        "Gunakan operator: 'data' in teks."
    ),
    (
        "Apa arti hasil -1 dari find()?",
        "Substring yang dicari tidak ditemukan."
    ),
    (
        "Mengapa normalisasi teks diperlukan sebelum perbandingan?",
        "Agar perbedaan spasi dan kapitalisasi tidak menyebabkan "
        "data yang seharusnya sama dianggap berbeda."
    ),
    (
        "Perintah apa yang digunakan untuk mengirim commit ke GitHub?",
        "git push"
    ),
]

print("=== KUIS FORMATIF PERTEMUAN 10 ===")

for nomor, (pertanyaan, jawaban) in enumerate(kuis, start=1):
    print(f"\n{nomor}. {pertanyaan}")
    print(f"   Jawaban: {jawaban}")