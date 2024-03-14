# Armstrong sonini topish =>  153 => (1x1x1) + (5x5x5) + (3x3x3) = 1 + 125 + 27 = 153
#  53 = (5*5)+(3*3) - ?
# Armstrong soni bo'lishi uchun sonning raqamlari kubining yig'indisi  shu songa teng bo'lishi kerak. 153
son = int(input("Sonni kiriting: ")) # 153 
sum = 0 # yig'indi uchun

temp = son # temp = 15
while temp > 0: # 1 > 0
    sonning_raqami = temp % 10 # 1 % 10 = 1
    kub = sonning_raqami ** 3 # kub = 1
    sum = sum + kub # sum =152 + 1 153
    temp = temp // 10 # sonni barcha raqmlari uchun uni orqadan hisoblayapmiz! => temp = 0

if sum == son:
    print("Armstrong soni!")
else:
    print("Armstrong soni emas!")         

# 2-usul 
son = int(input("Sonni kiriting: ")) # 153 
daraja = len(str(son))# sonning darajasini topamiz

sum = 0
temp = son # temp = 15
while temp > 0: # 1 > 0
    sonning_raqami = temp % 10 # 1 % 10 = 1
    sum += sonning_raqami ** daraja
    temp = temp // 10 # sonni barcha raqmlari uchun uni orqadan hisoblayapmiz! => temp = 0

if sum == son:
    print("Armstrong soni!")
else:
    print("Armstrong soni emas!")   