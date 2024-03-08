
a,b = map(int,input().split())
yigindi = 0
for i in range(a,b+1):
    if i % 3 == 0 and i % 7 != 0:
        yigindi += i

print(yigindi)        
        
