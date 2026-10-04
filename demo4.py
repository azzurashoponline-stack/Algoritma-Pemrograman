# game menebak ingredient 
# buat ingredient dalam list yang berisi
# eggs
# flour
# chocolate
# butter
# sugar
# salt 
# jika benar point +1

ingredient_kue = ["eggs","flour","chocolate","butter","sugar","salt"]
score = 0

print("Tebak 3 ingredient untuk membuat kue")
ingredient1 = input("Masukkan ingredient pertama: ")
if ingredient1 in ingredient_kue:
    print("Selamat anda benar!")
    score += 1
else:
    print("Maaf, jawaban anda salah!")
ingredient2 = input("Masukkan ingredient kedua: ")
if ingredient2 in ingredient_kue:
    print("Selamat anda benar!")
    score += 1
else:
    print("Maaf, jawaban anda salah!")
ingredient3 = input("Masukkan ingredient ketiga: ")
if ingredient3 in ingredient_kue:
    print("Selamat anda benar!")
    score += 1
else:
    print("Maaf, jawaban anda salah!")

print("Game Over, Skor akhir anda:", score)   