from faker import Faker
import random

# Inisialisasi objek Faker untuk bahasa Indonesia
fake = Faker('id_ID')

# Daftar kategori atau tema untuk teks acak
categories = ["teknologi", "kesehatan", "pendidikan", "sains", "bisnis", "keuangan", "seni", "olahraga"]

# Fungsi untuk membuat teks acak berdasarkan kategori
def generate_random_text(category):
    # Membuat kalimat acak dengan tema kategori yang dipilih
    sentence = fake.sentence(nb_words=random.randint(5, 10))  # Kalimat pertama
    if sentence is None:
        sentence = "Tidak ada kalimat yang valid."
        
    text = fake.text(max_nb_chars=200)  # Teks tambahan
    if text is None:
        text = "Tidak ada teks yang valid."
        
    # Gabungkan kalimat dan teks, pastikan tidak ada nilai None
    return sentence + " " + text

# Membuat 1000 teks acak
documents = []
for _ in range(1000):
    category = random.choice(categories)  # Pilih kategori secara acak
    document = generate_random_text(category)
    documents.append(document)

# Menyimpan teks acak ke dalam file txt
with open("random_kata.txt", "w") as file:
    for doc in documents:
        file.write(doc + "\n\n")  # Menambahkan newline ganda agar setiap teks terpisah dengan jelas

print("Teks acak dalam bahasa Indonesia telah disimpan dalam 'random_kata.txt'")
