import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Fungsi untuk menentukan sentimen
def get_sentiment(text):
    analysis = TextBlob(text)
    # Mengembalikan sentimen: positif, negatif, atau netral
    if analysis.sentiment.polarity > 0:
        return 'Positif'
    elif analysis.sentiment.polarity < 0:
        return 'Negatif'
    else:
        return 'Netral'

# Membaca dataset (ganti 'dataset.csv' dengan path ke dataset Anda)
data = pd.read_csv('dataset_IKN.csv')

# Menampilkan nama kolom
print("Nama kolom dalam dataset:", data.columns)

# Mengganti 'text' dengan nama kolom yang sesuai
data['Sentiment'] = data['text'].apply(get_sentiment)  # Ganti 'text' dengan nama kolom yang benar

# Menampilkan hasil
print(data[['text', 'Sentiment']])

# Menyimpan hasil ke file baru
data.to_csv('dataset_with_sentiment.csv', index=False)

# Visualisasi Sentimen
plt.figure(figsize=(8, 6))
sns.countplot(x='Sentiment', data=data, palette='viridis')
plt.title('Distribusi Sentimen')
plt.xlabel('Sentimen')
plt.ylabel('Jumlah')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Visualisasi Word Cloud untuk Komentar Positif
positive_comments = ' '.join(data[data['Sentiment'] == 'Positif']['text']).replace('https', '')
wordcloud_positive = WordCloud(width=800, height=400, background_color='white').generate(positive_comments)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_positive, interpolation='bilinear')
plt.axis('off')  # Menyembunyikan sumbu
plt.title('Word Cloud dari Komentar Positif')
plt.show()

# Visualisasi Word Cloud untuk Komentar Negatif
negative_comments = ' '.join(data[data['Sentiment'] == 'Negatif']['text']).replace('https', '')
wordcloud_negative = WordCloud(width=800, height=400, background_color='white').generate(negative_comments)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_negative, interpolation='bilinear')
plt.axis('off')  # Menyembunyikan sumbu
plt.title('Word Cloud dari Komentar Negatif')
plt.show()