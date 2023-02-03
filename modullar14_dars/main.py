"""funksiyaga ro'yxat uzatish"""
# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# talabalar = ['Ali', 'Vali', 'Hasan','husan']
# baholar = bahola(talabalar)
# print(baholar)

""" *args usuli """ # *args - arguments
# def summa(*sonlar):
#     """Kiritilgan sonlarni yig'indisini hisoblovchi funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son

#     return yigindi 
# print(summa(1,2,3,4,5,6,7,8,9))
# print(summa(-7,0,8))
# print(summa(23))

""" **kvars usuli""" # **kwars ---> keyword arguments (kalit sozlari argumentlar)
""" Agar funksiya kalit soz - qiymat korinishdagi argumentlar uzatish talab qilinsa, 
va bunday parametrlar soni nomalum bolsa, argument oldiddan ikkita yulduzcha qoyiladi (**kwars)"""

# def info(ism, familya, **malumotlar):
#     """ Inson haqidagi malumotlarni lugat korinishda qaytaradigan funksiya"""
#     malumotlar['ism'] = ism
#     malumotlar ['familya'] = familya
#     return malumotlar
# inson1 = info("Akbarali", "Olimov")
# inson2 = info("hasan", "Abdullayev", yosh=34, kasbi="haydovchi")
# print(inson1)
# print(inson2)

""" Modullar"""
# from funksiyalar import bahola
# from yordamchi_funksiyalar.y_funksiyalar import summa
# from yordamchi_funksiyalar.y_funksiyalar import summa as yig
# """bahola"""
# talabalar = ['ali','vali','hasan','husan']
# baholar = bahola(talabalar)
# print(baholar)

"""summa"""
# print(summa(1,2,3,4,5,6,7,8,9))
# print(summa(-7,0,8))
# print(summa(23))


# print(yig(1,2,3,4,5,6,7,8,9))
# print(yig(-7,0,8))
# print(yig(23))

# from math import pi
# uzunlik = lambda pi, r : 2*pi*r
# #             argument : ifoda"""
# print(uzunlik(pi,10))

# """ 2 Istalgan songa 10 ni qoshuvchi funksiya"""
# x = lambda a : a+10
# print(x(9))

""" 3 a va b ni kopaytmasini qaytaradigan funksiya"""
# x = lambda a, b, c : a+b*c
# print(x(5,6,2))

# x = lambda a, b : a*b
# print(x(5,6))

""" 4 Sonni istalgan songa kopaytiruvchi funksiya"""
# def myfunc(n):
#     return lambda a : a * n
# ikkiga = myfunc(2) #2
# uchga = myfunc(3)
# tortga = myfunc(4)

# print(ikkiga(10))
# print(uchga(15))
# print(tortga(20))
# from funksiyalar import bahola
# from yordamchi_funksiyalar.y_funksiyalar import summa
# from yordamchi_funksiyalar.y_funksiyalar import summa as yig
""""vazifa"""
#1
# from yordamchi_funksiyalar.password.y_password import aylana_info
# aylana1 = aylana_info("10","20","12","30")
# aylanalar = [aylana1]
# print("aylana haqida malumot")
# for aylana in aylanalar:
#     print(f"{aylana['radusi']} {aylana['diametr']}. {aylana['peremetr']} \
#      {aylana['yuzi']} ")