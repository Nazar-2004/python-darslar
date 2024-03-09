
print("Mening kompyuter haqidagi testimga xush kelibsiz!")

playing = input("O'yin o'ynashni xohlaysizmi?(yes/no)>>>")

if playing.lower() != "yes":
    quit()

print("Yaxshi,Qani ketdik!")
ball = 0 # To'plangan ballni hisoblash uchun o'zgaruvchi.

javob = input("CPU nimani anglatadi?")
if javob.lower() == "central processing unit":
    print("To'g'ri javob!")
    ball += 1
else:
    print("Xato javob!")    

javob = input("GPU nimani anglatadi?")
if javob.lower() == "graphics processing unit":
    print("To'g'ri javob!")
    ball += 1
else:
    print("Xato javob!")    

javob = input("RAM nimani anglatadi?")
if javob.lower() == "random access memory":
    print("To'g'ri javob!")
    ball += 1
else:
    print("Xato javob!")     
    
javob = input("ROM nimani anglatadi?")
if javob.lower() == "read only memory":
    print("To'g'ri javob!")
    ball += 1
else:
    print("Xato javob!")     

javob = input("HDD nimani anglatadi?")
if javob.lower() == "hard disk drive":
    print("To'g'ri javob!")
    ball += 1
else:
    print("Xato javob!")                 

print("Siz " + str(ball) + "ta savolda to'g'ri javob berdingiz!")  
print("Siz " + str((ball / 5) * 100) + "% natija ko'rsatdingiz.")  