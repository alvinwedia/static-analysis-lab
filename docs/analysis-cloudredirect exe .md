## 📑 LAPORAN STATIC ANALYSIS 2: `CloudRedirect.exe`

### 1. Identitas Objek Analisis
| Item | Keterangan |
| :--- | :--- |
| **Nama File** | `CloudRedirect.exe` |
| **Hash MD5** | `e392aee5c7375703636652d6f6e5214f` |
| **Hash SHA256** | `926db44f7fe1b5c0bb8d32c5ba44e4d61e04afc2e5e7c890c7207360a7a28a9f` |
| **Ukuran File** | `14.87 MB (15,602,941 bytes)` |
| **Sistem Operasi Target** | `Windows (x64)` |
| **Kategori Pengujian** | Aplikasi Finansial / Cloud Routing Client |

### 2. Ringkasan Hasil Analisis
| Aspek | Hasil |
| :--- | :--- |
| **Bahasa Pemrograman** | `C# (.NET 8)` |
| **Arsitektur** | `x64 (64-bit / PE32+)` |
| **Jenis File** | `EXE (Native Host Launcher with Managed Overlay)` |
| **Packer/Protector** | `.NET Single-File Deployment Bundle (Self-Contained)` |
| **Obfuscation** | `Tidak secara langsung (Terbungkus di dalam Kontainer)` |
| **Tingkat Risiko** | `Sedang (Memerlukan verifikasi logika lanjutan)` |

### 3. Analisis Header File
| Parameter | Nilai |
| :--- | :--- |
| **Entry Point** | `0x00011AB0` |
| **Image Base** | `0x0000000140000000` |
| **Section Jumlah** | `6` |

### 4. Analisis Section
| Section | Size (Raw Disk) | Entropy | Keterangan |
| :--- | :--- | :--- | :--- |
| `.text` | `91,136 bytes` | `6.34` | Berisi kode *native bootstrapper* standar dari Microsoft .NET Core (apphost.exe). |
| `.rdata` | `48,640 bytes` | `4.83` | Menyimpan data read-only untuk launcher biner. |
| `.data` | `2,560 bytes` | `2.40` | Alokasi variabel global dasar. |
| `.pdata` | `5,632 bytes` | `4.84` | Berisi tabel informasi Exception Handling arsitektur x64. |
| `.reloc` | `1,024 bytes` | `4.80` | Tabel relokasi dasar untuk pengondisian memori biner. |
| `.rsrc` | `60,928 bytes` | `7.95` | Manifes utama, informasi aset, dan ikon launcher. |

### 5. Analisis Temuan Khusus: Struktur Overlay Raksasa
Berdasarkan kalkulasi matematika, akumulasi total seluruh ukuran *Section* resmi di dalam tabel PE biner ini hanya berkisar **~210 KB**. Adanya selisih masif hingga mencapai ukuran akhir **14.87 MB** mengindikasikan struktur **Overlay** yang sangat besar (data tambahan yang disuntikkan secara mentah di luar batas tabel section resmi).

Hasil ekstraksi string pada area ekor biner (*tail components*) mendeteksi sidik jari bundle framework .NET modern:
* `CloudRedirect.dll` (Logika bisnis dan inti program utama)

**`CloudRedirect.exe` (Modern Single-File Bundling):** File `.exe` ini sejatinya hanyalah "kulit peluncur" (*native stub host runner*). Seluruh kode program asli yang berupa kode terkelola (*managed MSIL assembly code*) tersimpan utuh di dalam sektor *Overlay*. Analisis biner ini tidak memerlukan teknik *Unpacking* manual lewat *Debugger*, melainkan diekstrak atau didekompilasi langsung menggunakan *specialized .NET tools* seperti **ILSpy**, **dnSpy**, atau **DotPeek** untuk mengembalikan kode sumber C# yang bersih dan terstruktur.
* `Wpf.Ui.dll` & `Wpf.Ui.Abstractions.dll` (Pustaka antarmuka grafis modern berbasis WPF)
* Runtime internal `.NET 8.0 Engine` yang di-embed secara mandiri (*Self-Contained*).
