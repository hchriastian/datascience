import pytchat
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def fetch_comments(video_id):
    """
    Scrape live comments from YouTube using pytchat.
    """
    chat = pytchat.create(video_id=video_id)
    comments = []

    print("Fetching live comments... Press Ctrl+C to stop.")
    try:
        while chat.is_alive():
            for c in chat.get().sync_items():
                comments.append(c.message)
                print(f"[{c.author.name}]: {c.message}")
    except KeyboardInterrupt:
        print("\nScraping stopped.")
    return comments

def analyze_sentiment(comments):
    """
    Analyze sentiment of each comment using TextBlob.
    """
    sentiments = {'positive': 0, 'neutral': 0, 'negative': 0}

    for comment in comments:
        analysis = TextBlob(comment)
        polarity = analysis.sentiment.polarity
        if polarity > 0:
            sentiments['positive'] += 1
        elif polarity == 0:
            sentiments['neutral'] += 1
        else:
            sentiments['negative'] += 1

    return sentiments

def generate_wordcloud(comments):
    """
    Generate and display a word cloud from comments.
    """
    all_comments = " ".join(comments)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_comments)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title("Word Cloud of YouTube Live Comments", fontsize=16)
    plt.show()

if __name__ == "__main__":
    # Ganti dengan ID video live YouTube
    video_id = input("Masukkan ID Video Live YouTube: 8KmMUW9-LV8 ").strip()

    # Fetch live comments
    comments = fetch_comments(video_id)

    # Analyze sentiment
    if comments:
        sentiments = analyze_sentiment(comments)
        print("\nSentiment Analysis:")
        print(f"Positive: {sentiments['positive']}")
        print(f"Neutral: {sentiments['neutral']}")
        print(f"Negative: {sentiments['negative']}")

        # Generate Word Cloud
        generate_wordcloud(comments)
    else:
        print("Tidak ada komentar yang diambil.")
