"""date:2023-01-04"""
"""lug'lat ichida lug'at"""

# insonlar = {
#     "inson_1" : {
#         "ism" : "Ali",
#         "familya" : "Valiyev",
#         "t_yili" : "2000",
#         "kasbi" : "O'qtuvchi"
#     },
    
#     "inson_2" : {
#         "ism" : "Nodir",
#         "familya" : "Jo'rayev",
#         "t_yili" : "1992",
#         "kasbi" : "Haydovchi"
#     },
    
#     "inson_3" : {
#         "ism" : "Hasan",
#         "familya" : "Husanov",
#         "t_yili" : "1991",
#         "kasbi" : "shifokor"
#     }
# }

# print(insonlar["inson_1"]["ism"])
# print(insonlar["inson_1"]["kasbi"])

# print(f"salom bu inson {insonlar['inson_1']['ism']}) {insonlar['inson_1']['familya']}\
#           kasbi {insonlar['inson_1']['kasbi']}")

# qizlar = {
#     "anora" : ['atirgul','lola'],
#     "ezoza" : ['binavsha','moychechak'],
#     "dilshoda" : ['nastarin','chinnigul'],
#     "nigina" : ['kaktus','qizg\'aldoq']
# }

# print(qizlar['anora'[0]])
# print(qizlar['ezoza'[1]])
# print(qizlar['nigina'[0]])

# for key,value in qizlar.items():
#     print(f"\n{key.title()} quyidagi gullarni yoqtiradi: ", end=' ')
#     for v in value:
#         print(f"{v.title()}", end=' ')
    
"""vazifa"""
"""ro'yhat ichida ro'yhat"""
#1
# lg = ['X5' , 'Q7', 'X power 1']
# sumsung = ['S10' , 'A50' , 'A10S']
# telefonlar = [lg, sumsung]
# print(telefonlar[0][2])
# print(telefonlar[1][0])

#2
"""lug'at ichida lug'at"""
# oilalar = {
#     'oila1' : {
#         'ota': {
#             'ism':"Alijon",
#             'familya':"Mamajonov",
#             'yosh':"32",
#             'kasb':"Duradgor",
#                 },
#         'ona':{
#             'ism':"Munisa",
#             'familya':"Mamajonova",
#             'yosh':"30",
#             'kasb':"Tikuvchi",
#                 },
#         },
#     'oila2' : {
#         'akam':{
#             'ism':"Zufar",
#             'familya':"Jo'rayev",
#             'yosh':"30",
#             'kasb':"Usta",
#                 },
#         'apam': {
#             'ism':"Maqsuda",
#             'familya':"Inakova",
#             'yosh':"28",
#             'kasb':"Ishchi"
#             }
#         }
# }

# for key,value in oilalar.items():
#     print(f"         Mening {key} da")
#     for k,v in value.items():
#         print(f"Mening {k}")
#         for a,b in v.items():
#             print(f"    {a.upper()}-{b.title()}.")
            
#3
"""lug'at ichida  ro'yxat"""
# dostlar = {
#     'sinfdoshlar':{
#             'ali': ['hotdok','osh','norin'],
#             'anvar': ['lavash','shashlik','manti'],
#             'olim' : ['kabob','somsa','gumma']
#                   },
#     'kursdosh':{
#             'abbos':['lovya','mosh','guruch'],
#             'said':['pamidor','bodiring','piyoz'],
#             'alisher':['suc','cola','fanta']
#                 }
#             }            
# for key,value in dostlar.items():
#         print(f"\n Mening {key.title()}im ning yoqtiradigan taomlari:")
#         for k,v in value.items():
#             print(f"\n {k} {v}")
#             for x in v:
#                 print(f"x")
#4
"""royxat ichida lugat"""
# car_1 = {
#     'model':"S3",
#     'brend':"BMW",
#     'yil':"2021",
#     'narx':"23000",
# }
# car_2 = {
#     'model':"Nexia",
#     'brend':"CHevrolet",
#     'yil':"2019",
#     'narx':"10000",
# }
# cars = [car_1, car_2]
# print(cars[0]['model'])
# for car_1 in cars:
#     print(f"car_1: {car_1['model'].title()} {car_1['brend'].upper(),}"
#           f"car_1:{car_1['yil']}",
#           f"sotiladigan narxi:{car_1['narx'].title()}")
    