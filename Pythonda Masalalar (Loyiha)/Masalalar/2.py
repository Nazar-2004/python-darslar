# Fibonachchi sequence (Fibonachi ketma-ketligi)
# 0,1,1,2,3,5,8,13,21
# a = 0, b = 1, c = a + b
a = 0 # 1-chi hadi
b = 1 # 2-chi hadi
son =int(input("Fibonachi ketma-ketligini kiriting: "))
if  son == 1: # 1-chi hadi 0 ga teng!
    print(a)
else:
    print(a) # 1-chi hadi => 0 konsolga chiqryapmiz
    print(b) # 2-chi hadi => 1 konsolga chiqryapmiz
    for i in range(2, son):
        c = a + b # oldingi 2 ta hadi yig'indisi
        a = b
        b = c
        print(c)
            