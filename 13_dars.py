""" Thame    funksiya """
# """funksiyadan qiymat qaytarish"""
# def full_name(name, surname):
#     """to'liq ism qaytaradigan funksiya"""
#     name = f"{name.title()} {surname.title()}"
#     return name #qiymat qaytarish uchun return operatorini ishlatamiz

# """funksiyani return operatori yordamida full_name degan o'zgaruvchining qiymatini qaytarish uchun return operatorini ishlatamiz"""
# person1 = full_name("Ali", "Olimov")
# person2 = full_name("Aziza", "Sanoyeva")
# print(person1)
# print(person2)

# """Funksiya lug'at qaytarish"""
# def person_info(name, surname, birth, gender, age, job=None):
#     """inson haqidagi ma'lumotlarni qytaruvch funsiya"""
#     person = {
#         'name' : name,
#         'surname' : surname,
#         'birth' : birth,
#         'gender' : gender,
#         'age' : age,
#         'job' : job
#     }
#     return person

# """ 'job' nomli parametirga 'None' stardart qiymat berib ketdik.
# None Pythonda mavjud emas ma'nosini beradi va if yordamida tekshirilganda 
# false mantiqiy qiymat qaytaradi"""

# person1 = person_info("Olimjon", "Voliyev","1998", "erkak","25","quruvchi")
# person2 = person_info("Ahmad", "Abbosov","1987","erkak","34") 
# insonlar = (person1,person2) 

# """1-usul"""
# print("Insonlar haqida ma'lumotlar: ")
# for inson in insonlar:
#     print(f"{inson['name']} {inson['surname']}. {inson['birth']}-yilda tug'ulgan,\
#     hozirda {inson['age']} yoshda. jinsi {inson['gender']} \ kasbi {inson['job']}")

# """2-usul"""
# print("Insonlar haqida ma'lumotlar")
# for inson in insonlar:
#     if inson['job']:
#         job = inson['job']
#     else:
#         job = "nomalum"
#     print(f"{inson['name']} {inson['surname']}. {inson['birth']}-yilda tug'ulgan,\
#     hozirda {inson['age']} yoshda. jinsi {inson['gender']} \ kasbi {inson['job']}")
      
# """Funksiyadan ro'yxat qaytarish"""
# def oila(n):
#     """Oila azolarining ismini ro'yxat holatida qaytaruvchi funksiya"""
#     oila = []
#     for i in range(n):
#         azo = input(f"{i+1}- oila azongizning ismi : ")
#         oila.append(azo)
#     return oila
# oila1 = oila(4)
# oila2 = oila(7)
# oila3 = oila(3) 
# print(oila1)     
# print(oila2)
# print(oila3)

# """ Funksiyani tsiklda ishlatish"""
# def avto_info(kompaniya, madel, rangi, karobka, yili, narhi=None):
#     avto = {'kompaniya' : kompaniya,
#             'madel' : madel,
#             'rangi' : rangi,
#             'karobka' : karobka,
#             'yili' : yili,
#             'narhi' : narhi}
#     return avto
# print("Saytimizdagi avtolar royxatini shakillantiramiz")
# avtolar= []
# while True:
#     print("\n Quyidagi ma'lumotlarni kriting: ",end='')
#     kompaniya=input("\n ishlab chiqaruvchi: ")
#     madel=input("Madeli: ")
#     rangi=input("Rangi: ")
#     karobka=input("Karobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
    # foydalanuvchi kiritgan ma'lumotlardan avto+info yordamida 
    # lug'at shakilantirib , har bir lug'atni ro'yxatga qo'shamiz:
    # avtolar.append(avto_info(kompaniya,madel, rangi, karobka, yili, narhi))
    # yana avto qo'shish qo'shmaslikni so'raymiz
    # javob = input("Yana avto qo'shasizmi? (yes/no: ")
    # if javob=='no':
    #     break
    
# print('Onlayin bozordagi mavjud avto mashinalar: ')
# for avto in avtolar:
#     if avto['narhi']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['kampaniya']} {avto['rangi']} {avto['madel']} .narh:{narh}")

""" Pass operatori"""
"""pass - operatori malum vaqt funksiyasini ishlatmaslik kerak bolganda kerak boladi """

# def name(ism):
#     pass 
# name("Abbos")
# def name(ism):
#     pass

"""vazifa"""
"""1) Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va 
    telefon raqamini qabul qilib, lug'at ko'rinishida malumot qaytaruvchi funksiya yozing. 
    Lug'atda foydalanuvchi yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy 
    qiling (masalan, tel.raqam, el.manzil)

"""
""" Funksiyadan lugat  qaytarish"""
# def inson_info(ism, familya, tugulgan_yili, tugulgan_joyi, \
#     email_manzili, telefon_raqami, yoshi=None ):
#     """ Inson haqidagi malumotlarni qaytaruvchi funksiya"""
#     inson = {
#         'ism' : ism,
#         'familya' : familya,
#         'tugulgan_yili' : tugulgan_yili,
#         'tugulgan_joyi' : tugulgan_joyi, 
#         'email_manzili' : email_manzili,
#         'telefon_raqami' : telefon_raqami,
#         'yoshi' : yoshi
#     }
#     return inson
# inson1 = inson_info("Mamur", "Izbosarov","1995","Buxoro","WWWWW","94 151 22 77","30" )
# inson2 = inson_info("Zarif", "Boboyev","1999","Namangan","SSSSSS","94 222 33 88",)
# insonlar = [inson1, inson2]
# # """1-usul"""
# for inson in insonlar:
#     print(f"{inson['ism']} {inson['familya']}. {inson['tugulgan_yili']}-yilda tugulgan \
# {inson['tugulgan_joyi']}da tugulgan {inson['email_manzili']} \
# {inson['telefon_raqami']} {inson['yoshi']}")
# # """2-usul"""
# print(f"Insonlar haqida malumotlar: ")
# for inson in insonlar:
#     if inson['yoshi']:
#         yoshi = inson['yoshi']
#     else:
#         yoshi = "nomalum"
#     print(f"{inson['ism']} {inson['familya']}. {inson['tugulgan_yili']}-yilda tugulgan \
#     {inson['tugulgan_joyi']}da tugulgan {inson['email_manzili']} \
#     {inson['telefon_raqami']} {yoshi}")

"""2) Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan 
    ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.
"""
""" Funksiyadan lugat  qaytarish"""
# def inson_info(ism, familya, tugulgan_yili, tugulgan_joyi, \
#     email_manzili, telefon_raqami, yoshi=None ):
#     """ Inson haqidagi malumotlarni qaytaruvchi funksiya"""
#     inson = {
#         'ism' : ism,
#         'familya' : familya,
#         'tugulgan_yili' : tugulgan_yili,
#         'tugulgan_joyi' : tugulgan_joyi, 
#         'email_manzili' : email_manzili,
#         'telefon_raqami' : telefon_raqami,
#         'yoshi' : yoshi
#     }
#     return inson
# print("insonlar haqidagi malumotlarni shaklantiramiz", end=' ')
# insonlar=[]
# while True:
#     ism = input("Ism: ")
#     familya = input("Familya: ")
#     tugulgan_yili = input("Tugulgan_yili: ")
#     tugulgan_joyi= input("Tugulgan_joyi: ")
#     email_manzili = input("Email_manzili: ")
#     telefon_raqami = input("Telafon_raqami: ")
#     yoshi = input("Yoshi: ")
#     # foydalanuvchi kiritgan malumotlardan inson_info yordamida
#     # lugat shakilantirib, har bir lugatni royxatga qoshamiz
#     insonlar.append(inson_info(ism, familya, tugulgan_yili, \
#     tugulgan_joyi, email_manzili, \
#     telefon_raqami, yoshi))
#     # yana  inson haqida malumot berishni soraymiz
#     javob = input("Yana insonlar haqida malumot qoshasizmi? (ha/yoq): ")
#     if javob== 'yoq':
#         break
    
# print("Elektron royxatda mavjut insonlar: ")
# for inson in insonlar:
#     if inson['yoshi']:
#         yoshi = inson['yoshi']
#     else:
#         yoshi = "Nomalum"
#     print(f"{inson['ism']} {inson['familya']}. {inson['tugulgan_yili']}-yilda tugulgan \
# {inson['tugulgan_joyi']}da tugulgan {inson['email_manzili']} \
# {inson['telefon_raqami']}.Yoshi:{yoshi}")   
    
"""3) Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
"""
""" Uchta son qabul qilib, ulardan eng kattasini kattasini qaytaruvchi funksiya yozing"""
# def katta_kichik():
#     """kiritilgan sonning eng kattasin korsatuvchi funksiya"""
#     son1 = int(input("1-sonni kiriting: "))          
#     son2 = int(input("2-sonni kiriting: "))          
#     son3 = int(input("3-sonni kiriting: "))   
#     if son1 > son2 and son1 > son3:
#         print(f"{son1}")
#     elif son2 > son1 and son2 > son3: 
#         print(f"{son2}")   
#     elif son3 > son1 and son3 > son2:
#         print(f"{son3}")
#     elif son1==son2==son3:
#         print("Sonlar teng")
#     else:
#         print("Sonlar 2 tasi teng") 
# katta_kichik()

"""4) Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, 
    perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing
"""
# def aylana_info(radusi,diametr,peremetr,yuzi):
#     aylana = {
#         'radusi' : radusi,
#         'diametr' : diametr,
#         'peremetr' : peremetr,
#         'yuzi' : yuzi        
#     }
#     return aylana
# aylana1 = aylana_info("10","20","12","30")
# aylanalar = [aylana1]
# print("aylana haqida malumot")
# for aylana in aylanalar:
#     print(f"{aylana['radusi']} {aylana['diametr']}. {aylana['peremetr']} \
#      {aylana['yuzi']} ")




















"""5) Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya 
 yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan 
    katta musbat sonlar)"""

"""6) Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi 
    sonlar ro'yxatni qaytaruvchi funksiya yozing.  
    Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan 
    ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 
    1 deb olinadi.  1, 1, 2, 3, 5, 8, 13, 21, 34, 55,... 
"""

               
               
               
               
               
               
               
               
               
               