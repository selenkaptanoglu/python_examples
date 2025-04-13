#####     GÖREV 1

# Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz

text="The goal is to turn data into information, and information into insight."

words=text.replace('.',' ').replace(',',' ').upper().split()

print(words)

#####     GÖREV 2

# Verilen listeye aşağıdaki adımları uygulayınız.

liste= ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'N', 'C', 'E']

# Adım1: Verilen listenin eleman sayısına bakınız.

len(liste)

# Adım2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.

liste[0]
liste[10]

# Adım3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.

liste[:4]

# Adım4: Sekizinci indeksteki elemanı siliniz.

liste.pop(8)
print(liste)

# Adım5: Yeni bir eleman ekleyiniz.

liste.append("Se")
print(liste)

# Adım6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

liste.insert(8,'N')
print(liste)

#####     GÖREV 3

#Verilens özlük yapısına aşağıdaki adımları uygulayınız.

dict= {'Cristian': ['America', 18],
       'Daisy': ['England', 12],
       'Antonio': ['Spain', 22],
       'Dante': ['Italian', 25],}

#Adım1: Key değerlerine erişiniz

dict.keys()

#Adım2: Value'lara erişiniz.

dict.values()

# Adım3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz

dict['Daisy'][1]=13

#Adım4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

dict.update({'Ahmet': ['Turkey', 24]})

#Adım5: Antonio'yu dictionary'den siliniz.

dict.pop('Antonio')

#####     GÖREV 4

# Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız.

l=[2, 13, 18, 93, 22]

def func(l):
    groups=[[],[]]
    for i,letter in enumerate(l):
        if i%2==0:
            groups[0].append(i)
        else:
            groups[1].append(i)
    return(groups)
cift,tek=func(l)

#####     GÖREV 5

# Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrencide tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

ogrenciler= ['Ali', 'Veli', 'Ayse', 'Talat', 'Zeynep', 'Ece' ]

# cozum1:
for i,ogrenci in enumerate(ogrenciler):
    if i<3:
        i += 1
        print("Mühendislik Fakültesi", i, ". öğrenci: ", ogrenci)
    else:
        i -= 2
        print("Tıp Fakültesi", i, ". öğrenci: ", ogrenci)
# cozum1

# cozum2:
for index, ogrenci in enumerate(ogrenciler[:3], 1):
    print(f"Mühendislik Fakültesi {index} . öğrenci: {ogrenci}")

for index, ogrenci in enumerate(ogrenciler[3:], 1):
    print(f"Tıp Fakültesi {index} . öğrenci: {ogrenci}")
# cozum2

#####     GÖREV 6

# Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer
# almaktadır. Zip kullanarak ders bilgilerini bastırınız.

ders_kodu = ["CMP1005", "PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

for kod, kr, kont in zip(ders_kodu, kredi, kontenjan):
    print(f"Kredisi {kr} olan {kod} kodlu dersin kontenjani {kont} kisidir.")

#####     GÖREV 6

# Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir
# Beklenen Çıktı: Kapsayıp kapsamadığını kontrol etmek için issuperset() metodunu, farklı ve ortak elemanlar için ise intersection ve difference metodlarını kullanınız.

kume1 = set(['data', 'pyhton'])
kume2 = set(['data', 'pyhton', 'qcut', 'lambda', 'function', 'miuul'])

if kume1.issuperset(kume2):
    print(kume1.intersection(kume2))
else:
    print(kume2.difference(kume1))
