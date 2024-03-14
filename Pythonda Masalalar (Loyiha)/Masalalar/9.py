# 14.03.2024
# Maqsad: # Sonning bo'luvchilari sonini topish algoritmi
# Muallif : Ne'matov Nazar

son = int(input("Sonni kiriting:"))
sanagich = 0
for i in range(1,son + 1):
    if son % i == 0:
        print(i)
        sanagich += 1
print(son," sonining bo'luvchilari soni:",sanagich," ta")    