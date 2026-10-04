# mencari tahu lama waktu/jam tidur user
# mencari tahu lama waktu/jam kerja user
# mencari tahu lama waktu/jam istirahat/santai tiap hari kerja user
# mencari tahu lama waktu/jam istirahat/santai tiap akhir pekan user

jam_tidur = float(input("Berapa lama anda tidur? "))
jam_kerja = float(input("Berapa lama anda bekerja? "))
jam_istirahat_hk = float(input("Berapa lama anda istirahat tiap hari kerja? "))
jam_istirahat_ap = float(input("Berapa lama anda istirahat tiap akhir pekan? "))

# rumus penghitungan
# menghitung waktu yang tersedia untuk user per hari kerja :
# 24 - waktu tidur - waktu kerja - waktu santai - 3

waktu_tiap_hk = 24 - jam_tidur - jam_kerja - jam_istirahat_hk -3

# menghitung waktu yang tersedia untuk user per akhir pekan :
# 24 - waktu tidur - waktu santai akhir pekan - 3

waktu_tiap_ap = 24 - jam_tidur - jam_istirahat_ap - 3

# menghitung waktu yang tersedia untuk user per minggu :
# 5 * waktu yang tersedia tiap hari kerja + 2 * waktu yang tersedia tiap akhir pekan

waktu_per_minggu = 5 * waktu_tiap_hk + 2 * waktu_tiap_ap

# tampilan waktu yang tersedia
print("Jadi waktu yang masih tersedia tiap hari kerja adalah = ", waktu_tiap_hk , "jam")
print("Jadi waktu yang masih tersedia tiap akhir pekan adalah = ", waktu_tiap_ap, "jam")
print("Jadi waktu yang masih tersedia per minggu adalah = ", waktu_per_minggu, "jam")