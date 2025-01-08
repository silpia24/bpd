# Fungsi get_biaya() yang diambil berdasarkan kode program studi yang ada di dalam NIM
# o Contoh: 2411502025, angka 11 (tebal) menjelaskan biaya kuliah = 9.600.000
# o Contoh: 2412502025, angka 12 (tebal) menjelaskan biaya kuliah = 9.100.000
# o Contoh: 2413502025, angka 13 (tebal) menjelaskan biaya kuliah = 9.300.000

def get_biaya(nim):
    nim = str(nim)
    kode_jurusan = nim[2:4]  
    if kode_jurusan == '11':
        return 9600000
    elif kode_jurusan == '12':
        return 9100000
    elif kode_jurusan == '13':
        return 9300000
    else:
        return 'Tidak ada jurusan'
    
# nim = 2411512025
# print(get_biaya(nim))