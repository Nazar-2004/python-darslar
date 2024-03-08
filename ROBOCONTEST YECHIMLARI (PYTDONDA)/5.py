z = int(input())
s = 0 # shartni qanoatlaniruvchi (x,y) juftliklar soni
n = 0
if z == 0: # (x,y) juftliklar soni 0-ta bo'lsa -1 chiqaramiz
    s = -1
else:
    if z < 0:
        n = -z    