n = int(input("Massiv elementlari sonini kiriting n="))
a = list(map(int,input().split())) # n- ta butun sonni bitta satrga kiritish  
s = 0
Maxxx = max(a) # Massivning eng katta elementi
for i in range(len(a)):
    print('%.2f'% (a[i]/Maxxx),end=" ") # Massivning eng katta elementini uning barcha elementlariga bo'lyapmiz
    