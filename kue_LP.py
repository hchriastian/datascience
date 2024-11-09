import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog


c = [-12800, -14000, -16000, -4800]  # Negatif karena linprog di SciPy meminimalkan fungsi


A = [
    [15000, 3000, 3750, 3250],  # Kendala tepung terigu
    [6000, 1200, 1500, 1300],    # Kendala gula
    [10758, 2152, 2690, 2331]    # Kendala telur
]


b = [50000, 20000, 14368]


x_bounds = (0, None)

result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, x_bounds, x_bounds, x_bounds], method='simplex')


if result.success:
   
    produk_optimal = result.x
    keuntungan_maksimum = -result.fun

   
    produk_nama = ['Bolu Pisang', 'Kue Tape', 'Brownies', 'Roti Tawar']
    keuntungan_per_unit = [12800, 14000, 16000, 4800]


    fig, ax1 = plt.subplots(figsize=(10, 6))

  
    ax1.bar(produk_nama, produk_optimal, color='skyblue')
    ax1.set_xlabel('Jenis Kue')
    ax1.set_ylabel('Jumlah Produksi Optimal (unit)')
    ax1.set_title('Jumlah Produksi Optimal untuk Masing-Masing Jenis Kue')

   
    for i, v in enumerate(produk_optimal):
        ax1.text(i, v + 0.1, f"{v:.2f}", ha='center', va='bottom')

  
    ax2 = ax1.twinx()
    ax2.plot(produk_nama, keuntungan_per_unit, color='green', marker='o', linestyle='-', linewidth=2, label="Keuntungan per Unit")
    ax2.set_ylabel('Keuntungan per Unit (Rp)')
    ax2.legend(loc='upper left')

 
    plt.figtext(0.15, 0.85, f'Keuntungan Maksimum: Rp {keuntungan_maksimum:.2f}', fontsize=12, color='darkred')

    plt.show()

else:
    print("Tidak ada solusi optimal yang ditemukan.")
