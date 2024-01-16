class TV:
    def _init_(self, merk, harga, stok):
        self.merk = merk
        self.harga = harga
        self.stok = stok

    def tampilkan_info(self):
        print(f"Merk: {self.merk}, Harga: {self.harga} USD, Stok: {self.stok} unit")

def beli_tv(tv, jumlah):
    if tv.stok >= jumlah:
        total_harga = tv.harga * jumlah
        tv.stok -= jumlah
        return f"Anda telah membeli {jumlah} unit {tv.merk}. Total harga: {total_harga} USD."
    else:
        return f"Maaf, stok {tv.merk} tidak mencukupi untuk pembelian ini."

def main():
    daftar_tv = [
        TV("Samsung", 500, 10),
        TV("LG", 450, 15),
        TV("Sony", 600, 8),
        TV("sharp",700, 50),
        TV("toshiba",350, 40),
        TV("xioami", 500 , 35)
    ]

    while True:
        print("\nMenu:")
        print("1. Tampilkan TV")
        print("2. Beli TV")
        print("3. Keluar")

        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            print("\nDaftar TV:")
            for tv in daftar_tv:
                tv.tampilkan_info()
        elif pilihan == "2":
            merk_tv = input("Masukkan merk TV yang ingin dibeli: ")
            tv_terpilih = next((tv for tv in daftar_tv if tv.merk.lower() == merk_tv.lower()), None)

            if tv_terpilih:
                jumlah_pembelian = int(input(f"Masukkan jumlah {tv_terpilih.merk} yang ingin dibeli: "))
                hasil_pembelian = beli_tv(tv_terpilih, jumlah_pembelian)
                print(hasil_pembelian)
            else:
                print("Merk TV tidak ditemukan.")
        elif pilihan == "3":
            print("Terima kasih! Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")

if _name_ == "_main_":
    main()
