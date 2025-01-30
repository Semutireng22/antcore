![image](https://github.com/user-attachments/assets/d378b526-cc0f-4ec8-b94f-cbf1e3a39fbe)

# AntCore Testnet Daily

![GitHub License](https://img.shields.io/github/license/Semutireng22/antcore)  
![GitHub Last Commit](https://img.shields.io/github/last-commit/Semutireng22/antcore)

---

## Persyaratan
1. **Daftar di AntCore Testnet**:  
   Pastikan Anda sudah terdaftar di AntCore Testnet. Jika belum, daftar dulu di [https://portal.antcore.xyz/?ref_id=4686](https://portal.antcore.xyz/?ref_id=4686).

2. **Python 3**:  
   Pastikan Python 3 sudah terinstal di sistem kalian. Saaya lebih merekomendasikan penggunaan Ubuntu/VPS.

---

## Instalasi dan Penggunaan

### 1. Clone Repositori
Clone repositori ini menggunakan perintah berikut:
```bash
git clone https://github.com/Semutireng22/antcore/
cd antcore
```

### 2. Instal Dependensi
Instal semua dependensi yang diperlukan menggunakan pip:
```bash
pip install -r requirements.txt
```

### 3. Konfigurasi Alamat Wallet
Edit file `address.txt` dan isi dengan alamat wallet yang akan digunakan untuk mengikuti testnet.  
- **Format**: Satu baris untuk satu alamat.
- Contoh:
  ```
  0x6f3eb0241c9da65daa878808d1b86b98..............
  0x6f3eb0241c9da65daa878808d1b86b98..............
  ```

### 4. Jalankan Program
Jalankan program menggunakan perintah berikut:
```bash
python3 main.py
```

#### Menjalankan di Background (Opsional)
Jika Anda ingin menjalankan program di background, gunakan `screen`:
```bash
# Buat session screen baru
screen -S antcore

# Jalankan program
python3 main.py

# Detach dari screen (tekan Ctrl+A lalu D)
```

Untuk melanjutkan session screen:
```bash
screen -r antcore
```

---

## Catatan Penting
- Pastikan alamat wallet yang dimasukkan di `address.txt` valid dan aktif di testnet.
