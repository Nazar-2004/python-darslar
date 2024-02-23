s = 0
n = int(input())
aa = list(map(int,input().split())) # n- ta butun sonni bitta satrga kiritish  
for i in  range(n):
    s = s + aa[i]**2
print(s)    