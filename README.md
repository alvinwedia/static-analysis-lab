# static-analysis-lab
# 🔬 Static Analysis Lab
Laporan praktikum analisis statis terhadap beberapa sampel binary PE (Portable Executable) untuk mata kuliah Reverse Engineering.

## 🎯 Tujuan
Repository ini berisi dokumentasi pembedahan file binary tanpa mengeksekusinya di memori. Tujuannya adalah untuk memahami struktur PE Header, mengidentifikasi *packer* (seperti UPX/Themida), dan mengekstrak informasi penting (seperti *strings* dan *Import Address Table*).

## 🛠️ Tools yang Digunakan
Berikut adalah alat bantu yang saya gunakan dalam analisis ini:
* **Detect It Easy (DiE):** Untuk mendeteksi *packer*, *compiler*, dan melihat tingkat entropi file.
* **PEstudio / PEview:** Untuk membedah struktur PE Header, Section, dan tabel Import/Export.
* **BinText / FLOSS:** Untuk mengekstrak *strings* (teks yang bisa dibaca) dari dalam binary.
* **VirusTotal:** Untuk memverifikasi *hash* file dengan database *threat intelligence*.
* **Ghidra / IDA Free:** (Opsional) Untuk melihat dekompilasi kode *assembly* dasar.

## ⚠️ Disclaimer Legalitas
Semua file yang dianalisis di sini dilakukan di dalam lingkungan terisolasi (Virtual Machine). **Tidak ada file *malware* aktif (.exe) yang diunggah ke dalam repository ini** demi alasan keamanan dan etika.
