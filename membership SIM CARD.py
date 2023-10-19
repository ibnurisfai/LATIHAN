#membership SIM CARD

poin=int(input("masukan total poin yang diperoleh: "))
total_harga=int(input("masukan total harga: "))
diskon= 0.0
Idcard=int(input("masukan nomor ID CARD: "))

#proses menghitung poin
if poin >= 100:
    member="SILVER"
    if poin>= 1500:
        member="PERUNGGU"
        if poin >= 3000:
            member>= "GOLD"
            if poin >=5000:
                member >="DAIMOND"
            else:
                member >="NON MEMBER"

#proses menghitung diskon
if total_harga>= 1_000_000:
    diskon=0.10
    if total_harga>=2_000_000:
        diskon=0.20
    else:
        diskon=0.0
    #proses 
    besaran_diskon= total_harga * diskon
    bayar= total_harga-besaran_diskon



#tampilkan hasil
print("_________________________________")
print("data pengguna")
print("_________________________________")
print("ID pengguna toko RISFAIZ: ",Idcard)
print("tdak belanjaan anda: ", total_harga)
print("total poin and ", poin)
print("status member pelanggan: ",member)
print("total belanjaan: ", total_harga)
print("jumlah yang harus dibayar: ", bayar)
print("total diskon yang didapat: ",besaran_diskon)



