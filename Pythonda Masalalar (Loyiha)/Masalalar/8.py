# 14.03.2024
# Maqsad: # Sonning EKUBIni topish, Ekub- bu eng katta umumiy bo'luvchi
# Muallif : Ne'matov Nazar
def EKUB(x,y): # x = 12, y = 30
    if x > y: # 12 > 30 => ?
        kichik = y
    else:
        kichik = x # x = 12
    for i in range(1, kichik + 1): # 1,12
        if ((x % i == 0) and (y % i == 0)): #  12 % 3 == 0 and 30 % 3 == 0
            ekub = i # ekub = 6
    return ekub

print("Sonning Ekubi:", EKUB(12,30))        

