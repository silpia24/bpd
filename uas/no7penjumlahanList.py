# Buatlah program untuk menjumlahkan data antara dua buah list dengan menggunakan fungsi, jika diketahui
# List A = [1, 2, 4, 8] dan List B = [16, 32, 64, 128]

listA = [1, 2, 4, 8]
listB = [16, 32, 64, 128]

result = [a + b for a, b in zip(listA, listB)]

print("Hasil penjumlahan:\n", result)