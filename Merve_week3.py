gorevler=[]
sira_numarasi=[]

#GOREV EKLEME FONKSIYONU

def gorev_ekle(gorev_adi):
    global sira_numarasi
    if sira_numarasi:
       sira=sira_numarasi.pop(0)
    else:
       sira=len(gorevler)+1
    gorev={"Sira Numarasi":sira,"Gorev adi":gorev_adi,"Durum":"Bekliyor"}
    gorevler.append(gorev)
    gorevler.sort(key=lambda x:x["Sira Numarasi"])
    print(f"{sira} numarali {gorev_adi}  gorevi basariyla eklendi")
    


#GOREV DURUMUNU GUNCELLEME FONKSIYONU

def gorev_durumu(sira):
    for gorev in gorevler:
        if gorev["Sira Numarasi"]==sira and gorev["Durum"]=="Bekliyor":
           gorev["Durum"]="Tamamlandi"
           print(f"{gorev["Gorev adi"]} tamamladiniz.")
           return
    print("Sira numarasi yanlis veye gorev zaten tamamlanmis!!")   

#GOREV SILME FONKSIYONU

def gorev_sil(sira):
    global sira_numarasi
    for gorev in gorevler:
        if gorev["Sira Numarasi"]==sira:
           gorev["Durum"]="Silindi"
           sira_numarasi.append(sira)
           sira_numarasi.sort()
           print(f"{gorev["Gorev adi"]} gorevi silindi..")
           return
    print("Girdiginiz sira numarasi yanlis!")

#LISTELEME FONKSIYONU

def tamamlanan_gorevler():
    print("Tamamlanan Gorevler:")
    for gorev in gorevler:
        if gorev["Durum"]=="Tamamlandi":
           print(f"Sira:{gorev["Sira Numarasi"]}-Gorev Ad:{gorev["Gorev adi"]}-Durum:{gorev["Durum"]}")

def tum_gorevler():
    print("Tum Gorevler:")
    for gorev in gorevler:
        print(f"Sira:{gorev["Sira Numarasi"]}-Gorev Ad:{gorev["Gorev adi"]}-Durum:{gorev["Durum"]}")


#MENU OLUSTURMA

def menu():
    while True:
        print("------------GOREV YONETICISI------------")
        print("1.Gorev Ekle")
        print("2.Gorev Tamamla")
        print("3.Gorev Sil")
        print("4.Tamamlanan Gorevleri Listele")
        print("5.Tum Gorevleri Listele")
        print("6.Cikis")

        secim=input("Hangi islemi yapmak istiyorsunuz (1-6 ):")

        if secim=="1":
            gorev_adi=input("Bir gorev adi giriniz :")
            gorev_ekle(gorev_adi)
            

        elif secim=="2":
            sira=int(input("Tamamlanacak gorevin sira numarasi : "))
            gorev_durumu(sira)

        elif secim=="3":    
            sira=int(input("Silinecek gorevin sira numarasi : "))
            gorev_sil(sira)

        elif secim=="4": 
            tamamlanan_gorevler()   

        elif secim=="5":
            tum_gorevler()
        
        elif secim=="6":
            print("Cikiliyor....")
            break
        else:
            print("Gecerli bir secenek seciniz!!")

menu()
