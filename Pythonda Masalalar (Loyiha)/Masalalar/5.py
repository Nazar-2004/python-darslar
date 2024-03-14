# Sonning raqamlari yig'indisini topish dasturi
n = int(input("Sonni kiriting:")) # 12

if n < 0:
    print("Iltimos,musbat son kiriting!")
else:
    sum = 0 # 
    while n > 0:
        sum += n # sum = 23
        n -= 1 # n = n - 1 => 22
    
    print(sum)    