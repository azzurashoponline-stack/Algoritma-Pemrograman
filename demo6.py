def nilai ():
    nilai = []
    sts_nilai = True
    index = 0
    print ("Masukkan nilai anda dari 0-10 dan katakan 'sudah' untuk stop input nilai")
    while sts_nilai == True :
        input_nilai = input("Masukkan nilai ke " + str(index) + " : ")
        if  str(input_nilai) == "sudah":
             sts_nilai = False
        elif int(input_nilai) >= 0 and int (input_nilai) <= 10:
            nilai.append(int(input_nilai))
            index += 1
        else:
            print ("Tolong masukkan nilai yang sesuai (0-10)")
    return nilai

def nilai_terkecil():
    minimum = nilai[0]
    index = 0
    for i in nilai:
        if i < minimum:
            minimum = i
            index += 1
    return minimum

def nilai_terbesar():
    maksimum = nilai[0]
    index = 0
    for i in nilai:
        if i > maksimum:
            maksimum = i
            index += 1
    return maksimum
    
def rata_rata():
    total = 0
    for i in nilai:
        total += i
    rata2 = total / len(nilai)
    return rata2

nilai = nilai()
if len(nilai) == 0:
    print ("Tidak ada nilai yang dimasukkan")
else:
    print ("Anda sudah memasukkan nilai: " + str(nilai))
    minimum = nilai_terkecil()
    maksimum = nilai_terbesar()
    rata2 = rata_rata()
    print ("Nilai terkecil dari nilai yang anda masukkan adalah: " + str(minimum) + ", nilai terbesar adalah: " + str(maksimum) + ", dan rata-ratanya adalah: " + str(rata2))

