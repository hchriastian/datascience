import tweepy
import pandas as pd
from textblob import TextBlob

# Masukkan kredensial API Anda
API_KEY = 'gFJrq6cH8lQXSwLndKyVniCSZ'  # Ganti dengan API Key Anda
API_SECRET_KEY = 'p0KoGFBk2ZnNwZ3i3Bh4LQZRKas6B5Rk0pQQ2ioonfh28mRNYq'  # Ganti dengan API Secret Key Anda
ACCESS_TOKEN = '1476460745663475715-QdmJolYP5jCAEWWVtDSCRruk3c3D1o'  # Ganti dengan Access Token Anda
ACCESS_TOKEN_SECRET = 'w7zeutMAvJD9k5JCGcTc2RWhzmkZaH4BxlzZCMnCfFR0F'  # Ganti dengan Access Token Secret Anda

# Autentikasi ke Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Memeriksa apakah autentikasi berhasil
try:
    api.verify_credentials()
    print("Authentication OK")
except Exception as e:
    print(f"Error during authentication: {e}")

# Mengambil tweet berdasarkan kata kunci
keyword = 'ibu kota negara IKN'  # Kata kunci untuk pencarian
tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang='id', tweet_mode='extended').items(20)  # Ambil 100 tweet

# Menyimpan tweet dalam list
tweet_data = []
for tweet in tweets:
    tweet_data.append({
        'tweet_id': tweet.id,
        'created_at': tweet.created_at,
        'user': tweet.user.screen_name,
        'text': tweet.full_text,
        'retweet_count': tweet.retweet_count,
        'favorite_count': tweet.favorite_count
    })

# Mengonversi list menjadi DataFrame
df_tweets = pd.DataFrame(tweet_data)

# Fungsi untuk analisis sentimen
def get_sentiment(text):
    analysis = TextBlob(text)
    # Mengembalikan sentimen: positif, negatif, atau netral
    if analysis.sentiment.polarity > 0:
        return 'positif'
    elif analysis.sentiment.polarity < 0:
        return 'negatif'
    else:
        return 'netral'

# Menerapkan analisis sentimen ke kolom 'text'
df_tweets['sentiment'] = df_tweets['text'].apply(get_sentiment)

# Menyimpan DataFrame ke file CSV
df_tweets.to_csv('tweets_sentiment_analysis.csv', index=False)

print("Data berhasil disimpan ke tweets_sentiment_analysis.csv")