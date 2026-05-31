# 🧪 SauceDemo Automation Testing UI (Selenium & Python)

Tugas ini adalah repositori uji otomatis (*automated UI testing*) berbasis objek untuk platform e-commerce **Swag Labs (SauceDemo)**. Pengujian mencakup **40 skenario komprehensif** yang terbagi menjadi 20 skenario positif (alur sukses) dan 20 skenario negatif (penanganan error/keamanan).

---

## 🚀 Fitur Utama Pengujian
* **Manajemen Autentikasi:** Login sukses dengan multi-user profile (`standard_user`, `problem_user`, dll) serta validasi pesan error login gagal.
* **Fitur Katalog:** Pengujian fitur *sorting* produk (A-Z, Z-A, harga murah-mahal) serta verifikasi fungsionalitas detail produk via gambar/judul.
* **Sistem Keranjang & Checkout:** Validasi kalkulasi item, pembatalan alur belanja (*cancel checkout*), hingga simulasi pengisian form transaksi lengkap.
* **Pengujian Keamanan (Security Bypass):** Memastikan halaman dalam (*inventory*, *cart*, *checkout*) tidak dapat diakses secara langsung via URL tanpa sesi login aktif.

---

## 🛠️ Spesifikasi Teknologi
* **Bahasa Pemrograman:** Python 3.x
* **Framework Testing:** `unittest` (Bawaan Python)
* **Alat Otomasi:** Selenium WebDriver
* **Driver Manager:** `webdriver-manager` (Otomatisasi unduhan ChromeDriver)

---

## ⚙️ Cara Instalasi & Menjalankan Driver

### 1. Klon Repositori
```bash
git clone [https://github.com/USERNAME_ANDA/NAMA_REPOSITORI.git](https://github.com/USERNAME_ANDA/NAMA_REPOSITORI.git)
cd NAMA_REPOSITORI