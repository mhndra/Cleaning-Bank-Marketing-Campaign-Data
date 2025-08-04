# Cleaning Bank Marketing Campaign Data

## 🏦 Latar Belakang

Pinjaman pribadi adalah salah satu sumber pendapatan yang menguntungkan bagi bank. Rata-rata suku bunga untuk pinjaman dua tahun di Inggris adalah sekitar **10%**. Meskipun angka ini tampak kecil, pada bulan September 2022 saja, konsumen di Inggris meminjam [sekitar £1,5 miliar](https://www.ukfinance.org.uk/system/files/2022-12/Household%20Finance%20Review%202022%20Q3-%20Final.pdf), yang artinya bank dapat menghasilkan sekitar **£300 juta** dari bunga dalam dua tahun.

Sebagai bagian dari strategi pemasaran, sebuah bank telah mengumpulkan data dari kampanye promosi pinjaman pribadi. Mereka berencana untuk mengadakan kampanye serupa di masa depan, sehingga mereka meminta bantuan untuk:

1. Membagi satu file CSV menjadi tiga file CSV dengan struktur dan tipe data yang konsisten.
2. Membersihkan dan memformat penulisan data yang memiliki standar.

Mereka telah memberikan file CSV bernama `"bank_marketing.csv"` yang harus diproses.

---

## 🎯 Tujuan

✅ Memisahkan data menjadi tiga tabel relasional.  
✅ Mengubah tipe data sesuai spesifikasi kolom.  
✅ Membersihkan data dari inkonsisten dan nilai tidak valid.  
✅ Menyimpan hasil akhir masing-masing tabel dalam format CSV.

---

## 🧱 Struktur Output

Data dipisahkan menjadi **tiga file** berdasarkan kategori:

- ['client.csv'](#-file-1-clientcsv) ➡️ Data pribadi dan status klien
- ['campaign.csv'](#-file-2-campaigncsv) ➡️ Interaksi klien dengan kampanye
- ['economics.csv'](#-file-3-economicscsv) ➡️ Referensi kondisi ekonomi klien

---

## 📁 File 1: `client.csv`

Berisi informasi pribadi klien yang menjadi target kampanye.

<details>
<summary><strong>Lihat struktur tabel</strong></summary>

| Kolom             | Tipe Data  | Deskripsi                           | Pembersihan Data                                     |
|-------------------|------------|-------------------------------------|------------------------------------------------------|
| `client_id`       | integer    | ID unik klien                       | Tidak perlu diubah                                   |
| `age`             | integer    | Umur klien (tahun)                  | Tidak perlu diubah                                   |
| `job`             | object     | Jenis pekerjaan                     | Ganti `.` dengan `_`                                 |
| `marital`         | object     | Status pernikahan                   | Tidak perlu diubah                                   |
| `education`       | object     | Tingkat pendidikan                  | Ganti `.` dengan `_`, `"unknown"` dengan `NaN`       |
| `credit_default`  | boolean    | Apakah klien memiliki kredit macet  | Ubah jadi boolean: `1` jika `"yes"`, selain itu `0`  |
| `mortgage`        | boolean    | Apakah klien memiliki kredit rumah  | Ubah jadi boolean: `1` jika `"yes"`, selain itu `0`  |

</details>

---

## 📁 File 2: `campaign.csv`

Mencatat informasi aktivitas kampanye terkait interaksi kampanye pemasaran dengan klien.

<details>
<summary><strong>Lihat struktur tabel</strong></summary>

| Kolom                         | Tipe Data  | Deskripsi                                 | Pembersihan Data                                         |
|-------------------------------|------------|-------------------------------------------|----------------------------------------------------------|
| `client_id`                   | integer    | ID klien                                  | Tidak perlu diubah                                       |
| `number_contacts`             | integer    | Jumlah kontak selama kampanye             | Tidak perlu diubah                                       |
| `contact_duration`            | integer    | Durasi kontak terakhir (detik)            | Tidak perlu diubah                                       |
| `previous_campaign_contacts`  | integer    | Jumlah kontak di kampanye sebelumnya      | Tidak perlu diubah                                       |
| `previous_outcome`            | boolean    | Hasil kampanye sebelumnya                 | Ubah jadi boolean: `1` jika `"success"`, selain itu `0`  |
| `campaign_outcome`            | boolean    | Hasil kampanye saat ini                   | Ubah jadi boolean: `1` jika `"yes"`, selain itu `0`      |
| `last_contact_date`           | datetime   | Tanggal kontak terakhir (`"YYYY-MM-DD"`)  | Gabung `day`, `month`, dan tahun tetap `2022`            |

</details>

---

## 📁 File 3: `economics.csv`

Berisi informasi tentang referensi kondisi perekonomian klien saat kampanye berlangsung.

<details>
<summary><strong>Lihat struktur tabel</strong></summary>

| Kolom                   | Tipe Data  | Deskripsi                            | Pembersihan Data    |
|-------------------------|------------|--------------------------------------|---------------------|
| `client_id`             | integer    | ID klien                             | Tidak perlu diubah  |
| `cons_price_idx`        | float      | Indeks harga konsumen (bulanan)      | Tidak perlu diubah  |
| `euribor_three_months`  | float      | Suku bunga Euribor 3 bulan (harian)  | Tidak perlu diubah  |

</details>

---

## ⚙️ Teknologi

- Integrated Development Environment (IDE) ➡️ Visual Studio Code
- Distributed Version Control System ➡️ Git 
- Bahasa Pemrograman ➡️ Python 
- Python Library ➡️ ipykernel, pandas, numpy)
- Operating System ➡️ Linux

---

## 📂 Struktur Direktori

```
🗃️ Cleaning-Bank-Marketing-Campaign-Data/
├── bank_marketing.csv  # File mentah
├── campaign.csv        # Output data kampanye
├── cleaning_script.py  # Python script - membersihkan data
├── client.csv          # Output data klien
├── economics.csv       # Output data ekonomi
├── README.md           # Deskripsi proyek ini
└── requirements.txt    # Python library dibutuhkan
```

---

## 📌 Insight & Pembelajaran

- Memahami pentingnya **data integrity** dalam struktur data relasional dan tipe data yang sesuai spesifikasi kolom.
- Mengasah kemampuan dalam **data cleaning** yang realistis dan praktikal.
- Memastikan **data quality** melalui pengelolaan data yang tidak konsisten dan mengandung nilai tidak sesuai format penulisan data.
- Merancang dan membuat pipeline konversi data siap pakai yang berulang (**scalable**).

