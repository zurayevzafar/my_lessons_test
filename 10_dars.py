"""Thame while sikl""" 
"""1"""
# son = 1
# while son < 100:
#     print(son)
#     son = son + 1
"""2"""
# x = 1
# s = 0
# while x < 20:
#     if x%2== 0:
#         s = s+x
#         print(x)
#     x = x + 1
# print(s)
"""3"""#abadiy sikl
# while True:
#     savol = input("son kiriting: ")
#     if savol != 'exit' and savol.isdigit():
#         print(int(savol)**2)
#     elif savol == 'exit':
#         break#siklni toxtatish uchun
#     else:
#         print("son kiriting")

# ishora = True       
# while True:# = while True -> abadiy sikl 
#     savol = input("Istalgan son kiriting (dasturni toxtatish uchun 'exit'\
#                 deb yozing): ")
#     if savol != 'exit':
#         ishora == False
#     else:
#         print("float(savol)**2")

# """continue""" # davom etrish / bu holatda 6 ni tashlab otib ketiladi
# sonlar = [1,2,3,4,5,6,7,8,9,10]
# for son in sonlar:
     # if son == 6:
        # continue # davom etrish / bu holatda 6 ni tashlab otib ketiladi
    # else:
    #     print(son, end=' ')

       
# """vazifa"""
#1
# kutubxona = []
# while True:
#     savol = input("yaxshi korgan kitoblarizni kiriting(dasturni toxtatish uchun 'exit'):")
#     for savol in kutubxona:
#         if savol == 'exit':
#             ishora == False
#         else:
#             print(str(savol))
"""muzey"""
# ishora = True
# while ishora:
#     yosh = input("Yoshingiz nechida(dasturni toxtatish uchun 'exit'ni yozing): ")
#     if yosh == 'exit':
#         if yosh >= 0 and yosh <=100:
#             if yosh <= 7:
#                  yosh >= 65:
#                 narx = 'bepul'
#         elif yosh == 7:
#             narx = 2_000
        # elif yosh >= 7 and yosh < 18:
        #     narx = 3_000
#         elif yosh >= 18 and yosh < 65:
#             narx = 10_000  
#         if narx == 'bepul':
#             print(f"Sizga kirish{narx}")
#         else:
#             print(f"sizga kirish {narx} so'm")
#     elif yosh > 100:
#         print(f"Siz xato son kiritingiz")
#     else:
#         print(f"Musbat son kiriting")
 

# print("kiritilgan sonning kvadratini qaytaruvchi dastur.\n")  
# while True:
#     savol = input("Musbat son kiriting (dasturni toxtatish uchun 'exit' deb yozing)")
#     if savol == 'exit':
#         break
#     elif int(savol) < 0:
#         continue
#     else:
#         kvadrat = (savol)**2 
#         print(f"{savol} ning kvadrati {kvadrat} ga teng")  
        
     
# mahsulotlar = {
#     'gosh': "10000",
#     'tuxum': "11000", 
#     'guruch': "9000",
#     'makaron': "12000",
#     'kartoshka': "13000", 
#     'sabzi': "15000",
#     'piyoz': "20000",
# }
# savatcha = []
# summ
# ishora = True
# while True: 
#     savol = input("mahsulotni sorang (dasturni toxtatish uchun 'exit'ni yozing) ")
#     if savol in mahsulotlar.keys():
#         savatcha.append(savol)
#     else:
#         print(f"Siz kiritgam mahsulot dokonimizda mavjut emas")
        
#     chiqish = input("yana mahsulot olasizmi (ha yoki yoq)") 
#     if chiqish == "ha":
#         continue
#     elif chiqish == "yoq":
#         break
#     print(f"")
     
# talaba = ['Ali','Muhammaali','Mushtariy']
# print(talaba)
# yangi_talaba = []
# yangi_talaba.append(talaba.pop(1))
# print(talaba)
# print(yangi_talaba)
# yangi_talaba.append(talaba.pop(0))
# print(yangi_talaba)
# talaba.remove('Ali')
# print(talaba)
# print(f"bizning oilada {len(talaba)} ta yashaydi")
# print(f"ular {talaba[0]},{talaba[1]},{talaba[2]}")
# for talabalar in talaba:
#     print(f"salom {talabalar} aholing yaxshimi")
# del talaba[1]
# print(talaba)
# son = list(range(1,30,2))
# print(son)
# sonlar = son[1:20]
# print(sonlar)
# davlatlar = ["kariya","Germaniya","Fransiya","Amerika"]
# davlatlar.reverse()
# print(davlatlar)
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)
# sonlar = [1,58,-65,54,852,-2,4789,14785,3654,-9658,25,14,78,65,-54,21]
# sonlar.sort()
# print(sonlar)
# # print(f"Bizning royxatimizdagi eng kichik son {min(sonlar)} va eng katta son {max(sonlar)}")
# # print(sum(sonlar))
# sonlar1 = max(sonlar)-min(sonlar)
# print(sonlar1)
# sonlar1 = max(sonlar)+min(sonlar)
# print(sonlar1)
# sonlar1 = max(sonlar)*min(sonlar)
# print(sonlar1)
# sonlar1 = max(sonlar)/min(sonlar)
# print(sonlar1)
# familyalar = ["Jorayev","Primova","Nurilloyeva","Nurilloyev"]
# ismlar = ["Zafar","Madina","Mushtariy","Muhammadali"]
# print(type(familyalar))
# print(type(ismlar))
# ismlar.append("Bilol")
# print(ismlar)
# familyalar.append("Yarashiv")
# print(familyalar)
# familyalar = list(familyalar)
# print(type(familyalar))
# for ism in ismlar:
#     if ism == "Zafar":
#         print(f"Salom {ism} admin, sizga yangi xabar bor")
#     else:
#         print(f"salom {ism}")
# sonlar = [1,2,3,4,5,6,7,8,9,10]
# for son in sonlar:
    # if son < 5:
    #     print(f"{son} 5 dan kichik")
    # elif son == 5:
    #     print(f"{son} 5 ga teng")
    # else:
    #     print(f"{son} 5 dan katta")
    # if son < 5 or son >5:
    #     print(f"{son} 5 ga teng emas")
# son = int(input("Zafarni baxosini kiriting "))
# for son in sonlar:
# if son >1 and son <4:
#     print("qoniqarli baxo")
# elif son >=4 and son <=7:
#     print("yaxshi baxo")
# elif son >= 7 and son <=10:
#     print("alo baxo")
# son = int(input("istalgan son kiriting "))  
# if son > 0:
#     print("{son} musbat")  
# elif son == 0:
#     print("{son} 0 ga teng")
# else:
#     print("{son} manfiy")          
# taomlar = {
#     'somsa':"10_000",
#     'manti':"8_000",
#     'shashlik':"12_000"
# }
# print(f"somsaning narxi {taomlar['manti']}")
# taomlar['manti'] = "11_000"
# print(taomlar)
# del taomlar['shashlik']
# print(taomlar)
# print(taomlar.get('qayish', 'bunday taom yoq'))
# print(taomlar.items())
# for key,value in taomlar.items():
#     print(f"{key.title()}ning narxi {value.upper()}")

