# Import library yang diperlukan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Memuat data dari file CSV
data = pd.read_csv('data.csv')  # Ganti 'data.csv' dengan path file Anda

# Menampilkan lima baris pertama dari data
print("Lima baris pertama dari data:")
print(data.head())

# Melihat ringkasan statistik
print("\nRingkasan Statistik:")
print(data.describe())

# Menghitung nilai null
print("\nNilai Null:")
print(data.isnull().sum())

# Menghapus baris yang memiliki nilai null (opsional)
data_cleaned = data.dropna()

# Visualisasi distribusi dari kolom tertentu
plt.figure(figsize=(10, 6))
plt.hist(data_cleaned['kolom_tertentu'], bins=30, alpha=0.7, color='blue')
plt.title('Distribusi dari Kolom Tertentu')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')
plt.grid(axis='y')
plt.show()

# Contoh analisis korelasi
correlation_matrix = data_cleaned.corr()
print("\nMatriks Korelasi:")
print(correlation_matrix)

# Visualisasi matriks korelasi
plt.figure(figsize=(12, 8))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.title('Matriks Korelasi')
plt.xticks(range(len(correlation_matrix)), correlation_matrix.columns, rotation=90)
plt.yticks(range(len(correlation_matrix)), correlation_matrix.columns)
plt.show()
