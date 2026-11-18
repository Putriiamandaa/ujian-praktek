# Program Sistem Pengelolaan Stok Barang Toko

print("=== SISTEM PENGELOLAAN STOK BARANG ===")

# 1. Input Data
nama_barang = input("Masukkan nama barang: ")
stok = int(input("Masukkan jumlah stok awal: "))

# 2. Pilih dan Proses Transaksi
while True:
    print("\n=== MENU TRANSAKSI ===")
    print("1. Barang Masuk")
    print("2. Barang Keluar")
    print("3. Selesai")

    pilihan = input("Pilih transaksi (1/2/3): ")

    # 3. Percabangan
    if pilihan == "1":
        jumlah = int(input("Masukkan jumlah barang masuk: "))
        stok += jumlah
        print("Barang berhasil ditambahkan!")

    elif pilihan == "2":
        jumlah = int(input("Masukkan jumlah barang keluar: "))

        if jumlah <= stok:
            stok -= jumlah
            print("Barang berhasil dikeluarkan!")
        else:
            print("Stok Tidak Mencukupi!")

    elif pilihan == "3":
        print("\nTransaksi selesai.")
        break

    else:
        print("Pilihan tidak valid!")

    # 4. Cek Stok
    print("Stok barang saat ini:", stok)

# 5. Tampilkan Hasil
print("\n=== HASIL AKHIR ===")
print("Nama Barang :", nama_barang)
print("Sisa Stok   :", stok)
print("Terima kasih!") 



=== SISTEM PENGELOLAAN STOK BARANG ===
Masukkan nama barang: meja
Masukkan jumlah stok awal: 20

=== MENU TRANSAKSI ===
1. Barang Masuk
2. Barang Keluar
3. Selesai
Pilih transaksi (1/2/3): 1
Masukkan jumlah barang masuk: 30
Barang berhasil ditambahkan!
Stok barang saat ini: 50

=== MENU TRANSAKSI ===
1. Barang Masuk
2. Barang Keluar
3. Selesai
Pilih transaksi (1/2/3): 2
Masukkan jumlah barang keluar: 7
Barang berhasil dikeluarkan!
Stok barang saat ini: 43

=== MENU TRANSAKSI ===
1. Barang Masuk
2. Barang Keluar
3. Selesai
