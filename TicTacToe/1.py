
import random # kompyuter tasodifiy joyga "O" qo'yishi uchun random modulini chaqirdik.
# Start (Boshlash)
taxta = ["-", "-", "-",    # O'yin xoch(taxtasini)  ro'yxat ko'rinishida 3 ta qatorga chop etyapmiz. 
         "-", "-", "-",
        "-", "-", "-",
]

firstPlayer = "X" # 1-chi foydalanuvchi "X" ni kiritadi. 
winner = None  # g'alabani boshiga 0 (None) ga teng deb qo'yamiz.
gameRunning = True # Dasturni ishlab turishi uchun boshlanishiga True(1) ga tenglab qo'yamiz

# 1-printing the game board (O'yin taxtasini chiqarish)
def printTaxta(taxta): # o'yin taxtasini chiqarish uchun  printTaxta() funksiyasini yaratamiz, va unga taxta degan parametrni yuboramiz. 
    print(taxta[0] + " | " + taxta[1] + " | " + taxta[2])  # Va ro'yxat indexlariga murojaat qilish orqali konsolga chiqaramiz.
    print("----------") 
    print(taxta[3] + " | " + taxta[4] + " | " + taxta[5])
    print("----------")         
    print(taxta[6] + " | " + taxta[7] + " | " + taxta[8])
# take player input (O'yinchi ma'lumotlarini qabul qilish)
def playerInput(taxta):
    kiritish = int(input("1-9 gacha son kiriting: ")) # 1-chi o'yinchi 1-dan  9  gacha son kiritadi. 
    if kiritish >= 1 and kiritish <= 9 and taxta[kiritish-1] == "-":
        taxta[kiritish - 1] = firstPlayer
    else:
        print("Afsuski,computer allaqachon bu yerni bosgandi!")
        
# check for win or tie (G'alaba yoki Durrang bo'lishini tekshirish)
def SatrTekshir(taxta): # O'yindagi gorizontal bo'lganligini tekshirish uchun funksiya
    global winner
    if taxta[0] == taxta[1] == taxta[2] and taxta[1] != "-":
        winner =taxta[0]
        return True
    elif taxta[3] == taxta[4] == taxta[5] and taxta[3] !="-":
        winner = taxta[3]
        return True
    elif taxta[6]== taxta[7] == taxta[8] and taxta[6] != "-":
        winner = taxta[6]
        return True
    
def UstunTekshir(taxta): # Satrni tekshiramiz.     
    global winner
    if taxta[0] == taxta[3] == taxta[6] and taxta[0] != "-":
        winner = taxta[0]  # bu yerda  taxta[0] ning qiymati dastlabki kiritganimizga,ya'ni "X", yoki "O" ga tenglayapmiz.
        return True
    elif taxta[1] == taxta[4] == taxta[7] and taxta[1] != "-":
        winner = taxta[1]
        return True
    elif taxta[2] == taxta[5] == taxta[8] and taxta[2] != "-":
        winner = taxta[2]
        return True

def DiagonalTekshir(taxta):
    global winner
    if taxta[0] == taxta[4] == taxta[8] and taxta[0] != "-":
        winner = taxta[0]
        return True
    elif taxta[2] == taxta[4] == taxta[6] and taxta[2] != "-":
        winner = taxta[2]
        return True
    
def DurrangTekshir(taxta):
    global gameRunning
    if "-" not in taxta :  # Agar taxta nomli ro'yxatning ichida  "-" ishora bo'lmasa...
        printTaxta(taxta)
        print("Durrang!")
        gameRunning = False
        
def checkWin():
    if DiagonalTekshir(taxta)  or SatrTekshir(taxta) or UstunTekshir(taxta):
        print(f"Tabriklaymiz,{winner} yutdi!")

# switch the player (O'yinchini almashtirmoq)
def switchPlayer():
    global firstPlayer
    if firstPlayer == "X":
        firstPlayer = "O"
    else:
        firstPlayer = "X" 
# computer
def  computer(taxta):
    while firstPlayer == "O":
        saqla = random.randint(0, 8)
        if taxta[saqla] == "-":
            taxta[saqla] = "O"
            switchPlayer()  

# check for win or tie again (Yutgan yoki durrang bo'lganligini yana tekshirish )

while gameRunning:
    printTaxta(taxta)
    playerInput(taxta)
    checkWin()
    DurrangTekshir(taxta)
    switchPlayer()
    computer(taxta)
    checkWin()
    DurrangTekshir(taxta)

