import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

# Set page config
st.set_page_config(page_title="E-commerce Analysis Dashboard", layout="wide")

# Judul dan identitas
st.title("Proyek Analisis Data: E-commerce")
st.write("- **Nama:** Deva Athaya Aryaputra")
st.write("- **Email:** devathaya2016@gmail.com")
st.write("- **ID Dicoding:** Deva Athaya Aryaputra")

# Sidebar untuk navigasi
st.sidebar.header("Navigasi")
page = st.sidebar.selectbox("Pilih Halaman", ["Home", "Top 10 Kota", "Top 10 Produk", "Kesimpulan"])

# Fungsi untuk memuat data
@st.cache_data
def load_data():
    top_10_cities = pd.read_csv('top_10_cities.csv')
    top_10_products = pd.read_csv('top_10_products.csv')
    plots_data = pd.read_csv('plots_data.csv')
    return top_10_cities, top_10_products, plots_data

# Memuat data
top_10_cities, top_10_products, plots_data = load_data()

if page == "Home":
    st.header("Selamat Datang di Dashboard Analisis E-commerce")
    st.write("Dashboard ini menyajikan analisis data e-commerce berdasarkan jumlah customer dan penjualan produk.")
    
elif page == "Top 10 Kota":
    st.header("Top 10 Kota dengan Jumlah Customer Terbanyak")
    st.dataframe(top_10_cities)

    # Visualisasi kota
    st.subheader("Visualisasi Top 10 Kota")
    cities_plot = base64.b64decode(plots_data['cities_plot'].iloc[0])
    st.image(BytesIO(cities_plot), use_column_width=True)

    # Filter untuk kota
    city_filter = st.selectbox("Pilih Kota untuk Detail", top_10_cities['customer_city'])
    filtered_city = top_10_cities[top_10_cities['customer_city'] == city_filter]
    st.write(filtered_city)

elif page == "Top 10 Produk":
    st.header("Top 10 Produk dengan Penjualan Terbanyak")
    st.dataframe(top_10_products)

    # Visualisasi produk
    st.subheader("Visualisasi Top 10 Produk")
    products_plot = base64.b64decode(plots_data['products_plot'].iloc[0])
    st.image(BytesIO(products_plot), use_column_width=True)

    # Filter untuk produk
    product_filter = st.selectbox("Pilih Kategori Produk untuk Detail", top_10_products['product_category_name'])
    filtered_product = top_10_products[top_10_products['product_category_name'] == product_filter]
    st.write(filtered_product)

elif page == "Kesimpulan":
    st.header("Kesimpulan")
    st.write("- Kota yang memiliki customer paling banyak adalah", top_10_cities.iloc[0]['customer_city'])
    st.write("- Barang yang paling banyak terjual adalah", top_10_products.iloc[0]['product_category_name'])

# Tombol untuk mengunduh data
st.sidebar.header("Unduh Data")
if st.sidebar.button("Unduh Data Top 10 Kota"):
    top_10_cities.to_csv('top_10_cities.csv', index=False)
    st.sidebar.success("Data Top 10 Kota telah diunduh.")
if st.sidebar.button("Unduh Data Top 10 Produk"):
    top_10_products.to_csv('top_10_products.csv', index=False)
    st.sidebar.success("Data Top 10 Produk telah diunduh.")