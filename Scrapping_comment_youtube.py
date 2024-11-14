# prompt: buatkan program crawling comment di youtube dan export ke csv


from googleapiclient.discovery import build
import pandas as pd

# Ganti dengan API key Anda
api_key = "AIzaSyA0OajU3m8kIoSQmrPzOgi01odx8vPf_CQ"

# Ganti dengan ID video YouTube
video_id = "aQTMTHsLeJ4"

# Buat layanan YouTube Data API
youtube = build('youtube', 'v3', developerKey=api_key)

def get_comments(youtube, video_id):
  comments = []
  request = youtube.commentThreads().list(
      part="snippet",
      videoId=video_id,
      maxResults=1000  # Maksimum komentar yang akan diambil
  )
  while request:
    response = request.execute()
    for item in response["items"]:
      comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
      comments.append(comment)

    request = youtube.commentThreads().list_next(request, response)
  return comments

comments = get_comments(youtube, video_id)

# Buat DataFrame Pandas
df = pd.DataFrame({"Comment": comments})

# Export ke file CSV
df.to_csv("youtube_comments.csv", index=False)

print("Komentar berhasil diekspor ke youtube_comments.csv") 