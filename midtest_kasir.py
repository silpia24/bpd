from datetime import datetime

# Menu dan harga
menu = {
    1: ("Latte", 25000),
    2: ("Cappucino", 23000),
    3: ("Americano", 20000),
    4: ("Milk Tea", 21000)
}

jumlah_pelanggan = 0

while True:
    jumlah_pelanggan += 1
    is_first_10 = jumlah_pelanggan <= 10
    total_price = 0
    total_discount = 0
    orders = []

    print("--------------------------------\n")
    print(f"Pelanggan Ke-{jumlah_pelanggan}")
    print("\nMenu:")
    for key, value in menu.items():
        print(f"{key}. {value[0]} : Rp. {value[1]:,}")

    # Memesan menu
    while True:
        try:
            menu_number = int(input("Masukan nomor menu: "))
            if menu_number not in menu:
                print("Nomor menu tidak valid.\n")
                continue

            quantity = int(input("Jumlah pesanan: "))
            if quantity <= 0:
                print("Jumlah harus lebih dari 0.")
                continue

            item_name, item_price = menu[menu_number]
            discounted_price = item_price

            if is_first_10:
                discounted_price *= 0.70

            discount = (item_price - discounted_price) * quantity
            total_discount += discount
            total_price += discounted_price * quantity
            orders.append((menu_number, item_name, quantity, discounted_price, discount))

            # Tanyakan apakah ingin memesan menu lain
            another_order = input("\nApakah ingin memesan menu lain? (y/n): ").strip().lower()
            if another_order != 'y':
                break
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

    # Input waktu transaksi
    transaction_time = input("\nMasukkan waktu transaksi (HH:MM, atau 'exit' untuk keluar): ").strip()
    if transaction_time.lower() == "exit":
        break

    try:
        transaction_time = datetime.strptime(transaction_time, "%H:%M").time()
    except ValueError:
        print("Format waktu tidak valid. Gunakan HH:MM.")
        continue

    # Cek apakah waktu transaksi di jam early bird
    is_early_bird = datetime.strptime("07:00", "%H:%M").time() <= transaction_time <= datetime.strptime("08:00", "%H:%M").time()

    # Hitung ulang diskon jika early bird
    if is_early_bird:
        total_price = 0
        total_discount = 0
        for order in orders:
            item_price = menu[order[0]][1]
            discounted_price = item_price
            if is_first_10 and is_early_bird:
                discounted_price *= 0.50  # Diskon total 50%
            elif is_first_10:
                discounted_price *= 0.70  # Diskon 30%
            elif is_early_bird:
                discounted_price *= 0.80  # Diskon 20%
            discount = (item_price - discounted_price) * order[2]
            total_discount += discount
            total_price += discounted_price * order[2]

    print("\n-----Ringkasan Transaksi:-----")
    print(f"Nomor Pelanggan Ke-{jumlah_pelanggan}:")
    print(f"Waktu Transaksi: {transaction_time}")
    for order in orders:
        print(f"{order[2]} x {order[1]} (Rp. {order[3]:,.0f} per item) | Diskon per item: Rp. {(order[4] / order[2]):,.0f} | Total Diskon: Rp. {order[4]:,.0f}")

    if is_first_10 and is_early_bird:
        print("\nPelanggan mendapatkan diskon 50% karena termasuk 10 pelanggan pertama dan bertransaksi di jam 07:00-08:00.")
    elif is_first_10:
        print("\nPelanggan mendapatkan diskon 30% karena termasuk 10 pelanggan pertama.")
    elif is_early_bird:
        print("\nPelanggan mendapatkan diskon 20% karena bertransaksi di jam 07:00-08:00.")

    print(f"Total Diskon Keseluruhan: Rp. {total_discount:,.0f}")
    print(f"Total Harga: Rp. {total_price:,.0f}\n")
