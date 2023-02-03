#1   
# while True:
#     savol = input("Istalgan son kiriting (dasturni toxtatish uchun 'exit' or 'quuit' deb yozing): ")
#     if savol == 'exit'or 'quuit':
#         break
#     elif savol.isdigit() and savol > 0:
#         print(int(savol)**3)
#     elif int(savol) <= 0:
#         continue
#     else:
#         print("son kriting !!!")
#
# 18
# insonlar = {
#     "inson" : {
#         "ism" : "Ali",
#         "familya" : "Valiyev",
#         "yili" : "2000",
#         "kasbi" : "O'qtuvchi"
#     },
# }
# print(f"salom bu inson {insonlar['inson']['ism']} {insonlar['inson']['familya']} {insonlar['inson']['yili']} {insonlar['inson']['kasbi']}")
 
#19
# son = int(input("istalgan son kiriting "))  
# if son > 0:
#     print(f"{son} musbat")  
# elif son == 0:
#     print(f"{son} 0 ga teng")
# else:
#     print(f"{son} manfiy") 
#20
# taomlar = {
#     'ali':'osh',
#     'vali':'shashlik'
# }
# print(taomlar.get("abror","bunday key yo'q"))
#17
# x = 1
# while x < 10:
#     print(x) 
#     x = x+1

# d = 16
# import math
# print(math.sqrt(d))

# a1 = 3
# b1 = 4
# c = a1 + b1
# savol = "a+b nechiga teng? "
# javob = "{a1}+{b1} = {c}"
# print(savol, javob)

# """yoshni topivchi dastur"""
# year = int(input("Qaysi yilda tugulgansiz: "))
# age = 2023-year
# print(f"Siz {year} yili tugulgansiz  va yoshingiz {age} toshad")

# x,y,z = 1,2,3
# print(x,y,z)
"""kvadrat va kubni topish dasturi"""
# number = int(input(" bir son kiriting: "))
# kv = number**2
# kub = number**3
# print(f"Siz kiritgan {number} sonning kvadrati {kv} ga va kubi {kub} ga teng ")

# """kvadratning yuzasi va peremetirini topish dasturi"""
# kvadrat = int(input("Biror son kiriting: "))
# yuza = kvadrat**2
# peremetr = kvadrat*4
# print(f"tomoni {kvadrat} ga teng bolgan kvadratning yuzi {yuza} va peremetri {peremetr} ga teng  ")

# """ uchburchakning gipatinuzasini topuvch dastur"""
# a = int(input("Birinchi katetni kiriting: "))
# b = int(input("Ikkinchi katetni kirirting: "))
# c = a**2+b**2
# import math
# c = round(math.sqrt(a**2+b**2),2)
# print(f"katetlari {a} va {b} ga teng bolgan uch burchakni gipatunasi {c} ga teng")

"""element va index"""
# mevalar = ["olma","qovun","nok","shaftoli","qaroli"]
# print(mevalar)
# print(mevalar[4])
# print(mevalar[0])
# print(mevalar[-3])
# print(f"Biz bugun kechqurin {mevalar[0].capitalize()} va {mevalar[-2].upper()} yeymiz")
# # royxat elementlarini ozgartirish
# mevalar[1] = "gilos"
# print(mevalar)
# mevalar.append("bodom") #element boyicha qoshadi
# print(mevalar)
# mevalar.insert(1,"olcha") #indeks boyicha qoshadi
# print(mevalar)
# mevalar.remove("olma") # element boyicha ochiradi
# print(mevalar) 
# yangi_mevalar = []
# yangi_mevalar.append(mevalar.pop(-1))
# print(yangi_mevalar)
# len()-royxatni uzunligini olchaydi
# print(f"Bizning savatda {len(mevalar)} mevalar bor")
# print(f"they are {mevalar[0]},{mevalar[1]},{mevalar[-4]},{mevalar[3]},{mevalar[4]},{mevalar[-1]}")

"""range sonli oraliq shakillantirish uchun funksiya"""
# sonlar = list(range(1,20))
# print(sonlar)
# sonlar1 = sonlar[10:15]
# print(sonlar1)

""" sort. riyxatni alifbo korinishada tartiblash """
# name = ["zafar","bobur","axmad","hasan"]
# print(name)
# name.sort()
# name.sort(reverse=True)
# print(name)
# name.reverse()
# print(name)

""" range """
# number = list(range(-10,20))
# print(number)
# print(max(number))
# print(min(number))
# print(sum(number))

# number1 = [1,6,5,4,1,5,44,5,22,14,43,-245,-54,65,147,547,-547]
# number1.sort()
# print(f"Bizning royxatdagi eng katta son {max(number1)} va eng kichik son {min(number1)} \
# va barcha sonlar yigindisi {sum(number1)} ga teng")
# num = max(number1) - min(number1)
# print(num)

""" FOR """
# ismlar = ["Ali","Vali","Hasan","Olim"]
# print(ismlar)
# for ism in ismlar:
#     print(f"Salom {ism} sini 31-yanvar yangi yil bayramiga taklif qilamiz \
#     Hurmat bilan spc jamoasi")
""" for va sonlar"""
# for son in range(1,10):
#     print(f" {son} ning kvadrati {son**2} ga teng")
    
# son = int(input("Oila azolaringizni soni kiriting: "))
# oila = [] 
# for n in range(son):
#     azo = input(f" {n+1} - azoyizni ismni kiriting: ")
#     oila.append(azo)
#     print(oila)
      
# son = int(input(" gruh azolarini sonini kiriting: "))
# gruh = []
# for n in range(son):
#     azo = input(f" {n+1}-ning ismini kiriting: ")
#     gruh.append(azo)
#     print(gruh)
"""if - elif-else """
# ismlar = ["Ali","Vali","Hasan","Olim"]
# for ism in ismlar:
#     if ism == "Ali":
#         print(f" Salom {ism} Admin sizga xabar bor ")
#     else:
#         print(f" salom {ism}")
# ismlar = ["Ali","Vali","Hasan","Olim"]
# for ism in ismlar:
#     if ism == "Vali":
#         print(f"{ism} kelmadimi? ")
#     else:
#         print(f"Salom {ism}")

"""elif"""
# sonlar = [1,2,3,4,5,6,7,8,9,10]
# for son in sonlar:
#     if son < 5:
#         print(f"{son} 5 dan katta")
#     elif son == 5:
#         print(f"{son} 5 ga teng")
#     else:
#         print(f"{son} dan kichik")
# sonlar = [1,2,3,4,5,6,7,8,9,10]
# for son in sonlar:
#     if son < 5 or son > 5:
#         print(f"{son} son 5 ga teng emas")
#     else:
#         print(f"{son} son 5 ga teng")
""" baxo chiqarish"""
# son = int(input("Alining baxosini kirirting: "))
# if son > 1 and son < 4:
#     print(f"{son} qoniqarsiz baxo")
# elif son > 3  and son < 7:
#     print(f"{son} yaxshi baxo")
# elif son > 6 and son < 10:
#     print(f"{son} alo baxo")
""" son manfiy va musbat ekanini aniqlash"""
# son = int(input(" Istalgan son kiriting:"))
# if son > 0: 
#     print(f"bu son {son} musbat")
# # elif == 0:
# #     print(f"bu {son} 0 ga teng")
# else:
#     print(f"bu son {son} manfiy")
    
""" zoo"""
# yosh = int(input(" Siz necha yoshdasiz: "))
# if yosh > 1 and yosh < 100:
#     if yosh <= 7 and yosh >= 70:
#         narx = " bepul"
#     elif yosh >= 7 and yosh < 18:
#         narx = 5_000
#     elif yosh >= 18 and yosh < 70:
#         narx = 10_000
#     if narx == "bepul":
#         print(f" Sizga kirish {narx}")
#     else:
#         print(f"Sizga kirish {narx}")
# elif yosh > 100:
#     print(f"siz notogri son kiritingiz")
# else:
#     print(f"Musbat son kiriting")
"""qancha mahsult sotib olmoqchisiz"""
# fruits = ["apple","banana","grape","melon","peach"]
# no =[]
# buy = []
# print("Welcome to our shop")
# print(" There are following fruits our shop:",end=' ')
# question = int(input("How many fruits are you going to buy: "))
# for n in range(question):
#     fruit = input(f"{n+1} - enter fruits: ")
#     if fruit in fruits:
#         buy.append(fruit)
#     else:
#         no.append(fruit)
# print(f"There are not following our shop {no}")
# print(f"There are following our shop {buy}")
# print(f" xaridingiz uchun raxmat")
# """dictionary - lug'at"""
# mevalar = {
#     'Zafar' : "shaftoli",
#     'Madina' : "qovun",
#     'Mushtariy' : "bananan",
#     'Muhammadali' : "olma",
# }
# print(f"Zafarning sevimli mevasi {mevalar['Zafar']} ")
# print(f"Madinaning sevimli mevasi {mevalar['Madina']} ")
# print(f"Mushtariyning sevimli mevasi {mevalar['Mushtariy']} ")
# print(f"Muhammadalining sevimli mevasi {mevalar['Muhammadali']} ")

# """ Qiymat qo'shish"""
# mevalar['Dadam'] = "mandarin"
# print(mevalar)
# # mevalar['Nanam'] = input("Nanamning sevimli mevasi: ")
# # print(mevalar)

# """ Qiymatni o'zgartirish """
# mevalar['Zafar'] = ["nok"]
# mevalar['Nanam'] = ["uzum"]
# print(mevalar)

# """ Qiymatni o'chirish """
# del mevalar['Zafar']
# del mevalar['Nanam']
# print(mevalar)

# """ get metodi """
# mevalar['Sardor'] = "qaroli"
# print(mevalar.get("Zafar", "bunday key yo'q"))   

# """ items - metodi """
# print(mevalar.items())    
# for key, value in mevalar.items():
#     print(f"{key.title()} ning sevimli mevalasi {value.capitalize()}")     
# """ Lug'at(Dictionary) ro'yxatlar bilan ishlash """
# """ lug'at ichida lug'at """
# insonlar = {
#     "inson1" : {
#         'ism' : "Hasan",
#         'familya' : "Husanov",
#         't_yil' : "1992",
#         'kasb' : "sotuvchi",
#     },
#     "inson2" : {
#         'ism' : "Olim",
#         'familya' : "Aliyev",
#         't_yil' : "1990",
#         'kasb' : "o'qtuvchi",
#     },
#     "inson" : {
#         'ism' : "Valiyev",
#         'familya' : "Axmadov",
#         't_yil' : "1995",
#         'kasb' : "tikuvchi"
#     }
# }
# print(insonlar['inson1']['ism'])
# print(insonlar['inson1']['familya'])
# print(insonlar['inson1']['t_yil'])
# print(insonlar['inson1']['kasb'])
# print(f"Salom bu insoning ismi {insonlar['inson1']['ism']} \
#     familyasi {insonlar['inson1']['familya']} \
#         tug'ulgan yili insonlar['inson']['t_yil'] \
#         kasbi {insonlar['inson1']['kasb']}")
""" Lug'at ichida lug'at"""


