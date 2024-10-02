# Fungsi untuk mencetak n suku pertama dari barisan aritmetika
def barisan_aritmetika(a, d, n):
    for i in range(1, n+1):
        suku_n = a + (i - 1) * d
        print(f"Suku ke-{i}: {suku_n}")

# Input
a = 3   # Suku pertama
d = 3   # Beda (selisih antar suku)
n = 10  # Jumlah suku yang ingin ditampilkan

# Output
barisan_aritmetika(a, d, n)
