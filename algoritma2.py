gaji = int(input("masukkan gaji:"))
berkelurga = (False, True)[input("sudah berkeluarga? (Y/T)") == "Y"]
punya_rumah = (False, True)[input("punya rumah? (Y/T)") == "Y"]

if gaji > 3000000:
    print ("Gaji sudah diatas UMR")
    if berkeluarga:
        print ("Wajib ikutan asuransi dan menabung untuk pensiun")
    else:
        print ("Tidak perlu ikutan asuransi")

        if punya_rumah:
            print ("Wajib bayar pajak rumah")
        else:
            print ("tidak wajib bayar pajak rumah")
        else:
print ("Gaji belum UMR")