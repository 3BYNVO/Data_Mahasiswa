import json
from prettytable import PrettyTable

with open("nilaiUTS.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def tampilkan_nilai_uts():
    print("\n=== DAFTAR NILAI UTS MAHASISWA UNMUL ===")
    tabel = PrettyTable()
    tabel.field_names = ["Nama", "NIM", "Mata Kuliah", "Nilai UTS"]
    for mhs in data:
        tabel.add_row([mhs["nama"], mhs["nim"], mhs["matkul"], mhs["nilai_uts"]])
    print(tabel)

def tambah_nilai_uts(nama, nim, matkul, nilai_uts):
    data.append({
        "nama": nama,
        "nim": nim,
        "matkul": matkul,
        "nilai_uts": nilai_uts
    })
    return "Data telah ditambah"

def simpan_file_nilai_uts():
    with open("nilaiUTS.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    return "Tersimpan ke nilaiUTS.json"

def input_nilai():
    while True:
        nilai = input("Nilai (0-100): ")
        if nilai.isdigit():
            nilai = int(nilai)
            if nilai >= 0 and nilai <= 100:
                return nilai
            print("Nilai harus antara 0 sampai 100!")
        else:
            print("Nilai harus berupa angka bulat!")

while True:
    print("\n=== SISTEM PENCATATAN NILAI UTS MAHASISWA UNMUL ===")
    print("1. Lihat semua nilai")
    print("2. Tambah nilai baru")
    print("3. Keluar")
    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        tampilkan_nilai_uts()
    elif pilihan == "2":
        nama = input("Nama: ")
        nim = input("NIM: ")
        matkul = input("Mata Kuliah: ")
        nilai = input_nilai()
        print(tambah_nilai_uts(nama, nim, matkul, nilai))
        print(simpan_file_nilai_uts())
    elif pilihan == "3":
        print("Anda telah keluar dari Catatan Nilai UTS.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")