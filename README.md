# 🧪 SauceDemo Automation Testing UI (Selenium & Python)

[![Python Version](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-green?logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Automated Tests](https://img.shields.io/badge/Tests-40%20Passed-brightgreen)](#)

Repositori ini berisi proyek uji otomatis (*automated UI testing*) berbasis objek untuk platform e-commerce **Swag Labs (SauceDemo)**. Pengujian ini menggunakan pustaka Selenium WebDriver berbasis Python guna memvalidasi fungsionalitas antarmuka aplikasi secara *end-to-end*.

---

## 🚀 Cakupan Skenario Pengujian
Proyek ini menguji **40 skenario komprehensif** yang terbagi rata ke dalam dua kelompok utama:

### A. Skenario Positif (20 Kasus)
* **Autentikasi Multi-Akun:** Validasi login sukses menggunakan berbagai profil bawaan (`standard_user`, `problem_user`, `performance_glitch_user`, `error_user`, `visual_user`).
* **Manajemen Katalog:** Penambahan produk tunggal/multi-item ke keranjang, penghapusan item langsung dari halaman utama, serta fitur pengurutan (*sorting*) produk berdasarkan alfabet maupun harga.
* **Alur Transaksi:** Validasi navigasi detail produk (via judul & gambar), pemeriksaan isi keranjang, pengisian formulir data pengiriman, hingga penyelesaian proses checkout.

### B. Skenario Negatif & Keamanan (20 Kasus)
* **Gagal Login:** Penanganan error akibat kombinasi salah kata sandi, nama pengguna tidak terdaftar, kolom kosong, hingga akun terblokir (`locked_out_user`).
* **Proteksi URL (Security Bypass):** Memastikan halaman internal aplikasi (`inventory.html`, `cart.html`, `checkout-step-one.html`) memblokir akses langsung via tautan URL jika pengguna belum divalidasi oleh sesi login.
* **Validasi Formulir:** Memastikan sistem menolak proses transaksi jika terdapat kolom data kosong (*first name*, *last name*, atau *postal code*) saat checkout.
* **Pembatalan Alur (Cancel Flow):** Memastikan fungsionalitas tombol batal (*cancel*) mengembalikan pengguna ke halaman yang tepat secara aman.

---

## 🛠️ Spesifikasi Teknologi
* **Bahasa Pemrograman:** Python 3.x
* **Framework Pengujian:** `unittest` (Pustaka bawaan Python)
* **Alat Otomasi:** Selenium WebDriver
* **Driver Manager:** `webdriver-manager` (Sinkronisasi otomatis ChromeDriver)

---

## ⚙️ Cara Instalasi & Menjalankan Pengujian

### 1. Klon Repositori
```bash
git clone [https://github.com/Bearnut2/saucedemo-selenium-automation.git](https://github.com/Bearnut2/saucedemo-selenium-automation.git)
cd saucedemo-selenium-automation
