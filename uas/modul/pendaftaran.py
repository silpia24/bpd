import get_kelas
import get_biaya
import get_jurusan

def cetak(nim):
    kelas = get_kelas.get_kelas(nim)
    biaya = get_biaya.get_biaya(nim)
    jurusan = get_jurusan.get_jurusan(nim)
    print("NIM      : " + str(nim))
    print("Kelas    : " + str(kelas))
    print("Biaya    : " + str(biaya))
    print("Jurusan  : " + str(jurusan))

nim = input("Masukkan NIM: ")
nama = str(input("Masukkan Nama: "))
phone = int(input("Masukkan Phone: "))
email = str(input("Masukkan Email: "))
alamat = str(input("Masukkan Alamat: "))

print("\n-------------------------\n")
cetak(nim)
print("Nama     : ", nama)
print("Nomor HP : ", phone)
print("Email    : ", email)
print("Alamat   : ", alamat)
