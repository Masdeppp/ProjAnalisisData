# E-commerce Analysis Dashboard

## Deskripsi
Aplikasi ini adalah dashboard analisis data e-commerce yang menyajikan informasi tentang jumlah customer di berbagai kota dan penjualan produk. Dashboard ini dibangun menggunakan Streamlit dan menyediakan visualisasi yang interaktif untuk membantu pengguna memahami data dengan lebih baik.

## Fitur
- Menampilkan daftar 10 kota dengan jumlah customer terbanyak.
- Menampilkan daftar 10 produk dengan penjualan terbanyak.
- Visualisasi grafik untuk kota dan produk.
- Fitur filter untuk melihat detail berdasarkan kota atau kategori produk.
- Opsi untuk mengunduh data dalam format CSV.

## Prerequisites
Sebelum menjalankan aplikasi, pastikan Anda telah menginstal Python dan pip. Anda juga perlu menginstal beberapa library yang diperlukan.

## Instalasi
1. **Clone Repository**
   ```bash
   git clone <URL_REPOSITORY>
   cd <NAMA_FOLDER>
   ```

2. **Instal Library yang Diperlukan**
   Pastikan Anda berada di dalam lingkungan virtual (opsional) dan jalankan perintah berikut:
   ```bash
   pip install streamlit pandas matplotlib seaborn
   ```

3. **Siapkan Data**
   Pastikan file CSV (`top_10_cities.csv`, `top_10_products.csv`, dan `plots_data.csv`) berada di folder yang sama dengan file `app.py`.

## Menjalankan Aplikasi
Untuk menjalankan aplikasi, gunakan perintah berikut:
```bash
streamlit run app.py
```
Setelah menjalankan perintah tersebut, aplikasi akan terbuka di browser Anda, biasanya di `http://localhost:8501`.

## Navigasi
- **Home**: Menampilkan sambutan dan deskripsi aplikasi.
- **Top 10 Kota**: Menampilkan tabel dan grafik untuk 10 kota dengan jumlah customer terbanyak.
- **Top 10 Produk**: Menampilkan tabel dan grafik untuk 10 produk dengan penjualan terbanyak.
- **Kesimpulan**: Menyajikan kesimpulan dari analisis data.

## Mengunduh Data
Anda dapat mengunduh data untuk 10 kota dan 10 produk dengan mengklik tombol yang tersedia di sidebar.

## Kontribusi
Jika Anda ingin berkontribusi pada proyek ini, silakan fork repository ini dan buat pull request.

## Lisensi
Proyek ini dilisensikan di bawah MIT License. Lihat file LICENSE untuk detail lebih lanjut.