import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

# Baca data dari CSV
data = pd.read_csv('Dataset3.csv')

# Pisahkan fitur dan target
X = data.drop('target', axis=1)  # fitur
y = data['target']  # target

# Bagi data menjadi data latih dan uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=40)

# Membangun dan melatih model regresi logistik
model = LogisticRegression()
model.fit(X_train, y_train)

# Melakukan prediksi
y_pred = model.predict(X_test)

# Evaluasi model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f'Akurasi: {accuracy}')
print('Confusion Matrix:')
print(conf_matrix)


plt.scatter(X, y, color='blue', label='Data Aktual')  # Data aktual
plt.plot(X, model.predict_proba(X)[:, 1], color='red', label='Probabilitas Positif')  # Probabilitas kelas positif
plt.title('Regresi Logistik Coba')
plt.xlabel('X')
plt.ylabel('Probabilitas kelas 1')
plt.legend()
plt.show()

