
a,b,c = map(int,input().split())
if (a > b and b > c) or (a > c and c > b):
    x = a - c
elif a > c and c > b:
    x = a - b
elif b > a and a > c:
    x = b - c
elif b > c and c > a:
    x = b - a
elif a > b and b > c:
    x = a - c
elif a > c and c > b:
    x = a - b 

print(x)    
        