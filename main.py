#Sınıflar Dosyasına Yazdığımız Kodları Kullanabilmek İçin İmport Ediyoruz.

import sınıflar

#Döngü ile verileri almak için ilk olarak boş sözlükler oluşturuyoruz.
 
ordu1 = {}
birlik1 = {}

# Aşağıda 1 dögü içinde hem ordu hemde birlik sözlüğüne ekleyeceğimiz verileri kullanıcıdan alıyoruz.

for i in range (2):
  isim = input("Ordunuzun adını giriniz: ")
  kapladigiAlan = int(input("Kapladığı alanı giriniz : "))
  maliyet = int(input("Ordunuzun maliyetini giriniz : "))
  y = sınıflar.Ordu(isim, kapladigiAlan, maliyet)
  ordu1[i] = y
  
  print("----------------------------------")

  isim = input("Birliğinizin adını giriniz: ")
  kapladigiAlan = int(input("Kapladığı alanı giriniz : "))
  maliyet = int(input("Birliğinizin maliyetini giriniz : "))
  favorihedef = input("Favori hedefini giriniz :")
  hasarturu = input("Hasar türünü giriniz : ")
  hedefler = input("Hedeflerini giriniz : ")
  z = sınıflar.Birlik(isim, kapladigiAlan, maliyet, favorihedef, hasarturu, hedefler)
  birlik1[i] = z
  print("----------------------------------")
# Aşağıdaki döngü ile her bir veri için yazdığımız fonksiyonları çağırıyoruz.
  
for j in ordu1:
  ordu1[j].isimguncelle(input("Ordunuzun yeni ismini giriniz: "))
  ordu1[j].KAguncelle(input("Ordunuzun kapladığı alanı giriniz: "))
  ordu1[j].maliyetguncelle(input("Ordunuzun maliyetini giriniz: "))
  print("\nOrdu Bilgisi: ")
  ordu1[j].ordubilgisi()

  print("----------------------------------")

for g in birlik1:
  birlik1[g].isimguncelle(input("Birliğinizin yeni ismini giriniz: "))
  birlik1[g].KAguncelle(input("Birliğinizin kapladığı alanı giriniz: "))
  birlik1[g].maliyetguncelle(input("Birliğinizin maliyetini giriniz: "))
  print("\nBirlik Bilgisi: ")
  birlik1[g].ordubilgisi()
  birlik1[g].kacalinabilir()
  print("\n")
  birlik1[g].saldir()
