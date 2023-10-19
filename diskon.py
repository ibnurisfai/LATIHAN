print("MENGHITUNG DISKON")
#inputan data 
nama=("masukan nama pelanggan: ")
totalharga=int(input("Masukan total harga yang harus dibayar: "))
diskon= 0.0

#perhtingan diskom
if totalharga >=1_000_000:
    diskon= 0.10
    if totalharga>= 2_000_000:
        diskon=0.20
        if totalharga>= 3_500_000:
            diskon=0.30

        besaran_diskon= totalharga * diskon
        bayar= totalharga-besaran_diskon

#tampilkan diskon
        print("total belanjaan: ", totalharga)
        print("jumlah yang harus dibayar: ", bayar)
        print("total diskon yang didapat: ",besaran_diskon)