import csv
from googleapiclient.discovery import build
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Function to fetch YouTube comments using YouTube API
def fetch_comments(video_id, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=1000,
        textFormat='plainText'
    )
    response = request.execute()

    comments = []
    for item in response.get('items', []):
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)
    return comments

# Sentiment analysis function
def analyze_sentiments(comments):
    sentiments = []
    positive_comments = []
    negative_comments = []

    for comment in comments:
        polarity = TextBlob(comment).sentiment.polarity
        sentiments.append({'comment': comment, 'polarity': polarity})
        if polarity > 0:
            positive_comments.append(comment)
        elif polarity < 0:
            negative_comments.append(comment)
    
    return sentiments, positive_comments, negative_comments

# Generate Word Cloud
def generate_wordcloud(comments, title):
    all_words = ' '.join(comments)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_words)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.show()

# Function to plot positive and negative comment counts
def plot_sentiment_counts(positive_count, negative_count):
    labels = ['Positive Comments', 'Negative Comments']
    counts = [positive_count, negative_count]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, counts, color=['green', 'red'])
    plt.ylabel('Number of Comments')
    plt.title('Count of Positive and Negative Comments')
    plt.show()

# Function to export comments to CSV
def export_to_csv(sentiments, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Comment', 'Polarity'])  # Write header
        for sentiment in sentiments:
            writer.writerow([sentiment['comment'], sentiment['polarity']])  # Write comment and polarity

# Example usage:
api_key = "AIzaSyCbIAhKOxfL_4OVN_DmNB_fMV6_Zuos02A"  # Replace with your YouTube Data API key
video_id = "8KmMUW9-LV8"  # Replace with the desired YouTube video ID

# Fetch comments
comments = fetch_comments(video_id, api_key)

# Display total number of comments
total_comments = len(comments)
print(f"Total Comments: {total_comments}")

# Analyze sentiments
sentiments, positive_comments, negative_comments = analyze_sentiments(comments)

# Display positive and negative comments
print("Positive Comments:")
for comment in positive_comments:
    print(f"- {comment}")

print("\nNegative Comments:")
for comment in negative_comments:
    print(f"- {comment}")

# Generate Word Cloud
generate_wordcloud(comments, "Word Cloud of YouTube Comments")

# Display positive comments word cloud
if positive_comments:
    generate_wordcloud(positive_comments, "Word Cloud of Positive Comments")

# Display negative comments word cloud
if negative_comments:
    generate_wordcloud(negative_comments, "Word Cloud of Negative Comments")

# Plot sentiment counts
plot_sentiment_counts(len(positive_comments), len(negative_comments))

# Export sentiments to CSV
export_to_csv(sentiments, 'youtube_comments_sentiments.csv')