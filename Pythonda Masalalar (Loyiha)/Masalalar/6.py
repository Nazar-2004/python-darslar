# 2 sonining dastlabki n - ta darajasini aniqlovchi dastur
n = int(input("Sonni kiriting:"))

natija = list(map(lambda x : 2 ** x, range(n+1)))

print(natija)

for i in range(n + 1):
    print("2 soning ",i,"- chi","darajasi :",natija[i])
    
    