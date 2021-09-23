print("Bu ders dosyası Baysan tarafından hazırlanmıştır...")
print("""
****************************
             METODLAR	

Metod nedir ?
Şimdiye kadar Pythonda kullanabildiğimiz bir çok veri tipi gördük ve 
bazı veritipleri üzerinde bu veritiplerinin metodlarını kullandık. 
Aslında bu veritiplerin oluşturulan her bir değişken Pythonda obje( object) olarak düşünülür
ve Python geliştiricileri bu objelere birçok metod tanımlamıştır. Peki nedir bu metodlar ?

Metodlar bir obje üzerinde belli işlemleri gerçekleştiren objelere özgü fonksiyonlardır
 ve objelerin üzerinde metodlar şu şekilde kullanılır.

obje.herhangi_bir_metod(değerler(opsiyonel))
Örneğin bir liste objesi oluşturduğumuz zaman bu objenin
üzerinde belli metodları uygulayabiliriz.

liste=[1,2,3,4,5]
liste.insert(1,"Baysan")
print(liste)
	""")
liste=[1,2,3,4,5]
liste.insert(1,"Baysan")
print(liste)
print("**********************************")
print("""
                  FONKSİYONLAR


Python geliştiricilerin yazdığı fonksiyonlara yani bizim hazır kullandığımız fonksiyonlara(print(),type() vs.) gömülü fonksiyonlar(built-in function) denilmektedir.
Ancak bunlardan hariç olarak biz kendi özel fonksiyonlarımızı(user-defined functions) da tanımlayabiliriz.
Fonksiyonlar bizim gereksiz kod tekrarı yapmamamızı sağlar.
Fonksiyonlar şu şekilde tanımlanır:
def fonksiyon_adı(parametre1,parametre2..... (opsiyonel)):
    # Fonksiyon bloğu
    Yapılacak işlemler
    # dönüş değeri - Opsiyonel

   Selamla isimli bir fonksiyon tanımlayalım;
   def selamla():
   	print("Selamunaleyküm...")
   	print("Nasılsınız?")
	""")
def selamla():
	print("Selamunaleyküm...")
	print("Nasılsınız...")
print("""
Fonksiyonumuzu tanımladık şimdi de python'da type fonksiyonu ile daha detaylı görelim;
print(type(selamla))
	""")
print(type(selamla))
print("*****************************")
print("""
                    FONKSİYONLARIN KULLANILMASI	
Tanımlanan bir fonksiyonun kullanılmasına programlama dillerinde Fonksiyon Çağrısı denmektedir. 
O halde selamla fonksiyonumuzu nasıl çağıracağımızı öğrenelim. Fonksiyon çağrısı şu şekilde yapılabilmektedir;
fonksiyon_adı(Argüman1,Argüman2....)  -> fonksiyon çağırmak için

selamla()                              ->Fonksiyon parametre almadığında içine argümanlarımızı göndermiyoruz.
""")
selamla()
print("""
	Burada gördüğünüz gibi, fonksiyonumuz çağrıldığı zaman, kendi bloğundaki işleri yaptı 
	ve ekrana 2 tane değer yazdırdı. Bu fonksiyonu istediğimiz yerde tekrar tekrar çağırabiliriz.

selamla()
selamla()
selamla()  

""")
selamla()
selamla()
selamla()
print("**************************")
print("""
Peki fonksiyonumuzu içine değer verirsek ne olur?
selamla("Enes")
Bu selamla fonksiyonunun içine değer vermediğimiz için çalışmaz ve hata verir.
	""")
print("""***************************************
	                  Parametreler ve Argümanlar

Biliyorsunuz biz selamla fonksiyonunun içine herhangi bir değer göndermiyorduk ve fonksiyonumuz hep aynı işi yapıyordu. 
Ancak çoğu zaman fonksiyonlarımız içine gönderdiğimiz değerlerle farklı işlemler yaparlar.
Örneğin katı meyve sıkacağına eğer “Elma” verirsek elma suyu, “Nar” verirsek nar suyu hazırlayacaktır. 
Fonksiyonlarda da Parametreleri bu şekilde düşünebilirsiniz.
İsterseniz şimdi selamlama fonksiyonumuzu bir tane parametre alacak şekilde tanımlayalım

def selamla1(isim):          -> isim değişkenimiz burada parametre olmaktadır
	print("Merhaba",isim)
selamla1("Baysan")           -> "Baysan" değeri burda argüman olmaktadır.
selamla1("Kardeşim")         -> "Kardeşim" değeri burda argüman olmaktadır.
Çıktısı:
	""")
def selamla1(isim):
	print("Merhaba",isim)
selamla1("Baysan")
selamla1("Kardeşim")
print("""


Bizim fonksiyon tanımlarken tanımladığımız herbir değişken birer Parametre ,
fonksiyon çağrısı yaptığımız zaman içine gönderdiğimiz değerler ise Argümanolmaktadır. 
Burada fonksiyonu çağırırken gönderdiğimiz “Kemal” değeri “isim” isimli parametreye eşit oluyor 
ve fonksiyonumuz bu değere göre işlem yapıyor. “Ayşe” değerini gönderdiğimizde ise fonksiyonumuz bu değere göre işlem yaparak ekrana farklı bir değer yazdırıyor. 
Şimdi isterseniz farklı bir fonksiyon tanımlayalım ve 3 tane parametre alsın.

def toplama(a,b,c):
	print("Toplamları:",a+b+c)
toplama(3,4,5)
toplama(23,12,3)

Çıktısı :
	""")
def toplama(a,b,c):
	print("Toplamları:",a+b+c)
toplama(3,4,5)
toplama(23,12,3)
print("******************")
print("""
Şimdi de örnek olması için bir sayının faktoriyelini tanımlayan bir fonksiyon yazalım:
# Eğer sayımız “5” ise faktoriyel 5 x 4 x 3 x 2 x 1 = 120 olacaktır

faktoriyel için fonksiyon:
def faktoriyel(sayı):
    faktoriyel = 1
    if (sayı == 0 or sayı == 1):
        print("Faktoriyel",faktoriyel)
    else:
        while (sayı >= 1):
            faktoriyel *= sayı
            sayı -=1
        print("Faktoriyel", faktoriyel)
faktoriyel(5)
faktoriyel(6)
faktoriyel(3)
faktoriyel(1)
faktoriyel(0)

ÇIKTISI:

""")
def faktoriyel(sayı):
    faktoriyel = 1
    if (sayı == 0 or sayı == 1):
        print("Faktoriyel",faktoriyel)
    else:
        while (sayı >= 1):
            faktoriyel *= sayı
            sayı -=1
        print("Faktoriyel", faktoriyel)
faktoriyel(5)
faktoriyel(6)
faktoriyel(3)
faktoriyel(1)
faktoriyel(0)
print("*******************************************************************")
print("""

                       FONKSİYONLARDA RETURN
Bu konuda fonksiyonlardan değer döndürmemizi sağlayan return ifadesini görmeye çalışacağız. 
Önceki bölümde yazdığımız fonksiyonları hatırlayacak olursak, bu fonksiyonlar sadece ekrana print ile değer yazdırıyordu. 
Ancak bu fonksiyonlar yaptıklar işlemler bize herhangi bir değer vermiyorlardı. 
Ancak biz programlarımızda bir fonksiyon sonucunda elde edilen değerleri alıp programlarımızın bambaşka yerlerinde kullanmak isteyebiliriz. 
Bu derste bunu nasıl yapacağımızı öğrenmeye çalışacağız.
return ifadesi fonksiyonun işlemi bittikten sonra çağrıldığı yere değer döndürmesi anlamı taşır. 
Böylelikle, fonksiyonda aldığımız değeri bir değişkende depolayabilir 
ve değeri programın başka yerlerinde kullanabiliriz. Şimdi iki tane çok basit fonksiyon yazalım 
ve return neden gereklidir anlamaya çalışalım.

def toplama1(a,b,c):          -> Birinci fonksiyon
	print("Toplamları:",a+b+c)
def ikiyleçarp(a):            -> İkinci fonksiyon
	print("ikiyle çarp",a*2)

toplam = toplama1(3,4,5)
ikiyleçarp(toplam)           -> Hata alırız

toplamları:12
Type Error        verecektir
Burada hata almamızın sebebi fonksiyonları herhangi bir değer döndürmemesi yani return kullanmamasıdır.



Burada toplama fonksiyonundan herhangi bir değer döndürülmediği için toplam değişkenimiz hiçbir değere sahip olmadı
ve tipi NoneType(atanmamış) olmuş oldu. 
İsterseniz burada fonksiyonları tekrardan tanımlayalım ve return mantığını anlamaya çalışalım.

Doğru olan:
def toplama1(a,b,c):
	print("Toplamları:",a+b+c)
def ikiyle_çarp(a):
	return a*2
toplam=toplama1(3,4,5)
print(ikiyle_çarp(toplam))

ÇIKTISI:

	""")
def toplama1(a,b,c):
    return a+b+c     # return 'un kullanımı
def ikiyle_çarp(a):
    return a*2
 
toplam = toplama1(3,4,5)
print(ikiyle_çarp(toplam))
print("""
şte return ifadesinin anlamı tam olarak budur.
return yardımıyla fonksiyonlar değerleri çağrıldığı yere döndürebilir ve biz de bu değerleri istediğimiz yerde kullanabiliriz
	""")
print("""
Bir örnek daha yapalım:
def üçleçarp(a):
    print("1.fonksiyon çalıştı")
    return a*3
def ikiyletopla(a):
    print("2.fonksiyon çalıştı")
    return a + 2
def dördeböl(a):
    print("3.fonksiyon çalıştı")
    return a / 4
# 3 ünü beraber kullanalım.
 
print(dördeböl(ikiyletopla(üçleçarp(5))))


ÇIKTISI:
	""")
def üçleçarp(a):
    print("1.fonksiyon çalıştı")
    return a*3
def ikiyletopla(a):
    print("2.fonksiyon çalıştı")
    return a + 2
def dördeböl(a):
    print("3.fonksiyon çalıştı")
    return a / 4
# 3 ünü beraber kullanalım.
 
print(dördeböl(ikiyletopla(üçleçarp(5))))
print("""******************************************
return ifadesinden sonra fonksiyonumuz tamamıyla sona erer. Yani, return ifadesinden sonra yapılan herhangi bir işlem çalıştırılmaz. """)
print("""

def toplama2(a,b,c):
    return a + b + c
    print("Toplama fonksiyonu") -> Çalıştırılmadı.

doğrusu şu şekildedir:
def toplama2(a,b,c):
    print("Toplama fonksiyonu") # Çalıştırıldı.
    return a + b + c
 
toplama2(1,2,3)

	""")
def toplama2(a,b,c):
    print("Toplama fonksiyonu") # Çalıştırıldı.
    return a + b + c
 
toplama2(1,2,3)

print("""
	fonksiyonlarda çağrıldığı yere herhangi bir değer döndürmeyen(return kullanılmayan) fonksiyonlara void fonksiyonlar denmektedir. Bunu da genel kültür olarak bilmekte fayda var.

	***********************************************************************
	""")
print("""
                       FONKSİYONLARDA PARAMETRE TÜRLERİ

--Parametrelerin Varsayılan Değerleri--

def selamla(isim):
    print("Selam",isim)
selamla("Baysan")
Çıktısı:
Selam Baysan
*************
selamla()  -> Bu kullanım hata verecektir çünkü isim parametresi girmedik.

->Ancak biz eğer bir parametrenin değerini varsayılan olarak belirlemek istersek, 
bunu varsayılan değerler ile yapabiliriz. 
Varsayılan değerleri anlamak için selamla fonksiyonunu varsayılan parametre değeri ile yazalım.

def selamla5(isim="varsayılan isim"):
    print("Selam",isim)
selamla5()                -> Hiç bir değer göndermedik isim parametresinin değeri varsayılan olarak "varsayılan isim" olarak belirlendi
selamla5("Baysan")        -> Değer verirsek varsayılan değerin yerine bizim verdiğimiz değer geçer.


	""")
def selamla5(isim="varsayılan isim"):
    print("Selam",isim)
selamla5()
selamla5("Baysan")
print("""**************************************
    peki birden fazla parametreye sahip olursak ne olacak?
Birden fazla parametreye sahip olduğumuz bir fonksiyon daha tanımlayalım...

def bilgilerigöster(ad = "Bilgi Yok",soyad = "Bilgi Yok",numara =  "Bilgi Yok"):
    print("Ad:",ad,"Soyad:",soyad,"Numara:",numara)

bilgilerigöster()
bilgilerigöster("Enes","Baysan")

    """)
def bilgilerigöster(ad = "Bilgi Yok",soyad = "Bilgi Yok",numara =  "Bilgi Yok"):
    print("Ad:",ad,"Soyad:",soyad,"Numara:",numara)
bilgilerigöster()
bilgilerigöster("Enes","Baysan")
print("""**********
Ancak böyle bir durumda argümanları gönderirken sıralı vermemiz gerekiyor.
Peki sadece numara parametresine değer vermek istersek ne yapmalıyız?

bilgilerigöster(numara="12345")         -> numara parametresini özel olarak belirtiyoruz.
 
ÇIKTISI:
  """)
bilgilerigöster(numara="12345")

print("""********
    Bir diğer örnek:

    bilgilerigöster(ad="Enes",numara="12345")
Çıktısı:

    """)
bilgilerigöster(ad="Enes",numara="12345")
print("""**************
print fonksiyonunun sep parametresini hatırlayalım
print("Muhammed","Enes","Baysan")             -> sep parametresine değer vermeyince varsayılan olarak boşluk karakteri verildi.
print("Muhammed","Enes","Baysan",sep = "/")   -> sep parametresine özel olarak değer atadık.
 ÇIKTISI:""")
print("Muhammed","Enes","Baysan")
print("Muhammed","Enes","Baysan",sep="/")
print("""****************************
 Esnek Sayıda Değerler
Biliyorsunuz bir fonksiyon yazıldığında özel olarak kaç tane parametresi olacağını önceden belirtmemiz gerekiyor. 
Örneğin, bir toplama fonksiyonu yazalım.

def toplama6(a,b,c):
    print(a+b+c)
toplama6(7,8,9)
ÇIKTISI:
    """)
def toplama6(a,b,c):
    print(a+b+c)
toplama6(7,8,9)

print("""**************
toplama6(3,4,5,6)  -> bunu yaparsak hata alırız. 3 argüman tanımladığımız bir fonksiyona 4. argümanı veremeyiz.

Eğer bu fonksiyonu 4 argüman alacak şekilde tanımlamak istersek, tekrardan tanımlamamız gerekiyor.
def toplama6(a,b,c,d):
    print(a+b+c+d)
toplama6(1,2,3,4)
Ancak bu seferde 3 argüman veremeyiz
toplama6(1,2,3)     -> hata alırız  """)
print("""******************

Peki ben bir fonksiyonu esnek sayıda argümanla kullanmak istersem ne yapacağım ?
Bunun için de Yıldızlı Parametre kullanmam gerekiyor. 
Kullanımı şu şekildedir;

def toplama7(*parametreler): -> Artık parametreler değişkenini bir demet gibi kullanabilirim.
    toplam1 =  0
    print("Parametreler:",parametreler)
    for i in parametreler:
        toplam1 += i
    return toplam1
print(toplama7(3,4,5,6,7,8,9,10))
 ÇIKTISI:     """)
def toplama7(*parametreler):
    toplam1 =  0
    print("Parametreler:",parametreler)
    for i in parametreler:
        toplam1 += i
    return toplam1
print(toplama7(3,4,5,6,7,8,9,10))
print("""
    print(toplama7())
Çıktısı: """)
print(toplama7())

print("""*************
print(toplama7(1,2,3))
ÇIKTISI:  """)
print(toplama7(1,2,3))
print("*******************************")
print("""
                FONKSİYONLARIN KAPSAMI GLOBAL VE YEREL DEĞİŞKENLER




    """)