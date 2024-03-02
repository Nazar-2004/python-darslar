
python_izohli_lugati = {
    'boolean':'Mantiqiy qiymat',
    'float':'O\'nli son',
    'for':'Biror amalni qayta-qayta bajarish sikli',
    'if':'Shartlarni tekshirish operatori',
    'integer':'Butun son',
    'string':'Matn',
    'dictionary':'Lug\'at',
    'list':'Ro\'yxat'
}
for kalit,qiymat in sorted(python_izohli_lugati.items()):
    print(f"{kalit.title()}-{qiymat}")
    