# Buat program dengan Python, jika ada inputan dari 3 harga, gimana caranya untuk cari nilai yang bukan
# tertinggi tapi bukan terendah juga (harga produk harus bilangan bulat sembarang)

# harga1 = int(input("Masukkan harga pertama: "))
# harga2 = int(input("Masukkan harga kedua: "))
# harga3 = int(input("Masukkan harga ketiga: "))

# harga = [harga1, harga2, harga3]

# harga.remove(max(harga))
# harga.remove(min(harga))

# print("Harga yang bukan tertinggi dan bukan terendah:", harga[0])


harga1 = int(input("Masukkan harga pertama: "))
harga2 = int(input("Masukkan harga kedua: "))
harga3 = int(input("Masukkan harga ketiga: "))

if (harga1 > harga2 and harga1 < harga3) or (harga1 < harga2 and harga1 > harga3):
    nilai_tengah = harga1
elif (harga2 > harga1 and harga2 < harga3) or (harga2 < harga1 and harga2 > harga3):
    nilai_tengah = harga2
else:
    nilai_tengah = harga3

print("Harga yang bukan tertinggi dan bukan terendah:", nilai_tengah)