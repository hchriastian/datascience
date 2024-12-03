import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

# Pastikan Anda telah mengunduh sumber daya yang dibutuhkan
nltk.download('punkt')
nltk.download('stopwords')

# Membaca file teks
with open('random_texts.txt', 'r') as file:
    documents = file.readlines()  # Membaca semua baris dalam file

# Tampilkan beberapa baris untuk melihat struktur teks
print("Beberapa dokumen dalam file:")
for doc in documents[:5]:  # Menampilkan 5 dokumen pertama
    print(doc)

# Preprocessing Teks: Tokenisasi dan penghapusan stopwords
def preprocess_text(doc):
    # Tokenisasi: Memecah teks menjadi kata-kata
    tokens = word_tokenize(doc.lower())  # Menggunakan lowercase untuk konsistensi
    # Menghapus tanda baca dan stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words]  # Hanya kata-kata yang sah dan bukan stopwords
    return tokens

# Proses seluruh dokumen
processed_docs = [preprocess_text(doc) for doc in documents]

# Menampilkan hasil preprocessing beberapa dokumen pertama
print("\nHasil preprocessing (tokenisasi dan penghapusan stopwords):")
for doc in processed_docs[:5]:
    print(doc)
