# Seseorang menyimpan uang Rp. 1.000.000 di bank dengan bunga ber-bunga 2% per bulan. Setelah satu
# bulan uangnya menjadi Rp. 1.020.000. Satu bulan berikutnya uang Rp. 1.020.000 ini mendapat bunga lagi
# 2%, yaitu Rp. 20.400 sehingga setelah 2 bulan uangnya menjadi Rp. 1.020.000 + Rp. 20.400 = Rp.
# 1.040.400. Demikian seterusnya (bunga bulan ini ditambahkan ke saldo uangnya dan mendapatkan bunga
# lagi pada bulan berikutnya). Susun program untuk menghitung dan mencetak jumlah uangnya setelah 10
# bulan kedepan

saldo = 1000000
bunga = 0.02

for i in range(1, 11):
    saldo += saldo * bunga
    print(f"Saldo setelah {i} bulan: {saldo:.2f}")