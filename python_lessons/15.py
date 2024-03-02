# 15-dars. Lug'at(Dictionary) bilan ishlaymiz.
# Sana: 02/03/2024
# Muallif : Ne'matov Nazar

# .items() metodi - bu lug'atdagi barcha elementlarni (kalit va qiymatlarni) qulay ko'rinishda chiqaradi. element
# talaba_0 = {
#     'ism':'nazar',
#     'familiya':'ne\'matov',
#     'yosh':20,
#     'fakultet':'kompyuter injinering',
#     'kurs':2
# }

# print(talaba_0['ism'].title())
# print(talaba_0['yosh'])
# print(talaba_0.items())

# for kalit,qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n")   

# telefonlar = {
#     'ali':'iphone x',
#     'nazar':'galaxy M12',
#     'anvar':'mi 10 pro',
#     'umid':'galaxy s9'
# }

# for  k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")
    
# keys()-metodi bu lug'atdagi faqat kalitlarni qiymatini qaytaradi.
# mahsulotlar = {
#     'olma':10000,
#     'anor':12000,
#     'anjir':25000,
#     'shaftoli':30000,
#     'kivi': 35000
# }

# print(mahsulotlar.keys())

# 1-usul
# print('Do\'kondagi mahsulotlar:')
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())


# 2-usul
# print('Do\'kondagi mahsulotlar:')
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())
mahsulotlar = {
    'olma':10000,
    'anor':12000,
    'anjir':25000,
    'shaftoli':30000,
    'kivi': 35000
}
# print(mahsulotlar)
# bozorlik = ['anor','uzum','non','baliq','anjir']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
        

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos do'koningizga {buyum} ham olib keling")
      
      
# LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH
 
# mahsulotlar = {
#     'olma':10000,
#     'anor':12000,
#     'anjir':25000,
#     'shaftoli':30000,
#     'kivi': 35000
# }
# print("Do'konimizdagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

# .values() - lug'atdagi faqat qiymatlarni chiqarish uchun metod

# telefonlar = {
#     'ali':'iphone x',
#     'nazar':'galaxy M12',
#     'anvar':'mi 10 pro',
#     'umid':'galaxy s9'
# }

# print(telefonlar.values())

# print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
# for tel in telefonlar.values():
#     print(tel)

# set() funksiyasi bu lug'atda bir nechta bir xil qatnashgan elementlarni faqat bir marta chiqaradi.(ya'ni takrorlanganlarini)
telefonlar = {
    'ali':'iphone x',
    'nazar':'galaxy M12',
    'anvar':'mi 10 pro',
    'umid':'galaxy s9',
    'husan':'iphone x',
    'hasan':'galaxy s9',
    'jalol':'iphone x'
}
# print(telefonlar)
# for telefon in telefonlar.values():
#     print(telefon)

# set() - bu ma'lumot turi (U ham o'zida turli ma'lumotlarni saqlaydi)
print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
for tel in set(telefonlar.values()):
    print(tel)
    
# set()- ni ichidagi elementlar takrorlanmaydi! 
toys = {"ball","car","panda","ball","bear","car"}    

print(type(toys))
print(toys)