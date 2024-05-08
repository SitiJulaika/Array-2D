data_barang = [
    ["Minyak"              ,3000 , 10],
    ["Tepung"              ,2700 , 10],
    ["Mie"                 ,3500 , 20],
    ["Teh Celup"           ,3000 , 14],
    ["Kopi"                ,3100 , 19]
]
print("===========TABEL HARGA DAN STOK BARANG===========")
print()
print("Nama Barang              Harga         Stok")
for barang in data_barang:
    print(f"{barang[0]:<25}{barang[1]:<15}{barang[2]:<2}")
keuntungan_terbesar = data_barang[0][1] * data_barang[0][2]
keuntungan_terkecil = data_barang[0][1] * data_barang[0][2]
total_keuntungan = 0
for barang in data_barang:
    keuntungan = barang[1] * barang[2]  
    total_keuntungan += keuntungan
    if keuntungan > keuntungan_terbesar:
        keuntungan_terbesar = keuntungan
        nama_barang_terbesar = barang[0]
    elif keuntungan < keuntungan_terkecil:
        keuntungan_terkecil = keuntungan
        nama_barang_terkecil = barang[0]
print()        
print("=================================================")
print()
print("                     HASIL             ")
print()
print(f"Barang dgn keuntungan terbesar: {nama_barang_terbesar}")
print(f"Barang dgn keuntungan terkecil: {nama_barang_terkecil}")
print(f"Total keuntungan              : {total_keuntungan}")

    