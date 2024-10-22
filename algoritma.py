# Inisialisasi variabel
max = 0

while True:
    # Meminta input dari pengguna
    x = int(input("Masukkan bilangan (0 untuk berhenti): "))
    
    # Jika input adalah 0, berhenti
    if x == 0:
        break
    
    # Memeriksa apakah bilangan lebih besar dari max
    if x > max:
        max = x

# Setelah loop berakhir, cetak nilai maksimum
print("Bilangan terbesar adalah:", max)