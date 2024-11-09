from scipy.optimize import linprog

# Koefisien fungsi tujuan (maximization problem)
c = [-12800, -14000, -16000, -4800]  # Negatif karena linprog di SciPy meminimalkan fungsi

# Koefisien kendala (constraints) - berbentuk Ax <= b
A = [
    [15000, 3000, 3750, 3250],  # Kendala tepung terigu
    [6000, 1200, 1500, 1300],    # Kendala gula
    [10758, 2152, 2690, 2331]    # Kendala telur
]

# Batas kendala
b = [50000, 20000, 14368]

# Batasan variabel keputusan (X1, X2, X3, X4 >= 0)
x_bounds = (0, None)

# Menyelesaikan model menggunakan metode Simpleks
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, x_bounds, x_bounds, x_bounds], method='simplex')

# Menampilkan hasil
if result.success:
    print("Jumlah produksi optimal per hari:")
    print(f"X1 (Bolu Pisang)  : {result.x[0]:.2f} unit")
    print(f"X2 (Kue Tape)     : {result.x[1]:.2f} unit")
    print(f"X3 (Brownies)     : {result.x[2]:.2f} unit")
    print(f"X4 (Roti Tawar)   : {result.x[3]:.2f} unit")
    print(f"\nKeuntungan maksimum: Rp {-result.fun:.2f}")
else:
    print("Tidak ada solusi optimal yang ditemukan.")
