# Fungsi get_jurusan() berdasarkan kode program studi yang ada di NIM.
# o Contoh: 2411502025, angka 11 (tebal) menjelaskan kode program studi Teknik Informatika
# o Contoh: 2412502025, angka 12 (tebal) menjelaskan kode program studi Sistem Informasi
# o Contoh: 2413502025, angka 13 (tebal) menjelaskan kode program studi Sistem Komputer

def get_jurusan(nim):
    nim = str(nim)
    kode_jurusan = nim[2:4]  
    if kode_jurusan == '11':
        return 'Teknik Informatika'
    elif kode_jurusan == '12':
        return 'Sistem Informasi'
    elif kode_jurusan == '13':
        return 'Sistem Komputer'
    else:
        return 'Tidak ada jurusan'

# nim = 2413502025
# print(get_jurusan(nim))