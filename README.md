# CUPANG-QR

*Ensuring Authentic & Transparent Betta Fish Transactions through QR & Blockchain*

*Proyek ini merupakan proyek dummy*
Proyek ini dikembangkan oleh mahasiswa untuk memenuhi tugas pengembangan sistem informasi berbasis teknologi blockchain dan QR code, khususnya pada sektor maritim dan perdagangan ikan hias. 

![Python](https://img.shields.io/badge/python-3.8+-blue)
![Flask](https://img.shields.io/badge/framework-flask-yellow)
![QRCode](https://img.shields.io/badge/library-qrcode-lightgrey)

Built with the tools and technologies.

---

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)

---

## Overview

**CupangQR** adalah aplikasi web yang memanfaatkan blockchain sederhana untuk mencatat transaksi jual beli ikan cupang. Setiap transaksi menghasilkan hash unik yang kemudian dikonversi menjadi QR code. QR ini dapat diverifikasi untuk memastikan keaslian transaksi secara transparan.

Aplikasi ini sangat berguna bagi pelaku usaha ikan hias dalam memastikan setiap proses transaksi tercatat dengan baik dan tidak bisa dimanipulasi.

---

## Getting Started

### Prerequisites

Proyek ini membutuhkan:

- **Bahasa Pemrograman**: Python 3.8 atau lebih baru
- **Framework Web**: Flask
- **Library**: qrcode, Pillow

---

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/username/CupangQR.git
```
2. **Masuk ke direktori proyek:**

```bash
cd CupangQR
```

3. **Install depedencies:**

```bash
pip install -r requirements.txt
```
**OR**

```bash
pip install flask qrcode pillow
```

## Usage

```bash
python app.py
```

**Akses aplikasi di browser:**

```bash
http://localhost:5000
```

**Langkah Penggunaan:**

1.  Buka halaman utama dan isi form transaksi.

2.  Sistem mencatat data ke dalam blockchain dan menghasilkan QR code.

3.  QR dapat diverifikasi melalui halaman verifikasi.

## Testing

```bash
pytest
```

[⬆ Return to Top](#Transaksi-QR)
