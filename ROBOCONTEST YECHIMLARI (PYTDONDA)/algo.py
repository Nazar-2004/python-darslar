# 102
n = int(input())
arr = map(int,input().split())
a, b = map(int, input().split())
mn = min(arr) # massivdagi eng kichik elementni aniqlash
for i in range(a-1, b):  # [a,b] oraliqdagi sonlarni i o'zgaruvchisiga yuklayapmiz.
  arr[i] /= mn # [a,b] oraliqdagi sonlarni massivning eng kichik elementiga bo'lyapmiz.
for i in arr:   # massivni ekranga chiqarish uchun sikl
  print(round(i+0.00001, 1), end =' ')  # hammasini bir qatorga chiqaryapmiz