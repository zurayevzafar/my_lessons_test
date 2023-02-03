"""Thame: O'zgarmas ro'yxat(typle), set"""
"""Pythonda 4 turdagi malumotlar royxati mavjud:
list-royxat[]
tuple- Ozgarmas royxat()
set - Arlash royxat{}
Dictionary - lugatlar {}"""

"""Tuple -Ozgarmas ro'xatlar
Tuple o'zgarmas ro'yxatlarga element qo'shi bo'lmaydi 
ularni o'zgartirib yoki o'chirib bo'lmaydi.
tuple elementlari har qanday turdagi ma'lumotlarga ega bo'lishi mumkin:"""

# ismlar = ["Olim","Anvar","Rustam"]
# familyalar = ("Xasanov","Husanov","Abdullayev")
# print(type( ismlar))
# print(type(familyalar))
# ismlar.append("Aziz")
# print(ismlar)
# familyalar.append("Ismatov")# append ishlamaydi
# print(familyalar)

""" list(), tuple() funksiyalari"""
# print(type(familyalar))# tuple turdagi ro'xatni oddiy ro'yxatga o'tkazamiz
# familyalar = list(familyalar)
# print(type(familyalar))

# familyalar.append("Ismatov")# ro'yxatimizga yangi ro'yxat qo'shamiz
# print(familyalar)

# familyalar = tuple(familyalar) # list turdagi ro'yxatimizni o'zgarmas ro'yxat shakliga
# print(type(familyalar))

"""tuple yaratish"""
# meva = ("apple", "grape")
# print(type(meva))

# meva = ("apple")# tuple emas bitta bolganin uchun tuple ikki va undan ortiq elementlar jamlanmasi
# print(type(meva))

# """tuple ni o'chirish"""
# del meva
# print(meva)
#print(meva) bu xatolik keltirib chiqaradi, chunki endi "meva" degan ro'yxat yo'q

# """ tuple larni qo'shish"""
# tuple1 = ("a","b","c")
# tuple2 = (1,2,3)
# tuple3 = tuple1 + tuple2
# print(tuple3)
# tuple3 = tuple(tuple3)
# print(tuple3)

"""  set  """
""" Set tartibsiz , o'zgarmas va indekslanmagan to'plamdir.
Set elementlarin o'zgartirish mumkin emas, lekin elemenlarni olib tashlash va yangi qo'shish mumkin
Set tartibsiz, shuning uchun elementlar qaysi tartibda bo'lish aniq emas."""

# myset = {"apple","banana","cherry","lime","melom","orange"}# ikki ta birxil element prontga chiqmaydi
# print(myset)
# print(type(myset))

# """ set() funksiya """
# name = ("ali","vali","olim")
# print(name)
# print(type(name))

# name = set(name)
# print(name)
# print(type(name))

"""add() funksiya  (qo'shadi)""" 
# name = {"ali","vali","olim"}
# name.add("hasan")  
# print(name)

# """ elementni o'chirish.remove() va discard()"""
# name.remove("ali") # Agar o'chiriladigan element mavjud mo'lmasa remove() xato beradi
# print(name)

# name.discard("aziz") # discard() esa xato bermaydi
# print(name)

""" del va .clear"""
# name.clear()# clear bu tozalaydi
# print(name)

# del name # bu esa set ro'yxatini butunlay o'chirib tashlaydi
# print(name) # xatolik yuzaga keladi

""" Ikki set ni qo'shish / union(), update() funksiyalari"""
# name1 = {"Abbos","ahmad","Anvar"}
# name2 = {"Bobur","Baxrom"}

# name3 = name1.union(name2) # ikkita set ni qo'shib 3-yangi setni yaratadi
# print(name3)

# name1.update(name2)
# print(name1) # name1 ga name2 op kelib qo'shadi

# name2.update(name1)
# print(name2) # name2 ga name1 op kelib qo'shadi

""" vazifa """
"""1) oila deb nomlangan bo'sh o'zgarmas ro'yhatlarga(tuple) o'z oila azolaringizni ismini qo'shing
va konsulga chiqaring.com
  -so'ng oila azolarimizning 2 tasini ismini ro'yhatdan o'chirib tashalng va qolgan ismlarni konsulga 
  chiqaring;
  -keyin esa qolgan ismlarni tahrirlab ularni familyasini ham qo'shing --> "Ali" > "Olimov Ali" .
  va konsulga chiqaring;
  -so'ngra avval o'chirib yuborgan ismlaringizni qaytadan ro'yhatgfa qo'shing va ularni ham 
  konsulga chiqaring;
"""
# oila = ()
# print(type(oila))
# oila = list(oila)
# print(oila)

# oila.append("Zafar")
# oila.append("Muhammadali")
# oila.append("Mushtariy")
# oila.append("Sanjar")
# print(oila)

# oila.remove("Zafar")
# oila.remove("Muhammadali")
# print(oila)

# oila.insert(0,"Nurillayeva")
# oila.insert(2,"Jorayev")
# oila[0] = "Olimova Mushtariy"
# print(oila)

# oila.insert(4,"Zafar")
# oila.insert(5,"Muhammadali")
# print(oila)
# oila = tuple(oila)
# print(type(oila))

"""2) musbat_sonlar va manfiy_sonlar degan ikkita ro'yhat(list) yarating. so'ngra ularni birlashtirib yangi 'sonlar' deb nomlangan
  ro'yhat yarating.
  -so'ngra ushbu ro'yhatni o'zgarmas ro'yhat shakliga keltiring va konsulga shu ro'yhatni va uning turini chiqaring;
  -keyin shu ro'yhatni o'chirib tashlang va uni qaytadan konsulga chiqarishga urinib ko'ring;
"""
# musbat_sonlar = [2,5,4,7,8,25,65,1,4]
# manfiy_sonlar = [-3,-5,-9,-15,-98,-554]
# sonlar = musbat_sonlar + manfiy_sonlar
# print(sonlar)
# sonlar = tuple(sonlar)
# print(sonlar)
# # tupleni ochirish
# del sonlar
# print(sonlar)
 
"""3) ismlar deb nomlangan ro'yhat(list) va sonlar deb nomlangan o'zgarmas(tuple) ro'yhat yarating va ularni avval har birini keyin esa 
  birlashtirib ularning tuirni set ga almashtiring.
"""
# ismlar = ["Mahmud","Bobur","Hasan","Ali","Vali"]
# ismlar = set(ismlar)
# print(ismlar)
# sonlar = (1,2,3,6,5,4,78,9,10,12,258)
# sonlar = set(sonlar)
# print(sonlar)
# royxat = ismlar.union(sonlar)
# print(royxat)

"""4) mevalar deb nomlangan ro'yhat(list ) yarating. Avval uni o'zgarmas ro'yhat turiga , keyin esa set turiga o'zgartiring va konsulga ularning 
turini chiqaring.
  -remove() yordamida 3 ta discard() yordamida 3 ta elementni o'chirib tashlang va ro'yhatni konsulga chiqaring.
  -va yangi 5 ta element qo'shing va ro'yhatni konsulga chiqaring;
  -so'ngra ro'yhatni tozalang va uni konsulga chiqaring;
  -keyin esa ro'yhatni o'chirib tashlang;
"""
# meva = ["apple","melon","grape","banana","limo","tomato","mandarin","peach"]
# meva = tuple(meva)
# print(meva)
# meva = set(meva)
# print(type(meva))
# print(meva)
# meva.remove("apple")
# meva.remove("melon")
# meva.remove("grape")
# print(meva)
# meva.discard("peach")
# meva.discard("mandarin")
# meva.discard("tomato")
# print(meva)
# meva.add("orik")
# meva.add("gilos")
# meva.add("olcha")
# meva.add("qaroli")
# meva.add("nok")
# print(meva)
# meva.clear()
# print(meva)
# # del meva
# print(meva)

"""5) yuqorida yaratgan musbat_sonlar va manfiy_sonlar ro'yhatlarimizni set ko'rinishiga olib o'ting.
  -ularni sonlar degan yangi set ga birlashtiring va konsulga chiqaring;
  -har ikkolovida mavjud elementlarni avval musbat_sonlar setiga keyin esa manfiy_sonlar setiga birlashtirib, 
    har ikkolovini konsulga chiqaring;"""
# musbat_sonlar = [2,5,4,7,8,25,65,1,4]
# manfiy_sonlar = [-3,-5,-9,-15,-98,-554]
# sonlar = musbat_sonlar + manfiy_sonlar
# print(sonlar)
# sonlar = set(sonlar)
# print(type(sonlar))
# musbat_sonlar= set(musbat_sonlar)
# print(type(musbat_sonlar))
# manfiy_sonlar = set(manfiy_sonlar)
# print(type(manfiy_sonlar))
# musbat_sonlar.update(manfiy_sonlar)
# print(musbat_sonlar)
# manfiy_sonlar.update(musbat_sonlar)
# print(manfiy_sonlar)
# sonlar = musbat_sonlar.union(manfiy_sonlar)
# print(sonlar)
   





 