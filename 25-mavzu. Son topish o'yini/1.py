# Son topish o'yini
# 25-dars. Funksiyalar SON TOPISH O'YINI
# Sana: 09/03/2024
# Muallif : Ne'matov Nazar

# 1-qism: Kompyuter biror bir sonni o'ylaydi,biz esa ushbu sonni topishga harakat qilamiz. 
import random   # Tasodifiy sonlar bilan ishlash uchun random modulini chaqirib olamiz

def sontop(x=10): # Ushbu funksiya 1-ta parametr qabul qiladi,ya'ni komyuter o'ylagan sonning yuqori  chegarasi.misol x = 10 => (1,10)
    tasodifiy_son = random.randint(1,x) #Endi tasodifiy sonni generatsiya qilish uchun randint() funksiyasi 1-ta tasodifiy butun  sonni qaytaradi.   
    print(f"Men 1 dan {x} gacha son o'yladim.Topa olasizmi?")
    taxminlar = 0 # taxminlar sonini sanaydigan o'zgaruvchi
    
    while True: # Abadiy sikl. Toki foydalanuvchi o'ylangan sonni topguncha sikl davom etadi. Topgandan so'ng tugaydi. 
        taxminlar += 1 
        taxmin = int(input(">>>")) # Foydalanuvchi kiritgan taxmin son
        if taxmin < tasodifiy_son:  # Agar foydalanuvchi kiritgan son tasodifiy sondan kichik bo'lsa...
            print("Xato. Men o'ylagan son bundan kattaroq. Yana harakat qiling:")
        elif taxmin > tasodifiy_son: # Aks holda, foydalanuvchi kiritgan son tasodifiy sondan katta bo'lsa...
            print("Xato. Men o'ylagan son bundan kichikroq. Yana harakat qiling:")    
        else: # Aks holda  foydalanuvchi kiritgan son tasodifiy son bilan teng  bo'lsa, break orqali siklni yakunlaymiz. 
            break
    print(f"Tabriklaymiz. {taxminlar} ta taxmin bilan topdingiz!")    
    return taxminlar    
    
    
# sontop()     # sontop() funksiyasini chaqirdik.   

def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
        if javob == "-":
            yuqori =  taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim!")            
    return taxminlar

# sontop_pc() # sontop_Pc() funksiyasini chaqirdik.   
    
def play(x = 10): # taxminlarni solishtirib kim g'olib bo'lganini aniqlash uchun play() nomli funksiya yaratamiz
    yana = True 
    while yana:
        taxminlar_user = sontop(x) # 1-chi funksiyani chaqiryapmiz, taxminlar sonini topish uchun
        taxminlar_pc = sontop_pc(x)  # 2-chi funksiyani chaqiryapmiz
        # Endi yuqoridagi 2-ta taxminlarni solishtiramiz. Kim yutganini bilish uchun!
        if taxminlar_user > taxminlar_pc: # Agar foydalanuvchi ko'proq taxmin bilan topgan bo'lsa, u yutqizadi. 
            print("Men yutdim!")
        elif taxminlar_user < taxminlar_pc: # Agar kompyuter ko'proq taxmin bilan topgan bo'lsa, u yutqizadi.
            print("Siz yutdingiz!")
        else: # Agar taxminlar bir xil bo'lsa.
            print("Durrang!")       
        yana = int(input("Yana o'ynaysizmi? Ha(1)/Yo'q(0):"))
        

play() # play funksiyasini chaqirdik.        
            

    
    
    
    
    
    
    
    
    
                
        