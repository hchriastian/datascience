# Import library yang dibutuhkan
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

# Membuat dataset contoh
# X adalah fitur (variabel independen) dan y sebagai target (variabel dependen)
# Di sini kita membuat contoh sederhana dengan 2 fitur dan target biner
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10],[11],[12],[13]])
y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1])

# Memisahkan dataset menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat model regresi logistik
model = LogisticRegression()

# Melatih model dengan data latih
model.fit(X_train, y_train)

# Melakukan prediksi dengan data uji
y_pred = model.predict(X_test)

# Menampilkan akurasi
print("Coba Akurasi model:", accuracy_score(y_test, y_pred))

# Menampilkan confusion matrix untuk melihat performa klasifikasi
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", conf_matrix)

# Visualisasi data dan hasil prediksi
plt.scatter(X, y, color='blue', label='Data Aktual')  # Data aktual
plt.plot(X, model.predict_proba(X)[:, 1], color='red', label='Probabilitas Positif')  # Probabilitas kelas positif
plt.title('Regresi Logistik Sederhana')
plt.xlabel('X')
plt.ylabel('Probabilitas kelas 1')
plt.legend()
plt.show()
