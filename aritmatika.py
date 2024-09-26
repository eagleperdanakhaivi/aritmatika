def deret_aritmatika(n):
    # Inisialisasi nilai awal dan selisih
    awal = 2
    selisih = 3
    deret = []
    
    # Loop untuk menghasilkan deret aritmatika
    for i in range(n):
        deret.append(awal + i * selisih)
    
    return deret

# Input dari pengguna
N = int(input("Masukkan jumlah deret: "))
# Output deret aritmatika
hasil = deret_aritmatika(N)
print(", ".join(map(str, hasil)))
