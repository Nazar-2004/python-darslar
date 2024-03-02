
davlatlar = {
    "o'zbekiston":"toshkent",
    "aqsh":"vashington d.c",
    "rossiya":'moskva',
    "tojikiston":"dushanbe",
    "qirg'iziston":"bishkek",
    "qozog'iston":"nursulton",
    "malayziya":"kuala-lumpur",
    "singapur":"singapur",
    "italiya":"rim"
}

# print("Dunyo davlatlari:")
# for davlat in sorted(davlatlar):
#     print(davlat.upper())
    
# print("\nDavlatlarning poytaxtlari:")
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.title())

country = input("Qaysi davlat poytaxtini bilishni istaysiz?:").lower()
capital = davlatlar.get(country)
if capital == None:
    print("Kechirasiz,bizda bu haqida ma'lumot yo'q")
else:
    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")    














    
    