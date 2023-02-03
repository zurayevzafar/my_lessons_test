"""date:19.15.2022"""
# """thame: for operatori"""
# ismlar = ["Xayot","Farux","Farmon","Sardor"]
# print(F"salom, {ismlar[1]}")
# """for"""
# for ism in ismlar: #ismlar royxatini har bir ism(elemenlar) uchun
#     print(f"salom, {ism}") #ushbu kodni bajar
#     print(f"aholaring yaxshimi")

# mehmon = ["Xayot","Farux","Farmon","Sardor"]
# for royxatlar in mehmon:
#     print(f"Salom,{royxatlar} sizni bugungi futbolga taklif qilamiz")
#     print(f"{royxatlar} Hurmat bilan Zafar")

# """for"""
# for son in range(1,20):
#     print(f"{son} ning kvadrati {son**2} ga teng")

# # foydalanuvchidan oila azolarining ismini soraymiz
# son = int(input("oila azolaringiz sonini kiriting: "))
# oila = [] # bosh royxat yaratib olammiz
# # # foydalanuvchidan oila azolarini sonicha savol soraymiz
# for n in range(son):
# #     # oila azosining ismini olamiz
#     azo = input(f"{n+1}-azoyingiz ismini kiriting" )
#     oila.append(azo) #qabul qilingan ismni royxatga qo'shamiz
# #     print(oila) 

# print("sizning oila azolaringiz: ", end=' ')
# for ism in oila:
#     if ism != oila[-1]:
#         print(f"{ism.title()}", end=', ')
# print(f"{oila[-1].title}.")

# son = int(input("sonini soraymiz: "))
# dostlar = []
# for n in range(son):  
#     azo = input(f"{n+1}-dostlar ismini kiriting")
#     dostlar.append(azo)
# dostlar.sort()
# print(dostlar)
# print("sizning dostlaringiz: ", end=' ')
# for son in dostlar:
#     if son != dostlar[-1]:
#         print(f"{son.title()}", end=', ')
# print(f"{dostlar[-1].title()}.")

"""vazifa"""
# #1
# ismlar = ["Zafar","Bobur","Sardor","Elyor","Ramazon"]
# for ism in ismlar:
#     print(f"asalom, {ism} mening do'stlarim")
#     print(f"hurmat bilan kamina")
# print(f"{len(ismlar)}")
 
#2
# for sonlar in range(10,100,2):
#         print(f"{sonlar} ning kubi {sonlar**3} ga teng")


# son = int(input("kinolar soni kiriting" ))
# kinolar = []
# for n in range(son):
#     nomi = input(f"{n+1}-kinolar nomini kiriting" )
#     kinolar.append(nomi)
#     # print(kinolar)
#     print("kinonig nimi: ", end=' ')
# for son in kinolar:
#     if son != kinolar[-1]:
#         print(f"{son.title()}", end=', ')
# print(f"{kinolar[-1].title()}.")
# 4
# kishi = int(input("nechita odam bilan uchrashgiz" ))
# insonlar = []
# for n in range(kishi):
#     nomi = input(f"{n+1}-insoning nomini yozing" )  
#     insonlar.append(nomi)

# print("insonlar", end=', ') 
# for kishi in insonlar:
#     if kishi != insonlar[-1]:
#         print(f"{kishi.capitalize()}", end=', ') 
# print(f"{insonlar[-1].title()}" )  
         
    
