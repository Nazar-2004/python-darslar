lower = int(input("Pastki chegarani kiriting: "))
upper = int(input("Yuqori chegarani kiriting: "))


for son in range(lower, upper + 1):
    daraja = len(str(son))
    sum = 0
    temp = son 
    while temp > 0:
        sonning_raqami = temp % 10
        sum += sonning_raqami ** daraja
        temp //= 10
    if son == sum:
        print(son)    
    