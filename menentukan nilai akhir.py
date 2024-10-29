# Input data
nama = input("Masukkan nama: ")
uts = int(input("Masukkan nilai UTS: "))
uas = int(input("Masukkan nilai UAS: "))
tugas = int(input("Masukkan nilai Tugas: "))

# Menghitung nilai akhir
akhir = (tugas * 0.2) + (uts * 0.4) + (uas * 0.4)

# Menentukan status kelulusan
keterangan = "LULUS" if akhir > 60 else "TIDAK LULUS"

# Menentukan nilai huruf
if akhir > 80:
    huruf = "A"
elif akhir > 70:
    huruf = "B"
elif akhir > 50:
    huruf = "C"
elif akhir > 40:
    huruf = "D"
else:
    huruf = "E"

# Menampilkan hasil
print(f"\nNama        : {nama}")
print(f"Nilai UTS   : {uts}")
print(f"Nilai UAS   : {uas}")
print(f"Nilai Tugas : {tugas}")
print(f"Nilai Akhir : {akhir}")
print(f"\nNilai Huruf : {huruf}")
print(f"Keterangan  : {keterangan}")