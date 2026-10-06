# Data_Mahasiswa
Nama: Muhammad Ihsan  

Kelas: A  

NIM:2609116009

## Penjelasan Kode Program

**1. Import dan memuat data**
```python
import json
from prettytable import PrettyTable

with open("nilaiUTS.json", "r", encoding="utf-8") as f:
    data = json.load(f)
```
- `json` dipakai untuk membaca dan menulis file berformat JSON.
- `PrettyTable` adalah library untuk menampilkan data dalam bentuk tabel rapi di terminal.
- `json.load(f)` membaca isi `nilaiUTS.json` dan mengubahnya menjadi list berisi dictionary, lalu disimpan di variabel `data`. Setiap dictionary mewakili satu mahasiswa.

**2. Fungsi `tampilkan_nilai_uts()`**
Membuat objek `PrettyTable`, menentukan nama kolom (Nama, NIM, Mata Kuliah, Nilai UTS), lalu melakukan perulangan `for` pada `data` untuk menambahkan tiap mahasiswa sebagai satu baris. Terakhir tabel dicetak dengan `print(tabel)`.

**3. Fungsi `tambah_nilai_uts(nama, nim, matkul, nilai_uts)`**
Menambahkan satu dictionary baru ke list `data` menggunakan `append()`, lalu mengembalikan pesan "Data telah ditambah". Perlu diingat, fungsi ini baru mengubah data di memori, belum ke file.

**4. Fungsi `simpan_file_nilai_uts()`**
Membuka `nilaiUTS.json` dengan mode `"w"` (tulis), lalu `json.dump(data, f, indent=4)` menulis seluruh isi `data` ke file dengan indentasi 4 spasi agar mudah dibaca. Mengembalikan pesan "Tersimpan ke nilaiUTS.json".

**5. Fungsi `input_nilai()`**
Fungsi validasi input nilai. Di dalam `while True`, program meminta nilai lalu memeriksa:
- `nilai.isdigit()`: apakah input berupa angka bulat. Jika bukan, muncul pesan "Nilai harus berupa angka bulat!".
- Jika angka, diubah ke `int` dan dicek apakah berada di rentang 0-100. Jika ya, nilai dikembalikan dan perulangan berhenti. Jika tidak, muncul pesan "Nilai harus antara 0 sampai 100!" dan diminta ulang.

**6. Menu utama (perulangan `while True`)**
Menampilkan tiga pilihan menu, lalu membaca pilihan pengguna dengan `input()`:
- **Pilihan 1**: memanggil `tampilkan_nilai_uts()`.
- **Pilihan 2**: meminta nama, NIM, mata kuliah, dan nilai (lewat `input_nilai()`), lalu memanggil `tambah_nilai_uts()` dan `simpan_file_nilai_uts()` agar data langsung tersimpan.
- **Pilihan 3**: mencetak pesan keluar dan `break` untuk menghentikan program.
- **Selain itu**: menampilkan "Pilihan tidak valid, coba lagi." dan menu muncul kembali.

## Penjelasan Output

**Tampilan menu.** 

<img width="398" height="106" alt="1menuawal" src="https://github.com/user-attachments/assets/50b62d63-c3cb-4d18-b244-4a2532fc13c5" />

Program menampilkan judul sistem dan tiga pilihan menu, lalu menunggu pengguna mengetik angka 1-3.

**Pilihan 1 (Lihat semua nilai).** 

<img width="526" height="322" alt="2lihatnilai" src="https://github.com/user-attachments/assets/3286ef86-0614-4db2-8d63-aefb5bbfe508" />

Pengguna mengetik `1`, dan program menampilkan tabel berisi 3 mahasiswa awal: Octavia Putri Verene (Bahasa Inggris, 98), Fery Sugiantoro (Agama Islam, 90), dan Muhammad Ihsan (Matematika Diskrit, 84). Setelah itu menu muncul lagi karena program berada dalam perulangan.

**Pilihan 2 (Tambah nilai baru).** 

<img width="402" height="327" alt="3tambahnilai" src="https://github.com/user-attachments/assets/990d4ee1-19cc-47f7-8fbd-cb8d7c7fd58f" />

Pengguna mengisi Nama: Fery Sugiantoro, NIM: 2609116039, Mata Kuliah: Agama Islam, Nilai: 92. Program menampilkan "Data telah ditambah" (dari `tambah_nilai_uts`) dan "Tersimpan ke nilaiUTS.json" (dari `simpan_file_nilai_uts`), lalu kembali ke menu.

**Isi `nilaiUTS.json` sebelum penambahan.** 

<img width="400" height="401" alt="sebelum3" src="https://github.com/user-attachments/assets/5c038d45-b8c7-4423-8a19-29843eb8085e" />

Berisi 3 data mahasiswa awal dalam format JSON.

**Isi `nilaiUTS.json` setelah penambahan.** 

<img width="477" height="652" alt="sesudah3" src="https://github.com/user-attachments/assets/d523d1e0-ffb1-41ad-97e0-cdba71407fc3" />

Sekarang ada 4 data. Data keempat adalah entri baru milik Fery Sugiantoro dengan nilai 92, yang ditambahkan di akhir list. Ini membuktikan bahwa fungsi simpan berhasil memperbarui file.

**Pilihan 3 (Keluar).** 

<img width="522" height="146" alt="4logout" src="https://github.com/user-attachments/assets/f4de5d2b-aad8-447c-9ecb-ebebdea7aa70" />

Program mencetak "Anda telah keluar dari Catatan Nilai UTS." dan berhenti, sehingga kembali ke prompt terminal.
