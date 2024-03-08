yil = int(input()) 
x = ""  
if yil < 10:
    x = "000"
elif yil < 100:
    x = "00"
elif yil < 1000:
    x = "0"

if yil % 400 == 0 or yil % 4 == 0 and yil % 100 != 0: # Kabisa yiliga tekshiryapmiz
    x = f"12/09/{x+str(yil)}"
else:
    x = f"13/09/{x+str(yil)}"

print(x)    