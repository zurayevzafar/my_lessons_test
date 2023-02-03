"""if - else"""
# ismlar = ["Bobur","Farrux","Hasan","Javlon"]
# for ism in ismlar: # == -> teng bo'lsa,tengmi?
#     if ism =='Bobur':#if - agar / agar ism aloi ga tenga bolsa
#         print(f"Salom {ism} admin, sizga yangi xabar bor",)
#     else: # else -yoki , boshqa barcha hollarda
#         print(f"salom {ism}")

# ismlar = ["Bobur","Farrux","Hasan","Javlon"]
# for ism in ismlar: # == -> teng bo'lsa,tengmi?
#     if ism !='Farrux':# teng bo'lmasa
#         print(f"Salom {ism} Farrux kelodimi?")
#     else: # else -yoki , boshqa barcha hollarda
#         print(f"salom {ism}")

# sonlar =  [1,2,3,4,5,6,7,8,9,10]
# for son in sonlar:
#     if son < 5 : #agar son dan kichik bo'lsa 
#         print(f"{son} dan kichik")
#     elif son == 5: # yoki 5 ga teng bolsa / elifni istalganch ishlatish mn
#         print(f"{son} 5 ga teng")
#     else: # qolgan barcha hollarda
#         print(f"{son} 5 dan katta")
        
#    """
#     == -> teng bo'lsa
#     != -> teng bo'lsamasa
#     > -> katta bo'lsa
#     < kichik bo'lsa
#     >= -> katta yoki teng bo'lsa
#     <= -> kichik yoki teng bo'lsa
#     and -> va
#     or => yoki
#     """
# for son in sonlar:
#     if son < 5 or son > 5: #agar son 5 ga teng yoki son 5 dan katta bolsa
#         print(f"{son} 5 ga teng emas")
# son = [1,2,3,4,5,6,7,8,9,10]
# son = int(input("Alining bahosini kiriting"))
# if son > 1 and son < 4:
#     print("qoniqarli")
# elif son >= 4 and son <=7:
#     print("yaxsh")
# elif son >= 8 and son <=10:
#     print("alo")

# son = int(input("Istalgan son kiriting: "))
# if son > 0:
#     print(f"{son} musbat")
# elif son == 0:
#     print(f"{son} 0 ga teng") 
# elif son < 0:
#     print(f"{son} manfiy")

"""zoo"""
# yosh = int(input("Yoshingiz nechida: "))
# if yosh >= 1 and yosh <=100:
#     if yosh <= 7 or yosh >= 70:
#         narx = 'bepul'
#     elif yosh >= 7 and yosh < 18:
#         narx = 5_000
#     elif yosh >= 18 and yosh < 70:
#         narx = 10_000  
#     if narx == 'bepul':
#         print(f"Sizga kirish{narx}")
#     else:
#         print(f"sizga kirish {narx} so'm")
# elif yosh > 100:
#     print(f"Siz xato son kiritingiz")
# else:
#     print(f"Musbat son kiriting")

# """vazifa"""
# print(f"Asalomu aleykum UITC Academyasida xush kelibsiz! \nBizning Academyada quyidagi kurslar mavjud: Fronted, Backend, Java ")
# savol = input("siz qaysi kursni tanlaysiz: ")
# if savol == "Backend":
#     narx = 500_000
# elif savol == "Fronted":
#     narx = 600_000
# p rint(f"siz tanlagan kurs {narx} so'm: ")    

# #2
# mahsulotlar = ["anor", "olma", "non", "shakar", "tuz", "qaymoq"]
# xarid = []
# yoq = []
# print(f"Assalomu aleykum do'konimizga xush kelibsiz !")
# print("Bizda quyidagi mahsulotlar bor:", end=' ')
# for mahsulot in mahsulotlar:
#     print(f"{mahsulot}", end=' ')
    
# savol = int(input("nechita mahsulot sotib olmoqchisiz?: "))
# for n in range(savol):
#     meva = input(f"{n+1}-mahsulotni kiriting: ")
#     if meva in mahsulotlar:
#         xarid.append(meva)
#     else:
#         yoq.append(meva)
# print(f"Bizda yoq mahsulotlar: {yoq}")
# print(f"Bizda bor mahsulotlar: {xarid}")

# #
# print("Asssalomu aleykum Academyamizga xush kelibsiz !")
# print("Bizning Academyamizda quyidagi kurslar mavjud: \nFrontend \nBackend \nGrafik dizayn \n3D modeling")
# savol = input("Siz qaysi kursni tanlaysiz ?").lower()
# narx=0
# xato=''
# if savol == 'frontend':
#     narx == 500_000
# elif savol == 'grafik dizayn' or savol == '3D modeling':
#     narx == 550_000
# elif savol == 'backend':
#     narx == 600_000
# else:
#     xato = "Bizda bunday kurs yoq iltimos togri yozing" 
    
# if narx:
#      print(f"{savol.title()} kursning narxi {narx} som")
# elif xato:
#     print(f"{xato}")

# parol1 = input("Iltimos parolni yarating(eng kamida 8 ta belgidan): ")
# parol2 = input("Iltimos parolni parolni tastiqlang: ")
# permit = 0
# if parol1 == parol2 and len(parol1) >= 8:
#     print("Parol muvaqiyarli yaratildi")
#     permit = 1
# else:
#     if len(parol1) < 8:
#         print("Iltimos eng kamida 8 ta belgidan iborat parol kiriting")
#     else:
#         print("xato; parolar mos kelmadi")
        
# if permit == 1:
#     parol3 = input("Tizimga kirish uchun parolingizni kiriting: " )
#     if parol1 == parol3:
#         print("Xato; parol mos kelmadi")
    
# if permit == 1:
#     parol3 = input("tizimga kirish uchun parolingizni kiriting: ")
#     if parol1 == parol3:
#         print("Tizimga xush kelibsiz")
#     else:
#         print("Xato; parol xato kiritildi")

# sonlar = [-2, 5, 7.1]
# for n in sonlar:
#     if n > 0:
#         print(f"{n} ning kubi: {n**3}")      

  









 