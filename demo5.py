menu_pizza = ["Margherita", "calzone", "four cheese", "Pepperoni", "napoli"]
pizza_order = []
proses = True
harga = 0

print ("Selamat datang di restoran pizza kami")
print ("Ini adalah menu pizza yang tersedia:")
for i in enumerate(menu_pizza):
    print (str(i[0] + 1) + ". " + i[1])
while proses == True:
    pilih = input("Apakah anda ingin menambahkan pizza ke menu order? (ya / tidak) : ")
    if pilih == "ya":
        print ("Ketik 'cukup' jika anda sudah selesai memilih pizza")
        order  = True
        while order == True:
            pizza = input("Pilih pizza yang ingin Anda pesan (1-5) : ")
            if pizza == "cukup":
                order = False
            elif int(pizza) >= 1 and int(pizza) <= 5:
                    harga += 10
                    pizza_order.append(menu_pizza[int(pizza)-1 ])
                    print ("Pizza yang anda tambahkan adalah: " )                 #+ menu_pizza[int(pizza)-1]
                    for i in enumerate(pizza_order):
                        print (str(i[0] + 1) + ". " + i[1])         
                    # print ("Orderan anda saat ini:", pizza_order)
            else:
                print ("Pilihan tidak valid. Silakan pilih lagi.")
    elif pilih == "tidak":
            proses = False
    else:
        print ("Pilihan tidak valid. Silakan pilih lagi.")
    if proses == False:
        if harga == 0:
            print ("Anda tidak memesan pizza, terimakasih sudah datang ke restoran kami")
        elif harga >= 10:
            print ("Anda perlu membayar sebesar: ", harga , "€")
            tip = True
            while tip == True:
                tip_input = input("Apakah anda ingin memberikan tip? (ya / tidak) : ")
                if tip_input == "ya":
                    tip_amount = int(input("Masukkan jumlah tip yang ingin Anda berikan (0-25%): "))
                    harga += (tip_amount*harga)/100
                    print ("Total pembayaran anda adalah: ", harga , "€")
                    print ("Terimakasih sudah datang ke restoran kami, sampai jumpa lagi!")
                    tip = False
                elif tip_input == "tidak":
                    print ("Total pembayaran anda adalah: ", harga , "€")
                    print ("Terimakasih sudah datang ke restoran kami, Pizza anda sedang dibuat!")
                    tip = False
                else:
                    print ("Pilihan tidak valid. Silakan pilih lagi.")                
               






# for item in menu_pizza :
#                         nama_pizza = item.split(". ", 1)[1]
#                         pizza_order.append(nama)
#                         print (pizza_order)
