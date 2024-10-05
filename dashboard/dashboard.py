import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Memuat DataFrame yang sudah kamu buat sebelumnya
merged_data = pd.read_csv('all_data.csv')  # Ganti dengan path file yang sesuai jika perlu

# Judul Dashboard
st.title("Dashboard E-commerce")

# Visualisasi 10 Produk Teratas
st.header("10 Produk dengan Pembelian Terbanyak")

# Hitung jumlah pembelian untuk setiap produk
product_sales = merged_data.groupby('product_category_name')['order_id'].count().reset_index()  # Ganti ke 'product_category_name' jika 'product_category_name_english' tidak ada
product_sales.columns = ['product_name', 'purchase_count']
top_products = product_sales.sort_values(by='purchase_count', ascending=False)

# Plot Horizontal Bar Chart
fig1, ax1 = plt.subplots(figsize=(12, 6))
ax1.barh(top_products['product_name'].head(10), top_products['purchase_count'].head(10), color='skyblue')
ax1.set_xlabel('Jumlah Pembelian')
ax1.set_title('10 Produk dengan Pembelian Terbanyak')
ax1.invert_yaxis()  # Membalik sumbu y agar produk teratas di atas
st.pyplot(fig1)  # Tampilkan plot dengan Streamlit

# Visualisasi Metode Pembayaran
st.header("Metode Pembayaran yang Paling Banyak Digunakan")

# Hitung jumlah penggunaan setiap metode pembayaran
payment_methods = merged_data.groupby('payment_type')['payment_type'].count().reset_index(name='count')
top_payment_methods = payment_methods.sort_values(by='count', ascending=False)

# Plot Bar Chart
fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.bar(top_payment_methods['payment_type'], top_payment_methods['count'], color='skyblue')
ax2.set_title('Metode Pembayaran yang Paling Banyak Digunakan', fontsize=16)
ax2.set_xlabel('Metode Pembayaran', fontsize=12)
ax2.set_ylabel('Jumlah Penggunaan', fontsize=12)
ax2.tick_params(axis='x', rotation=45)
plt.tight_layout()
st.pyplot(fig2)  # Tampilkan plot dengan Streamlit

# Plot Pie Chart
fig3, ax3 = plt.subplots(figsize=(8, 8))
ax3.pie(top_payment_methods['count'], labels=top_payment_methods['payment_type'], autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
ax3.set_title('Distribusi Penggunaan Metode Pembayaran', fontsize=16)
plt.tight_layout()
st.pyplot(fig3)  # Tampilkan plot dengan Streamlit
