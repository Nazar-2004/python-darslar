
menu = {
    'osh':25000,
    'non':7000,
    'shashlik':60000,
    'somsa': 10000,
    'choy':2000,
    'tabaka':35000,
    'manti':8000
}

print("3 ta taom buyurtma bering.")
buyurtmalar = [] # bo'sh ro'yxat yaratamiz
for n in range(3): # foydalanuvchiga 3 ta ovqat so'rashi uchun 3-marta sikl ochamiz
    buyurtmalar.append(input(f"{n+1}-taom:").lower()) # append()-orqali keyingi taomni qo'shib boramiz.

for buyurtma in buyurtmalar: # buyurtmalar ro'yxati ichidagi elementlarni hammasini buyurtma o'zgaruvchisiga yuklaymiz.
    if buyurtma in menu: #Agar buyurtma menu lug'atini  ichida bo'lsa,
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm") # buyurtma narxi chiqaramiz
    else: # Aks holda, pastdagi shartni bajaramiz.
        print(f"Kechirasiz,bizda {buyurtma} yo'q")    