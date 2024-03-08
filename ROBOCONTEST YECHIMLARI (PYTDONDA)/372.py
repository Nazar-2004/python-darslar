a,b,c = map(int,input().split())
if a > b and a>c:
    katta = a
elif b > a and b > c:
    katta = b
else:
    katta = c
print(katta)            