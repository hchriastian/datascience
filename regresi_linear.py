# Import library yang dibutuhkan
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Membuat dataset contoh
# X akan menjadi fitur (variabel independen), dan y sebagai target (variabel dependen)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 2, 3, 3.5, 5])

# Memisahkan dataset menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat model regresi linear
model = LinearRegression()

# Melatih model dengan data latih
model.fit(X_train, y_train)

# Melakukan prediksi dengan data uji
y_pred = model.predict(X_test)

# Menampilkan koefisien regresi dan intercept
print("Koefisien regresi:", model.coef_)
print("Intercept:", model.intercept_)

# Menampilkan hasil prediksi
print("Prediksi:", y_pred)
print("Data aktual:", y_test)

# Visualisasi hasil regresi linear
plt.scatter(X, y, color='blue')  # Data aktual
plt.plot(X, model.predict(X), color='red')  # Garis regresi
plt.title('Regresi Linear Sederhana')
plt.xlabel('X')
plt.ylabel('y')
plt.show()
