#""" Date: 2022-12-28"""
# """Thame: Dictinary (lug'at)"""
# taomlar = {
#     'ali':"osh",
#     'vali':"pilav",
#     'hasan':"mastava"
#     }
# print(f"alining sevimli taomi{taomlar['ali']}")
"""Qiymatni qo'shish"""
# taomlar["bobur"] = 'narin'
# taomlar["azimjon"] = input("Azimjonning taomi ?")
# # print(taomlar)
"""Qiymat o'zgartirish"""
# taomlar[hasan] = "qozon_kabob"
# print(taomlar)
"""Qiymqtni o'chirish"""
# del taomlar["vali"]
# print(taomlar)
"""get() metodi"""
# print(taomlar["abror"])
# print(taomlar.get("abror","bunday key yo'q"))
# """items() metodi"""
# print(taomlar)
# print(taomlar.items())
# for key,value in taomlar.items():
#     print(f"{key.title()} ning sevimli taomi {value.title()}")

# davlatlar = {
#     'uzbekiston': "Tashkent", 
#     'usa':"vashinton",
#     'Russia':"Maskiva"
# }
# savol = input("Davlat nomini kiriting").lower()
# if savol in davlatlar:
#     print(f"Siz so'ragan {savol}ning poytaxti {davlatlar[savol].title()}")
# else:
#     print(f"Siz so'ragan {savol.title()} haqida bizdamalumot yo'q")
# """keys() va values""" 
# davlatlar = {
#     'uzbekiston': "Tashkent", 
#     'usa':"vashinton",
#     'Russia':"Maskiva"
# }
# for key in davlatlar.keys():
#     print(f"{key}")
# for value in davlatlar.values():
#     print(f"{value}")
    
# ismlar = {
#     '1':"Ali",
#     '2':"Hasan",
#     '3':"Husan",
# }
# for kalit, qiymat in ismlar.items():
#     print(f"Salom do'stim {qiymat} sening tartib raqaming {kalit}")
# for key in ismlar.keys():
#     print(f"Salom do'stim sening tartib raqaming {key}")
# for value in ismlar.values():
#     print(f"Salom do'stim sening tartib raqaming {value}")

"""vazifa"""
# oila = {
#     'otam': "Nurillo 1938 yil Buxoro viloyatida tug'ulgan",
#     'onam': "Sharofat 1948 yil, Buxoro viloyatida tug'ulgan", 
#     'akam': "Sadullo 1968 yil, Buxoro viloyatida tug'ulgan",
# }
# print(f"Meni otam ismi {oila['otam']}")

# otam = {
#     'ism':"Ali",
#     "yosh":"25",
#     "shaxar":"Namangan"
# }
# print(f"Mening otamning ismi {otam['ism']}, yoshi {otam['yosh']} da, {otam['shaxar']} shaxrida tug'ilgan")


#2
# taomlar = {
#     'Nurillo': "shashlik",
#     'Sharofat': "manti", 
#     'Sadullo': "kabob",
# }
# print(f"Nurilloning sevimli taomi {taomlar['Nurillo']}")

#3
# lugat = {
#     'integer': "butun_son",
#     'float': "o'nlik_son", 
#     'if': "agar",
#     'for': "uchun",
#     'in': "ichida", 
#     'and': "va",
#     'else': "yana",
# }
# print(lugat.items())
# for key, volue in lugat.items():
#     print(f"{key.title()} ning tarjimasi {volue.upper()}")
#4
# lugatlar = {
#     'integer': "butun_son",
#     'float': "o'nlik_son", 
#     'if': "agar",
#     'for': "uchun",
#     'in': "ichida", 
#     'and': "va",
#     'else': "yana",
# }
# print(lugatlar.get("string","bunday key yo'q"))

#5
# lugatlar = {
#     'integer': "butun_son",
#     'float': "o'nlik_son", 
#     'if': "agar",
#     'for': "uchun",
#     'in': "ichida", 
#     'and': "va",
#     'else': "yana",
# }
# savol = input("lugat nomini kiriting").lower()
# if savol in lugatlar:
#     print(f"Siz so'ragan {savol}ning manosi {lugatlar[savol].title()}")
# else:
#     print(f"Siz so'ragan {savol.title()} haqida bizda malumot yoq")
    
#6
# lugatlar = {
#     'airport': "plane",
#     'forest': "tree", 
#     'house': "people",
#     'rever': "fish",
#     'teacher': "students", 
#     'father': "son",
#     'mather': "girl",
# }
# lugatlar['class'] = "chair"
# lugatlar['aroq'] = "suv"
# lugatlar['oltin'] = "kumush"
# lugatlar['qogoz'] = "ruchka"
# print(lugatlar)
# print(lugatlar.items())
# for key, volue in lugatlar.items():
#     print(f"{key.title()}ning manosi {volue.title()}")

#7
# davlatlar = {
#     'rasiya': "maskva",
#     'ozbekiston': "toshkent", 
#     'germaniya': "berlin",
#     'angilya': "londin",
#     'kariya': "seul", 
#     'partugalya': "lisabung",
#     'qozoqiston': "astana",
# }
# for key in davlatlar.keys():
#     print(f"{key.title()}")
# for volue in davlatlar.values():
#     print(f"{volue.title()}")
#8 
# davlatlar = {
#     'rasiya': "maskva",
#     'ozbekiston': "toshkent", 
#     'germaniya': "berlin",
#     'angilya': "londin",
#     'kariya': "seul", 
#     'partugalya': "lisabung",
#     'qozoqiston': "astana",
# }
# savol = input("davlatni nomini kiriting").lower()
# if savol in davlatlar:
#     print(f"Siz soragan {savol}ning poytaxti {davlatlar[savol].title()}")
# else:
#     print(f"siz soragan {savol.title()} haqida bizda malumot yoq")

#9
# taomlar = {
#     'osh': "10000",
#     'shashlik': "11000", 
#     'manti': "9000",
#     'lagmon': "12000",
#     'shurva': "13000", 
#     'somsa': "15000",
#     'jiz': "20000",
# }
# buyurtma = []
# savol1 = input("1-ovqatni buyurtma bering ")
# savol2 = input("2-ovqatni buyurtma bering ")
# savol3 = input("3-ovqatni buyurtma bering ")
# buyurtma.append(savol1)
# buyurtma.append(savol2)
# buyurtma.append(savol3)
# for key,value in taomlar.items():
#     for n in buyurtma:
#         if n == key:
#             print(f"Siz so'ragan {n}ning narxi {value}")
#         # else:
#         #     print(f"siz so'ragan {n} yo'q")
# for n in buyurtma:
#     if n not in taomlar.keys():
#         print(f"Siz soragan {n} yoq")


