import pandas as pd
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
from nltk.corpus import stopwords
import re

# Download stopwords dari NLTK
nltk.download('stopwords')
stop_words = set(stopwords.words('indonesian'))

# Contoh data komentar tentang program "Makan Bergizi 2025"
data = {
    'komentar': [
        "Program ini sangat bagus untuk meningkatkan gizi masyarakat.",
        "Saya tidak setuju dengan implementasinya, kurang merata.",
        "Luar biasa! Program ini membantu anak-anak mendapatkan gizi yang cukup.",
        "Kurang sosialisasi, banyak yang belum tahu tentang program ini.",
        "Bagus, tapi perlu perbaikan dalam distribusi bantuan.",
        "Program yang sangat bermanfaat untuk masa depan Indonesia."
    ]
}

# Konversi ke DataFrame
df = pd.DataFrame(data)

# Fungsi untuk membersihkan teks
def clean_text(text):
    text = re.sub(r'\W', ' ', text)  # Menghapus karakter khusus
    text = re.sub(r'\s+', ' ', text)  # Menghapus spasi berlebih
    text = text.lower()  # Mengubah ke huruf kecil
    text = ' '.join([word for word in text.split() if word not in stop_words])  # Menghapus stopwords
    return text

# Membersihkan komentar
df['cleaned_komentar'] = df['komentar'].apply(clean_text)

# Analisis Sentimen dengan TextBlob
def get_sentiment_textblob(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positif'
    elif analysis.sentiment.polarity == 0:
        return 'netral'
    else:
        return 'negatif'

df['sentiment_textblob'] = df['cleaned_komentar'].apply(get_sentiment_textblob)

# Analisis Sentimen dengan VADER
def get_sentiment_vader(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    if score['compound'] >= 0.05:
        return 'positif'
    elif score['compound'] <= -0.05:
        return 'negatif'
    else:
        return 'netral'

df['sentiment_vader'] = df['cleaned_komentar'].apply(get_sentiment_vader)

# Tampilkan hasil
print(df[['komentar', 'sentiment_textblob', 'sentiment_vader']])