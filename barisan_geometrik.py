# Fungsi untuk mencetak n suku pertama dari barisan geometri
def barisan_geometri(a, r, n):
    for i in range(n):
        suku_n = a * (r ** i)
        print(f"Suku ke-{i+1}: {suku_n}")

# Input
a = 2   # Suku pertama
r = 2   # Rasio
n = 10  # Jumlah suku yang ingin ditampilkan

# Output
barisan_geometri(a, r, n)
