#bisakah anda mengemudi di negara ini
#cari tahu user ingin memilih negara mana "South Africa , Mexico , India , France"
# cari tahu umur user

# persyaratan 
# negara                 South Africa   Mexico                         India       France
# boleh berkendara        usia > 16     usia > 17                      usia > 17   usia > 17
# tidak boleh berkendara  usia <=16     usia < 15                      usia <= 17  usia <= 14
#parental requirment          -         usia 15 parental supervision       -       usia 15-17
#                                       usia 16-17 parental agreement              supervision


negara = input("Pilih negara yang ingin anda kunjungi dengan berkendara (South Africa,Mexico,INdia,France )")
usia = int(input("Masukkan usia anda saat ini = "))

if negara == "South Africa" and usia > 16 :
    print("Anda boleh berkendara")
elif negara == "South Africa" and usia <= 16:
    print("Anda tidak diperbolehkan berkendara")
elif negara == "Mexico" and usia > 17:
    print("Anda boleh berkendara")
elif negara == "Mexico" and usia < 15:
    print("Anda tidak diperbolehkan berkendara")
elif negara == "Mexico" and usia == 15:
    print("Anda perlu didampingi orang tua")
elif negara == "Mexico" and usia >15 and usia<18:
    print("Anda perlu persetujuan orang tua")
elif negara == "India" and usia > 17:
    print("Anda boleh berkendara")
elif negara == "India" and usia <= 17:
    print("Anda tidak boleh berkendara")
elif negara == "France" and usia > 17:
    print("Anda boleh berkendara")
elif negara == "France" and usia <= 14:
    print("Anda tidak boleh berkendara") 
elif negara == "France" and usia > 14 and usia < 18:
    print("Anda perlu dampingan saat berkendara")
else :
    print ("Negara yang anda cari tidak terdaftar")