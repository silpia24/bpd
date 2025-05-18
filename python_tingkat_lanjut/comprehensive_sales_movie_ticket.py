"""
Nim     : 2412510030
Nama    : Nurul Silpia

Study Case:
Buatlah suatu program python menggunakan dictionary comprehension untuk membuat struktur datanya 
Jika diketahui suatu ruangan berkapasitas 1100 orang akan digunakan untuk menggelar pertunjukan musik, 
dimana tiket terbadi menjadi 4 kelas berbeda. 20 persen digunakan untuk kelas titanium, 20 persen digunakan untuk kelas platinum, 
30 persen digunakan untuk kelas gold dan sisanya digunakan untuk kelas silver 
Selanjutnya, harga tiket sangat dipengaruhi dari kelas-kelas nya. kelas titanium-dibanderol sebesar 1000 platinum 750, gold 500 dan silver 350. 
buatlah suatu struktur data yang digunakan untuk menyimpan kebutuhan sesuai kasus yang disajikan, selanjutnya gunakan dictionary comprehension 
untuk menyimpan data jika tiket yang terjual untuk kelas titanium 10 persen dari kapasitas, platinum 15 persen dari kapasitas, 
sedangkan gold dan silver sold out. terakhir tampilkan data dari dictionary comprehension tersebut
""" 

total_capacity = 1100

# Informasi dasar untuk setiap kelas tiket
class_info = {
    "Titanium": {"percentage_capacity": 0.20, "price": 1000},
    "Platinum": {"percentage_capacity": 0.20, "price": 750},
    "Gold": {"percentage_capacity": 0.30, "price": 500},
    "Silver": {"percentage_capacity": 0.30, "price": 350} # Sisa dari total persentase
}

# Informasi penjualan tiket
# "base_sale": "total_capacity" -> persen penjualan dikali kapasitas total gedung
# "base_sale": "class_capacity" -> persen penjualan dikali kapasitas kelas itu sendiri (misalnya Gold & Silver sold out 100% dari kapasitas kelasnya)
selling_infomation = {
    "Titanium": {"base_sale": "total_capacity", "percentage_sales": 0.10},
    "Platinum": {"base_sale": "total_capacity", "percentage_sales": 0.15},
    "Gold": {"base_sale": "class_capacity", "percentage_sales": 1.00}, # 1.00 artinya 100%
    "Silver": {"base_sale": "class_capacity", "percentage_sales": 1.00} # 1.00 artinya 100%
}

# --- DICTIONARY COMPREHENSION ---
show_information = {
    movie_class: {
        # 1. Hitung kapasitas maksimal kelas ini
        "capacity_maks_class": (class_capacity := int(total_capacity * base_sale["percentage_capacity"])),

        # 2. Ambil harga tiketnya.
        "ticket_price": (ticket_price := base_sale["price"]),

        # 3. Hitung jumlah tiket yang terjual untuk kelas ini.
        "ticket_sell": (
            sold_ticket := int(
                (
                    # JIKA basis penjualannya adalah "total_capacity"...
                    total_capacity
                    if selling_infomation[movie_class]["base_sale"] == "total_capacity"
                    # JIKA BUKAN (berarti basisnya adalah kapasitas kelas itu sendiri)...
                    else class_capacity # Gunakan 'class_capacity' yang sudah kita hitung di nomor 1
                )
                # Hasil dari pengecekan di atas (total_capacity atau class_capacity) dikalikan dengan persentase penjualan tiket untuk kelas ini.
                * selling_infomation[movie_class]["percentage_sales"]
            )
        ),

        # 4. Hitung total pendapatan dari kelas ini.
        "pendapatan_kelas": sold_ticket * ticket_price
    }
    for movie_class, base_sale in class_info.items()
}

# Menampilkan data dari dictionary comprehension
print("Data Pertunjukan Musik:")
for kelas, detail in show_information.items():
    print(f"\nKelas: {kelas}")
    print(f"  Kapasitas Maks Kelas: {detail['capacity_maks_class']} orang")
    print(f"  Harga Tiket: Rp {detail['ticket_price']}")
    print(f"  Tiket Terjual: {detail['ticket_sell']} tiket")
    # Pengecekan tiket terjual tidak melebihi kapasitas maks kelas
    if detail['ticket_sell'] > detail['capacity_maks_class'] and (kelas == "Titanium" or kelas == "Platinum"):
         print(f"  Warning: Tiket terjual awal ({detail['ticket_sell']}) dihitung dari % total kapasitas.")
         print(f"             Karena melebihi kapasitas kelas ({detail['capacity_maks_class']}), maka tiket terjual disesuaikan menjadi {detail['capacity_maks_class']}.")
    print(f"  Pendapatan Kelas: Rp {detail['pendapatan_kelas']}")


# Menghitung total pendapatan keseluruhan dan total tiket terjual
total_pendapatan_keseluruhan = 0
total_ticket_sell_keseluruhan = 0

for kelas, detail in show_information.items():
    tiket_terjual_aktual_untuk_kelas = detail['ticket_sell']
    if (kelas == "Titanium" or kelas == "Platinum") and detail['ticket_sell'] > detail['capacity_maks_class']:
        tiket_terjual_aktual_untuk_kelas = detail['capacity_maks_class']

    total_ticket_sell_keseluruhan += tiket_terjual_aktual_untuk_kelas
    total_pendapatan_keseluruhan += tiket_terjual_aktual_untuk_kelas * detail['ticket_price']


print("\n========================================")
print(f"Total Tiket Terjual Keseluruhan: {total_ticket_sell_keseluruhan} tiket")
print(f"Total Pendapatan Keseluruhan: Rp {total_pendapatan_keseluruhan}")
print("========================================")
