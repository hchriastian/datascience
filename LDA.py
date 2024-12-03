import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim import corpora
from gensim.models import LdaModel
import pyLDAvis.gensim_models

# Mengunduh stopwords dan punkt dari nltk
nltk.download('punkt')
nltk.download('stopwords')

# Teks contoh (Anda bisa menggantinya dengan teks lain atau data Anda sendiri)
documents = [
    "I love programming in Python.",
    "Python is a versatile language used for machine learning and data science.",
    "Machine learning can help you predict future trends.",
    "Data science involves statistics and machine learning techniques.",
    "Artificial intelligence is the future of technology.",
    "Deep learning is a subset of machine learning."
]

# Preprocessing teks
def preprocess_text(doc):
    # Tokenisasi teks
    tokens = word_tokenize(doc.lower())
    # Menghapus stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    return tokens

# Preprocess seluruh dokumen
processed_docs = [preprocess_text(doc) for doc in documents]

# Membuat dictionary dan corpus untuk LDA
dictionary = corpora.Dictionary(processed_docs)
corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

# Membuat model LDA
lda_model = LdaModel(corpus, num_topics=3, id2word=dictionary, passes=15)

# Menampilkan topik yang ditemukan oleh LDA
topics = lda_model.print_topics(num_words=4)
print("Laporan Topik LDA:\n")
for idx, topic in enumerate(topics):
    print(f"Topik {idx+1}:")
    print(f"  Kata-kata utama: {topic[1]}")
    print("  Deskripsi: Kata-kata ini terkait dengan topik yang membahas tentang teknologi dan ilmu komputer.")
    print("-" * 50)

# Visualisasi hasil LDA
vis = pyLDAvis.gensim_models.prepare(lda_model, corpus, dictionary)
pyLDAvis.display(vis)
