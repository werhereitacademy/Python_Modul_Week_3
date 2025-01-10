
gorevler=[]




while True:

    print("1:yeni gorev")
    print("2:tamamlama")
    print("3:silmek")
    print("4:tamamlanan gorevler")
    print("5:durumlarıyla birlikte listele")
    print("6:cikis")

    secim = int(input("1 ilr 6 arasi bir rakam giriniz"))


    def yenigorev():
        yeniAd = input("gorev adini giriniz:")
        gorevNo = len(gorevler) + 1
        gorev = {"gorev adi": yeniAd, "gorev numarasi": gorevNo, "gorev durumu": "beklemede"}
        gorevler.append(gorev)
        print(f"yeni gorev:{yeniAd},gorev numarasi:{gorevNo},gorev durumu:beklemede olarak ekledndi.")





    def tamamlama():
        gorevNo = int(input("tamamlamak istediginiz gorev numarasini yaziniz:"))
        for gorev in gorevler:
            if gorevNo == gorev["gorev numarasi"]:
                gorev["gorev durumu"] = "tamamlandi"
                print("gorev tamamlandi")
                return


    def silme():
        print(gorevler)
        gorevNo = int(input("silmek istediginiz gorev numarasini yaziniz:"))
        for gorev in gorevler:
            if gorevNo == gorev["gorev numarasi"]:
                gorevler.remove(gorev)

                sayac=1
                for gorev in gorevler:
                    gorev["gorev numarasi"]=sayac
                    sayac+=1

    

                print("gorev silindi")
                return


    def tamamlanmis_liste():
        for gorev in gorevler:
            if gorev["gorev durumu"] == "tamamlandi":
                print(f"tamamlanan gorevler {gorev}")
            else:
                print("tamamlanan gorev bulunamadi")


    def tum_liste():
        print(gorevler)


    if secim <= 6:
        if secim != 1:
            if len(gorevler) == 0:

                print("herhangi bir gorev bulunamadi, yeni bir gorev ekleyiniz")
                yenigorev()
            else:
                if secim == 2:
                    tamamlama()
                elif secim == 3:
                    silme()
                elif secim == 4:
                    tamamlanmis_liste()
                elif secim == 5:
                    tum_liste()
                elif secim == 6:
                    break
        else:
            if secim == 1:
                yenigorev()
    else:
        print("Gecersiz giris yapildi")

print(gorevler)


