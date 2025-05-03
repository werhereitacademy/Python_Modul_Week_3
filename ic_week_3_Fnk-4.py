#1- Verilen bir kelimeyi belirtilen kez ekrana yazdiran python fonksiyonu yazınız.

def kelimeyaz(kelime, sayi):
        for i in range(sayi):
            print(kelime)


kelime = input("Bir kelime giriniz")
sayi = int(input("Kaç kere yazdırmak istersiniz?"))
kelimeyaz(kelime, sayi)


#2- Verilen 2 sayı arasındaki tüm asal sayıları bulan python fonksiyonunu yazınız.

def asalsayilar(sayi1, sayi2):
    asal_sayilar = []
    for sayi in range(sayi1, sayi2 + 1):
        if sayi > 1:
            for i in range(2, int(sayi ** 0.5) + 1):
                if sayi % i == 0:
                    break
            else:
                asal_sayilar.append(sayi)
    return asal_sayilar

print(f"1 ile 10 arası asalsayılar: {asalsayilar(1, 10)}")


#3- Saati saniyeye çeviren bir fonksiyon yazınız.

def saniye():
    saat=int(input("Saat: "))
    dakika=int(input("Dakika: "))
    saniye=int(input("Saniye: "))
    toplam_saniye=(saat*3600)+(dakika*60)+saniye
    print(f"Toplam saniye: {saat} Saat {dakika} dakika {saniye} saniye toplamı {toplam_saniye} saniyedir")

saniye()


#4- Matematik, Fizik ve Kimya derslerinin Vize ve Final ortalamalarina gore (Vize nin %40 i , Finalin %60 i) ogrencinin derslerden hangi not ile gectigini veya kaldigini gosteren bir program yaziniz.

def vize_final(ders, vnotu, fnotu):
    ders = input("Ders adı: ")
    vnotu = int(input("Vize notu: "))
    fnotu = int(input("Final notu: "))
    ortalama = (vnotu * 0.4) + (fnotu * 0.6)
    if ortalama >= 0 and ortalama <= 44:
        print("FF - Kaldınız")
    elif ortalama >= 45 and ortalama <= 54:
        print("DD - Geçtiniz")
    elif ortalama >= 55 and ortalama <= 69:
        print("CC - Geçtiniz")
    elif ortalama >= 70 and ortalama <= 84:
        print("BB - Geçtiniz")
    elif ortalama >= 85 and ortalama <= 100:
        print("AA - Geçtiniz")

 
vize_final("", 0, 0)
