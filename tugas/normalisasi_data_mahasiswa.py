def normalisasi_nama(nama):
    return " ".join(nama.strip().split()).title()


def buat_inisial(nama):
    kata = normalisasi_nama(nama).split()
    return "".join(kata_item[0] for kata_item in kata)


def normalisasi_kode(kode):
    kata = kode.strip().upper().split()
    return "-".join(kata)


nama = input("Nama: ")
kode = input("Kode kelas: ")

nama_bersih = normalisasi_nama(nama)
kode_bersih = normalisasi_kode(kode)
inisial = buat_inisial(nama)
jumlah_kata = len(nama_bersih.split())

print("\n=== HASIL NORMALISASI ===")
print(f"Nama bersih : {nama_bersih}")
print(f"Kode kelas  : {kode_bersih}")
print(f"Jumlah kata : {jumlah_kata}")
print(f"Inisial     : {inisial}")