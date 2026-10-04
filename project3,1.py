#cari tahu suhu ruangan 
#jika suhu < 20 menyalakan pemanas
#jika suhu = 20-25 katakan suhu stabil / kondisi suhuu ok
#jika suhu > 25 menyalakan cooler   

suhu = float(input("Masukkan suhu ruangan saat ini "))

if suhu < 20 :
    print("Suhu saat ini dingin, maka Heater akan menyala")
    print("Menyalakan Heater")
elif suhu >= 20 and suhu <= 25:
     print("Suhu ruangan saat ini stabil atau Ok")
else:
    print("Suhu ruangan saat ini panas, maka Cooler akan menyala")
    print("Menyalakan Cooler")
