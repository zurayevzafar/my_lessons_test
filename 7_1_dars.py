""" Thame: Operators and Boolens /  Operatoralar"""
""" Boollen / mantiqiy qiymatlar"""
""" Mantiqiy qiymatlarning ikkita turi mavjud true  va False
Ikki qiymat solishtirilganda, ifoda baholanadi Python qiymat javobini qaytaradi.
True/False bilan teng kuch bilan 1/0 ham ishlatiladi."""

# print(5>10) #False
# print(5==10) #False
# print(5<10) #True
""" if-else"""
# a = 17 
# b = 14
# if a > b:
#     print(f"{a} {b} dan katta")
# else:
#     print(f"{b} {a} dan kichik")
  
""" bool() funksiyasi"""
""" bool() fumksiyasi har qanday qiymatni baholashga imkon beradi bizga 
True va False javobini qaytaradi"""
# matn = ""
# son = -9
# print(bool(matn))  
# print(bool(son))  

# x= "salom"
# y = 17
# print(bool(x)) # o'zgaruvchi sifatioda
# print(bool(y)) # o'agaruvchi sifatioda

# yosh = input("Yoshigiz kiriting: ")
# if bool(yosh):
#     print(yosh)
# else:
#     print(f"Siz hech nima kiritmadingiz!!!")

""" Deyarli har qanday qiymat, agar u bo'sh bo'lmasa --> True
bo'sh matndan tashqari har qanday matn --> True
Har qanday raqam, agar u 0 bo'lmasa --> True
Har qanday tuple, List, set va dictionary, agar u bo'sh bo'lanadsa --> True"""

# print(bool(" Asalomu aleykum"))
# print(bool(" 123"))
# print(bool(["Ali", "vali","hasan"]))
# print(bool({23,"ism","daraxt"}))

# print(bool(""))
# print(bool(0))
# print(bool([]))
# print(bool({}))

""" Masalan """
# ism = input("Ismingizni kiriting: ")
# if bool(ism):
#     print(ism)
# else:
#     print(f"Siz hech nima kiritmadingiz.")

""" Operarators / operatorlar"""
""" operatolar o'zgaruvchilar va qiymatlar ustida amallarni bajarish uchun ishlatiladi.

"""
""" Arifmetik Operatotlar
+ Qo'shish x+y
- ayirish x-y
* kopaytirish x-y
** Datrajaga ko'tarish x+y
/ Bo'lish x+y
// Yaxlidlab bo;lish x+y
%  Qoldiqli bolish X  %  y
"""

# a = 15
# b = 7
# print(a//b)

""" Belgilash Operatori
=   x = 5   x = 5
+=   x += 5   x = x + 5
-=   x -= 5   x = x - 5
*=   x *= 5   x = x * 5
/=   x /= 5   x = x / 5
//=   x //= 5   x = x // 5
**=   x **= 5   x = x ** 5
%=   x %= 5   x = x % 5
"""

# x = 5
# x **= 3 # x = x**3
# print(x)

# x = 4
# x //= 3 # x = x//3
# print(x)

""" taqoslash Operatorlari 
== Tengmi           x == y
!= Teng emasmi      x != y
> katta             x > y
< Kichik            x < y
>= Katta yoki teng  x >= y
<= kichik yoki teng x <= y
"""
# a = 3
# b = 4
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)

""" Mnatiqiy operatorlar
and  Ikkala shart to'g'ri bo'lsa            x < 5 and x < 10
or  Ikkala shartdan biri to'g'ri bo'lsa     x < 10 and x < 5
not Inkor. Ikkala shart to'g'ri bo'lsa      not(x < 5 and x < 10)
"""
# x = 5
# print(x > 3 and x < 10 )
# print(x < 7 or x < 4 )
# print(not(x < 5 and x < 10 ))

""" Identifikatsiya operatorlari
is         agar ikkala o'zgaruvchi ham bir xil o'bekt bo'lsa     True
is not    agar ikkala o'zgaruvchi ham bir xil o'bekt bo'lsa !   True
"""
# x = ["apple","banana"]
# y = ["apple","banana"]
# z = x
# print(x is z) # True > chunki x ning obektlari z niki bilan bir xil joylashuvi ham bir xil
# print(x is y) # False > chunki x ning obektlari z niki bilan bir xil ammo joylashuvi ham bir xil emas !
# print(x == y) # "is" va "==  o'rtasida farqni ko'rsatish uchun: bu taqoslash True qaytaradi, chunki x y ga teng

""" A'zolik Operatorlari
in agar "x" "y" ni ichida bo'lsa           True
not in agar "x" "y" ni ichida bo'lsmasa    True
"""
# y = ["olma","gilos","anor"]
# print("olma" in y)
# print("shaftoli" not in y)

""" vazifa """ 
""" Arfmetik Operatorlar """
# x = 5
# y = 4
# print(x+y) # qo'shish
# print(x-y) # ayirish
# print(x*y) # ko'paytirish
# print(x/y) # bo'lish
# print(x**y) # darajaga ko'tarish
# print(x//y) # yaxlitlab bo'lish
# print(x%y) # qoldiqlab bo'lish

""" Belgilash Operatori"""
# x = 7
# x = x + 3
# print(x)
# x = x - 3
# print(x)
# x = x / 3
# print(x)
# x = x * 3
# print(x)
# x = x // 3
# print(x)
# x = x % 3
# print(x)

""" taqoslash Operatori """
# a = 5
# b = 6
# print(a > b)
# print(a < b)
# print(a == b)
# print(a <= b)
# print(a >= b)
# print(a != b)

""" Mantiqiy Operatorlar """
# a = 4
# print(a > 3 and a < 8)
# print(a > 5 or a < 8)
# print(not(a > 5 or a < 3))

""" Identifikatsiya Operatorlar """
# a = ["qovun","sut"]
# b = ["qovun","sut"]
# z = a
# print(a is z)
# print(a is b)

""" Azolik operatori """
# b = ["olma","qaroli","tarvuz"]
# print("tarvuz" in b)
# print("qaroli" not in b)










