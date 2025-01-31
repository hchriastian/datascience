import csv

# Data pidato dalam bentuk list paragraf
speech_data = [
    "Di hadapan majelis yang terhormat ini, di hadapan seluruh rakyat Indonesia, dan yang terpenting di hadapan Tuhan Yang Maha Kuasa Allah SWT, saya Prabowo Subianto dan saudara Gibran Rakabuming Raka telah mengucapkan sumpah untuk mempertahankan Undang-Undang Dasar kita, untuk menjalankan semua undang-undang dan peraturan yang berlaku, untuk berbakti pada negara dan bangsa. Sumpah tersebut akan kami jalankan dengan sebaik-baiknya, dengan penuh rasa tanggung jawab, dan dengan semua kekuatan yang ada pada jiwa dan raga kami,” ujar Presiden Prabowo.",
    "Presiden Prabowo mengatakan bahwa bangsa Indonesia menghadapi tantangan besar di tengah dinamika global yang terus berubah. Meski Indonesia diberkahi kekayaan alam yang melimpah, ia mengingatkan bahwa optimisme harus diiringi dengan kesiapan menghadapi hambatan dan ancaman.",
    "“Di tengah segala karunia tersebut, di tengah segala kelebihan yang kita miliki yang memang membuat kita harus menghadapi masa depan dengan optimis, tetapi kita pun harus berani untuk melihat hambatan tantangan rintangan ancaman dan kesulitan yang ada di hadapan kita,” ungkap Presiden.",
    "Dalam pidatonya, Presiden Prabowo juga menekankan pentingnya pemberantasan korupsi dan kolusi yang masih menjadi permasalahan bangsa. Menurutnya, kebocoran anggaran dan penyelewengan harus diatasi dengan keberanian dan transparansi.",
    "“Marilah kita berani mawas diri, marilah kita berani menatap wajah kita sendiri dan mari kita berani memperbaiki diri kita sendiri, marilah kita berani mengoreksi kita sendiri. Kita harus menghadapi kenyataan bahwa masih terlalu banyak kebocoran, penyelewengan, korupsi di negara kita,” ucap Presiden.",
    "Meski Indonesia telah mencapai beberapa prestasi di kancah internasional, seperti menjadi bagian dari G20 dan masuk sebagai ekonomi terbesar ke-16 dunia, Presiden Prabowo mengingatkan bahwa masih banyak pekerjaan rumah yang harus diselesaikan. Mulai dari kemiskinan, kekurangan gizi, hingga masalah pendidikan.",
    "“Marilah kita berani melihat kenyataan, kita boleh bangga dengan prestasi kita, tapi marilah kita jangan tertegun, jangan terlalu cepat puas jangan terlalu cepat gembira dengan menutup mata dan hati kita terhadap tantangan-tantangan dan penderitaan saudara-saudara kita."
]

# Nama file CSV
csv_filename = "pidato_presiden_prabowo.csv"

# Menyimpan data ke dalam file CSV
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Paragraf"])
    for paragraph in speech_data:
        writer.writerow([paragraph])

print(f"Pidato telah disimpan ke {csv_filename}")
