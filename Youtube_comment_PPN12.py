from youtube_comment_downloader import YoutubeCommentDownloader
import pandas as pd

# ID Video
video_ids = [
    "5ENLEY94u9M",  # Ganti dengan ID video pertama
    "8T2nmwUAgxY",  # Ganti dengan ID video kedua
    "Eb4CeUE7nOs",  # Ganti dengan ID video ketiga
]

# Fungsi untuk mengambil komentar
def get_comments(video_id):
    downloader = YoutubeCommentDownloader()
    comments = []
    for comment in downloader.get_comments(video_id):
        comments.append({
            'video_id': video_id,
            'author': comment['author'],
            'comment': comment['text'],
            'published_at': comment['time']
        })
    return comments

# Ambil komentar dari semua video
all_comments = []
for video_id in video_ids:
    print(f"Scraping comments for video: {video_id}")
    all_comments.extend(get_comments(video_id))

# Simpan ke dalam CSV
df = pd.DataFrame(all_comments)
df.to_csv('youtube_comments.csv', index=False)
print("Komentar berhasil disimpan ke youtube_comments.csv")
