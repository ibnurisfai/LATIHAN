# Input nilai dari pengguna
mim=("masiukan nim mahasiswa: ")
nama=("masukan nama mahasiswa: ")
nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))
nilai_kehadiran= float(input("masukan nikai kehadiran: "))

# Hitung nilai akhir
nilai_akhir = (nilai_tugas +  nilai_uts + nilai_uas+ nilai_kehadiran)/4

# Tentukan kriteria kelulusan
if nilai_akhir >= 85:
    status_kelulusan = "A"
    if nilai_akhir>= 70:
        status_kelulusan="B"
        if nilai_akhir>= 55:
            status_kelulusan="C"
            if nilai_akhir >= 45:
                status_kelulusan>= "D"
else:
    status_kelulusan = "TIDAK LULUS(E)"
    

# Tampilkan hasil
print("KELULUSAN MAHASISWA")
print("___________________________________")
print("nama mahasiswa: ",nama)
print("nim mahasiswa: ",mim)
print("Nilai Akhir: ", nilai_akhir)
print("Status Kelulusan: ", status_kelulusan)
