import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Membuat data kesehatan gigi fiktif
np.random.seed(0)
data = {
    'ID_Pasien': np.arange(1, 10001),
    'Usia': np.random.randint(10, 80, size=10000),
    'Jenis_Kelamin': np.random.choice(['Pria', 'Wanita'], size=10000),
    'Frekuensi_Menyikat_Gigi_per_Hari': np.random.choice([1, 2, 3], size=10000, p=[0.3, 0.5, 0.2]),
    'Pemeriksaan_Gigi_Terakhir': np.random.choice(['< 6 bulan', '6-12 bulan', '1-2 tahun', '> 2 tahun'], size=10000, p=[0.25, 0.35, 0.2, 0.2]),
    'Kondisi_Gigi': np.random.choice(['Sehat', 'Sedikit Karang', 'Gigi Berlubang', 'Gusi Berdarah'], size=10000, p=[0.4, 0.3, 0.2, 0.1]),
}

df = pd.DataFrame(data)
print("Data kesehatan gigi (contoh 5 baris):")
print(df.head())

# Analisis deskriptif
print("\nStatistik deskriptif data kesehatan gigi:")
print(df.describe(include='all'))
print("\nDistribusi data berdasarkan kondisi gigi:")
print(df['Kondisi_Gigi'].value_counts(normalize=True) * 100)


# Visualisasi distribusi usia pasien
plt.figure(figsize=(10, 6))
plt.hist(df['Usia'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribusi Usia Pasien')
plt.xlabel('Usia')
plt.ylabel('Jumlah Pasien')
plt.show()

# Visualisasi distribusi kondisi gigi
plt.figure(figsize=(10, 6))
df['Kondisi_Gigi'].value_counts().plot(kind='bar', color='coral', edgecolor='black')
plt.title('Distribusi Kondisi Gigi Pasien')
plt.xlabel('Kondisi Gigi')
plt.ylabel('Jumlah Pasien')
plt.show()

# Visualisasi frekuensi menyikat gigi
plt.figure(figsize=(10, 6))
df['Frekuensi_Menyikat_Gigi_per_Hari'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightgreen', 'lightblue', 'lightcoral'], startangle=140)
plt.title('Frekuensi Menyikat Gigi per Hari')
plt.ylabel('')
plt.show()
