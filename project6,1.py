def penjumlahan ():
    print ("Masukkan nilai yang ingin anda jumlahkan")
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    hasil = angka1 + angka2
    print("Hasil penjumlahan dari", angka1, "+", angka2, "adalah", hasil)

def pengurangan ():
    print ("Masukkan nilai yang ingin anda kurangkan")
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    hasil = angka1 - angka2
    print("Hasil pengurangan dari", angka1, "-", angka2, "adalah", hasil)

def perkalian ():
    print ("Masukkan nilai yang ingin anda kalikan")
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    hasil = angka1 * angka2
    print("Hasil perkalian dari", angka1, "x", angka2, "adalah", hasil)

def pembagian ():
    print ("Masukkan nilai yang ingin anda bagi")
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    if angka2 == 0:
        print("Semua angka tidak dapat dibagi dengan 0")
    else:
        hasil = angka1 / angka2
        print("Hasil pembagian dari", angka1, ":", angka2, "adalah", hasil)



print ("Pilih menu perhitungan yang akan digunakan")
menu = input("penjumlahan, pengurangan, perkalian, pembagian : ")
if menu == "penjumlahan":
    penjumlahan()
elif menu == "pengurangan":
    pengurangan()
elif menu == "perkalian":
    perkalian()
elif menu == "pembagian":
    pembagian()
else:
    print("Menu yang anda pilih tidak tersedia")