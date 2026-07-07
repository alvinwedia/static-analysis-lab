# 🔬 Laporan Hasil Static Analysis (Reverse Engineering Lab)

Repository ini berisi dokumentasi teknis mendalam mengenai analisis statis terhadap dua sampel file executable (`rufus-4.7.exe`).
---
## 📑 LAPORAN STATIC ANALYSIS 1: `rufus-4.7.exe`

### 1. Identitas Objek Analisis
| Item | Keterangan |
| :--- | :--- |
| **Nama File** | `rufus-4.7.exe` |
| **Hash MD5** | `f052acd38a010b6a1ffa26fdc229a229` |
| **Hash SHA256** | `45777d818fc9ba187bcc7b930583764130ea71100fd9e3c66d4a7143bdbce4c5` |
| **Ukuran File** | `1.61 MB (1,687,344 bytes)` |
| **Sistem Operasi Target** | `Windows (x64)` |
| **Kategori Pengujian** | Pembaikan / Utilitas Valid |

### 2. Ringkasan Hasil Analisis
| Aspek | Hasil |
| :--- | :--- |
| **Bahasa Pemrograman** | `C / C++` |
| **Arsitektur** | `x64 (64-bit / PE32+)` |
| **Jenis File** | `EXE (Portable Executable)` |
| **Packer/Protector** | `UPX (Ultimate Packer for eXecutables)` |
| **Obfuscation** | `Ya (Kompresi Kode / Packing murni)` |
| **Tingkat Risiko** | `Bersih` |

### 3. Analisis Header File
| Parameter | Nilai |
| :--- | :--- |
| **Entry Point** | `0x0048EA30` (Rutin awal stub unpacking UPX) |
| **Image Base** | `0x0000000140000000` |
| **Section Jumlah** | `3` |

### 4. Analisis Section
| Section | Size (Raw Disk) | Entropy | Keterangan |
| :--- | :--- | :--- | :--- |
| `UPX0` | `0 bytes` | `0.00` | **Anomali Penting:** Ukuran di disk kosong, namun memesan ruang memori virtual sebesar ~3 MB. Ini dipersiapkan sebagai wadah hasil ekstraksi kode asli saat dijalankan di RAM. |
| `UPX1` | `1,632,256 bytes` | `7.99` | **Anomali Penting:** Nilai entropi mendekati batas maksimal (8.00). Menandakan seluruh data di dalam section ini terkompresi kuat atau terenkripsi. |
| `.rsrc` | `43,008 bytes` | `3.94` | Menyimpan resource standar aplikasi (Ikon, Manifes, UI). |

### 5. Temuan Potensial & Analisis String
Ditemukan import fungsi kritis seperti `VirtualProtect` pada Import Address Table (IAT) yang sangat minimalis. Fungsi API Windows ini secara tipikal dimanfaatkan oleh stub UPX untuk mengubah hak akses memori wilayah `UPX0` menjadi *Execute* (`PAGE_EXECUTE_READWRITE`) setelah proses dekompresi payload selesai dilakukan di RAM.
