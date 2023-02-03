""" Thame: try - except """
# try:
#     son = int(input(" Son kirirting: "))
#     print(f"{son} ning kvadrati {son**2} ga teng")
# except:
#     print(f" Siz son kiritmadingiz")
# print(f"Dasturning davomi")

""" 
try - sizga xatolarni tekshirishga imkon beradi
except - sizga xatoni hal qishiga, va uning o'rniga boshqa ma'lumotni chiqishiga imkon beradi
else - xato bo'lmaganda bajarishga imkon beradi"""

# print(x)
# print("Hello words")

""" try """
# try:
#     print(x)
# except:
#     print(f"try-except yordamida, xatolik yuzaga kelganda va dastur to'xtab qolmaydi.")
# print("Hello words")

""" bir nechita except xato turlari """
# x = 5 
# y = 0
# print(x/y)

# x = 5
# y = 0

# try:
#     z = x/y
# except ZeroDivisionError:
#     print("Sonni nolga bo'lib bolmaydi")
# except NameError:
#     print(" 'x' degan ozgaruvchi topilmadi")
# except:
#     print("Bu yerda xoto matni topilmadi")
"""
Pythondagi barcha xatolik turlari 👇👇👇
https://www.tutorialsteacher.com/python/error-types-in-python

AssertionError -     Assert bayonoti bajarilmaganda ko'tariladi.
AttributeError -     Atribut tayinlashda ko'tarildi yoki mos yozuvlar bajarilmadi.
EOFError -   Input() funksiyasi faylning oxiri holatiga tushganda ko'tariladi.
FloatingPointError -     Suzuvchi nuqta operatsiyasi bajarilmaganda ko'tariladi.
GeneratorExit -  Jeneratorning close() usuli chaqirilganda ko'tariladi.
Import -     xatosi Import qilingan modul topilmaganda ko'tariladi.
IndexError -     Ketma-ketlik indeksi diapazondan tashqarida bo'lganda ko'tariladi.
KeyError -   Kalit lug'atda topilmasa ko'tariladi.
KeyboardInterrupt -  Foydalanuvchi uzilish tugmachasini bosganda ko'tariladi (Ctrl+c yoki o'chirish).
MemoryError -    Operatsiya xotirasi tugashi bilan ko'tariladi.
NameError -  O'zgaruvchi mahalliy yoki global miqyosda topilmasa ko'tariladi.
NotImplementedError -    Mavhum usullar bilan ko'tarilgan.
OSError -    Tizim ishi tizim bilan bog'liq xatolikka sabab bo'lganda ko'tariladi.
OverflowError -  Arifmetik amal natijasi koʻrsatish uchun juda katta boʻlganda koʻtariladi.
ReferenceError -     Axlat yig'ilgan referentga kirish uchun zaif havola proksi-serverdan foydalanilganda ko'tariladi.
RuntimeError -   Xato boshqa toifaga kirmasa ko'tariladi.
StopIteration -  iterator tomonidan qaytariladigan boshqa element yo'qligini bildirish uchun keyingi() funktsiyasi tomonidan ko'tariladi.
SyntaxError -    Sintaksis xatosiga duch kelganda tahlilchi tomonidan ko'tariladi.
IndentationError -   Noto'g'ri chiziq mavjud bo'lganda ko'tariladi.
TabError -   Qachonki chekinish mos kelmaydigan yorliqlar va bo'shliqlardan iborat bo'lsa ko'tariladi.
Tizim -  xatosi Tarjimon ichki xatoni aniqlaganida ko'tariladi.
SystemExit -     sys.exit() funksiyasi tomonidan ko'tarilgan.
TypeError -  Funktsiya yoki operatsiya noto'g'ri turdagi ob'ektga qo'llanilganda ko'tariladi.
UnboundLocalError -  Funksiya yoki usulda mahalliy o‘zgaruvchiga havola qilinganda ko‘tariladi, lekin bu o‘zgaruvchiga hech qanday qiymat bog‘lanmagan.
UnicodeError -   Unicode bilan bog'liq kodlash yoki dekodlash xatosi yuzaga kelganda ko'tariladi.
UnicodeEncodeError -     Kodlash paytida Unicode bilan bog'liq xatolik yuzaga kelganda ko'tariladi.
UnicodeDecodeError -     Unicode bilan bog'liq xato dekodlash vaqtida yuzaga kelganda ko'tariladi.
UnicodeTranslateError -  Unicode bilan bog'liq xato tarjima paytida yuzaga kelganda ko'tariladi.
ValueError -     Funktsiya to'g'ri turdagi, lekin noto'g'ri qiymatdagi argumentni olganida ko'tariladi.
ZeroDivisionError -  Bo'linish yoki modul operatsiyasining ikkinchi operandi nolga teng bo'lganda ko'tariladi.
"""

""" else - hech qanday xatolik yuzaga kelmasa ishlaydi """
# a = 5
# try:
#     print(a**2)
# except:
#     print("Bu yerda xato matn bo'lmadi")
# else:
#     print("Hech qanday xatolik yuzaga kelmaydi") # va hech qanday xatolik bo'lmasa 'else' ishlaydi

""" finally """
"try - blokida xattolik bo'ladimi yoqmi, qatiy nazar 'finally ' ishlatiladi"   
# a = 4
# b = 10
# try:
#     print(a+b)
# except:
#     print(" Error error error")
# finally:
#     print("'finally' doim ishlaydi")    

""" raise """
""" 'raise' xato matinni dasturga o'zimizni xoxlagan ko'rinishda  ko'rsatilganda imkon beradi"""
# a = 4
# b = 10
# try:
#     print(a+b)
# except NameError:
#     print("Name Error")
#     raise NameError("Name Error - berilgan nomdagi o'zgaruvchi topilmaganda yuzaga keladi")

""" 
try:
        Xatolik yuzaga kelishi mumkin bo'lgan blok
    
   """
# try:
#     son1 = int(input("1-sonni kiriting: "))
#     son2 = int(input("2-sonni kiriting: "))
#     if son1 > son2:
#         print(f"{son1} - {son2} dan katta")
#     elif son1 == son2:
#         print(f"{son1} - {son2} ga teng")
#     else:
#         print(f"{son2} - {son1} dan katta") 
# except ValueError:
#     print("valueError xatosi yuzaga kelishi mumkin")
# except:
#     print("siz son kiritmadingiz")

""" Vazifa """
"""Ushbu kodda yuzaga kelishi mumkin bo'lgan hatoliklarni 'try-except' yordamida oldini oling"""

"""1) Sonlar deb nomlangan ro'yhat tuzing ro'yhatda bir nechta sonlar va 0 ham bo'lsin.
    Keyin foydalanuvchidan biror son kiritishini so'rab, qabul qilingan sonni sonlar ro'yhatidagi 
    sonlarga bo'ling va natijani konsulga chiqaring.
    Dastur tuzishda 'try-except' dan foydalaning va yuzaga kelishi mumkin bo'lgan barcha xatoliklarni oldini oling !
"""
# try:
#     sonlar = [0,1,2,5,4,7,3,8]
#     son = int(input("Birorta son kiriting: "))
#     for x in sonlar:
#         print(x/son)
# except TypeError:
#     print("TypeError xatosi yuzaga kelish mumkin")
# except:
#     print("Siz matn kiritingiz") 

"""2) Foydalanuvchidan uning yoshini qabul qilib olib uni 0 dan 1,000 gacha bo'lgan sonlardan qaysilariga 
    qoldiqsiz bo'linnishini aniqlab, qoldiqsiz bo'linadigan sonlarni ro'yhatga saqlab konsulga chiqaring.
    Va bu dasturni funksiyaga joylang. Hamda uni yozishda 'try-except' dan foydalaning va yuzaga kelishi
    mumiin bo'lgan xatoliklarni oldini oling
""" 

# def bolinishi():
#     royxat = []
#     try:
#         son = int(input("Yoshingizni kiriting: "))
#         for n in range(0,1000):
#             if n % son == 0:
#                 royxat.append(n)
#     except:
#         print(f"bu yerda xatolik bor")
#     for x in royxat:
#         print(x, end=' ')
#     return royxat
# bolinishi()
    
"""3) To'g'ri burchakli uchburchakning gipotenuzasini hisoblash. Ushbu kodda yuzaga kelishi mumkin bo'lgan hatoliklarni
'try-except' yordamida oldini oling """
# try: 
#     a = int(input("Birinchi katetni kiriting: "))
#     b = int(input("Ikkinchi katetni kiriting: "))
#     c=a**2+b**2
#     import math
#     c = round(math.sqrt(a**2+b**2),2)
#     print(f"Katetlari {a} va {b} ga teng bo'lgan uchburchakning giputenuzasi {c} ga teng")
# except TypeError:
#     print(f"TypeError xatosi yuzaga kelishi mumkin")
# except:
#     print(f"Siz matn kiritdingiz")
    
"""4) mevalar deb nomlangan ro'yhat(list ) yarating. Avval uni o'zgarmas ro'yhat turiga ,
keyin esa set turiga o'zgartiring va konsulga ularning turini chiqaring.
  -remove() yordamida 3 ta discard() yordamida 3 ta elementni o'chirib tashlang va 
  ro'yhatni konsulga chiqaring.
  -va yangi 5 ta element qo'shing va ro'yhatni konsulga chiqaring;
  -so'ngra ro'yhatni tozalang va uni konsulga chiqaring;
  -keyin esa ro'yhatni o'chirib tashlang;
"""
"""Ushbu kodda yuzaga kelishi mumkin bo'lgan hatoliklarni 'try-except' yordamida oldini oling"""
# try: 
#     fruits = ["apple","banana","grape","peach","mandarin","pear","melon","pomegranate"]
#     fruits = tuple(fruits)
#     print(fruits)
#     fruits = set(fruits)
#     print(fruits)
#     fruits.remove("apple")
#     fruits.remove("banana")
#     fruits.remove("grape")
#     print(fruits)
#     fruits.discard("pomegranate")
#     fruits.discard("melon")
#     fruits.discard("pear")
#     print(fruits)
#     fruits.add("cherry")
#     fruits.add("strawberry")
#     fruits.add("lemon")
#     fruits.add("plum")
#     fruits.add("rice")
#     print(fruits)
#     fruits.clear()
#     print(fruits)
#     del fruits
#     print(fruits)
# except NameError:
#     print(f"NameError xatolik ko'rsatadi")
# except:
#     print(f"Boshqa xatoliklarni ko'rsatishi mumkin")