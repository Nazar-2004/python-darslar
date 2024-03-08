a,b,c = map(int,input().split())
if a != b and b != c:
    x = 3
elif (a != b and  b== c) or ( a == b and b !=c):
    x = 2
else:
    x = 1

print(x)            