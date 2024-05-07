# İleride Kullanmak Üzere Kütüphanelerimizi Kodumuza Dahil Ediyoruz.

import random
import math

#Ana Sınıfımızı Oluşturalım.

class Ordu:
  def __init__(self,isim,kapladigiAlan,maliyet):
    self.isim = isim
    self.kapladigiAlan = kapladigiAlan
    self.maliyet = maliyet
    
#Sonrasında İsim Değiştirmek İçin Bir Fonksiyon Yazalım.
    
  def isimguncelle(self, isim):
    self.isim = isim
    
#Sonrasında Kapladığı Alanı Değiştirmek İçin Bir Fonksiyon Yazalım.
    
  def KAguncelle(self, kapladigiAlan):
    self.kapladigiAlan = kapladigiAlan
    
#Sonrasında Maliyeti Değiştirmek İçin Bir Fonksiyon Yazalım.
    
  def maliyetguncelle(self, maliyet):
    self.maliyet = maliyet
    
#Ordumuz Hakkında Bilgi Edinmek İçin Bir Fonksiyon Yazalım.
  
  def ordubilgisi(self):
    print("Adı :", self.isim)
    print("Kapladığı Alan :", self.kapladigiAlan)
    print("Maliyet :", self.maliyet)
    
#Çocuk Sınıfımızı Oluşturalım

class Birlik(Ordu):
  def __init__(self, isim, kapladigiAlan, maliyet, favorihedef, hasarturu, hedefler):
    super().__init__(isim, kapladigiAlan, maliyet)
    self.favorihedef = favorihedef
    self.hasarturu = hasarturu
    self.hedefler = hedefler

# Belli Bir Kapasitesi Olan Ordumuza Kaç Adet Alabileceğimizi Öğrenmek İçin Bir Fonksiyon Yazalım Ayrıca Burada Kapladığı Alan Tam Bölünmediği Zaman İstediğimiz Sonucu Vermeyeceği İçin İmport Ettiğimiz Matematik Kütüphanesindeki Aşağı Yuvarlamaya Yarayan 'Floor' Fonksiyonunu Kullanıyoruz.
    
  def kacalinabilir(self):
    x = 300 / int(self.kapladigiAlan)
    print("Ordu Kapasiteniz maksimum 300 Birimdir. Dilerseniz ordunuza ", math.floor(x), "Adet Alabilirsiniz")

# Bir Liste İçersine Cümleler Yazıyoruz Ve Bunları Rastgele Şekilde Yazdırmak İçin İmport Ettiğimiz 'Random' Kütüphanesini Kullanıyoruz.
    
  def saldir(self):
    saldirisonucu = ["O kadar kötü savaştın ki klan lideri seni klandan attı", "Üzgünüm, Yüzde 99'da kaldın", "Yüzde 70 aldın iyi tarafından bak ganimetin hepsi sende", "Harika bir savaştı %100 aldın.", "Klan lideri seni tebrik ediyor, terfi aldın", "Sanırım kuzenin senin yerine savaştı, berbat!"]
    randomcumle = random.choice(saldirisonucu)
    print(randomcumle)

  # Override Edeceğimiz Fonksiyonu Ekleyelim.

  def ordubilgisi(self):
    print("Adı :", self.isim)
    print("Kapladığı Alan :", self.kapladigiAlan)
    print("Maliyet :", self.maliyet)
    print("Favori hedef :",self.favorihedef)
    print("Hasar Türü :", self.hasarturu)
    print("Hedefler :", self.hedefler)