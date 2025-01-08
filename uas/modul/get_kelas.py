# Fungsi get_kelas() yang diambil berdasarkan kode kelas yang ada di dalam NIM
# o Contoh: 2411502025, angka 0 (tebal) menjelaskan kelas reguler.
# o Contoh: 2412512025, angka 1 (tebal) menjelaskan kelas karyawan.

def get_kelas(nim):
    nim = str(nim)
    kelas = nim[5]  
    if kelas == '0':
        return 'Reguler'
    elif kelas == '1':
        return 'Karyawan'
    else:
        return 'Tidak ada kelas'
    

# nim = 2413512025
# print(get_kelas(nim))