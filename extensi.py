import random
import timeit
import matplotlib.pyplot as plt

# Fungsi untuk mengecek apakah elemen dalam array unik atau tidak
def is_unique(arr):
    return len(arr) == len(set(arr))

# Fungsi untuk menghitung rata-rata waktu eksekusi
def calculate_time(func, *args, repeat=10):
    return timeit.timeit(lambda: func(*args), number=repeat) / repeat

# Input dari pengguna untuk NIM (3 digit terakhir)
while True:
    try:
        nim_last3 = int(input("Masukkan 3 digit terakhir NIM Anda: "))
        if 0 <= nim_last3 <= 999:
            break
        else:
            print("Harap masukkan angka antara 000 hingga 999.")
    except ValueError:
        print("Input tidak valid. Masukkan angka yang benar.")

# Menghitung nilai maksimum array
max_value = 250 - nim_last3
print(f"Nilai maksimum array adalah: {max_value}")

# Daftar nilai n untuk array
n_values = [100, 150, 200, 250, 300, 350, 400, 500]

# Seed untuk random generator
random.seed(42)

# Menyimpan waktu eksekusi
average_case_times = []
worst_case_times = []

# Proses untuk setiap nilai n
for n in n_values:
    # Generate array dengan nilai random (average case)
    arr = [random.randint(1, max_value) for _ in range(n)]

    # Menghitung average case
    avg_time = calculate_time(is_unique, arr)
    average_case_times.append(avg_time)

    # Menghitung worst case (memaksa ada duplikat di array)
    arr[-1] = arr[0]  # Menambahkan duplikat untuk worst case
    worst_time = calculate_time(is_unique, arr)
    worst_case_times.append(worst_time)

# Plotting graph
plt.figure(figsize=(10, 6))
plt.plot(n_values, average_case_times, label='Average Case', marker='o', color='blue')
plt.plot(n_values, worst_case_times, label='Worst Case', marker='x', color='red')

plt.title('Performance Analysis: Unique Element Check', fontsize=16)
plt.xlabel('Array Size (n)', fontsize=14)
plt.ylabel('Execution Time (seconds)', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
