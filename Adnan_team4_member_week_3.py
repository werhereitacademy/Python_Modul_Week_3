print("Gorevlerinizi gorebilecegeniz, degisterebilecegiz ve silebilecegeniz programda hosgeldiniz!")
gorevler=[]
def gorev_ekle(gorev_listesi):
        gorev_ad=input("Gorev adini giriniz:")
        gorev_durum="Bekliyor"
        gorev_sirasi=len(gorev_listesi)+1
        gorev={"ad":gorev_ad,"durum":gorev_durum,"sira":gorev_sirasi}
        gorev_listesi.append(gorev)
        print(f"Gorev eklendi: {gorev['ad']}.{gorev['sira']}-{gorev['durum']}")
        return gorev_listesi

def gorev_tamamla(gorev_listesi):
        if not gorev_listesi:
            print("Gorev listesi bos.")
            return
        gorev_sirasi=int(input("Tamamlamak istediginiz gorevin sirasi:"))
        for gorev in gorev_listesi:
            if gorev["sira"]==gorev_sirasi:
                gorev["durum"]="Tamamlandi"
                print(f"Gorev tamamlandi: {gorev['ad']}")
                return
        print("Gorev bulunamadi.")
        
def gorev_sil(gorev_listesi):
        if not gorev_listesi:
            print("Gorev listesi bos.")
            return
        gorev_sil=int(input("Silmek istediginiz gorevin sirasi:"))
        for gorev in gorev_listesi:
            if gorev["sira"]==gorev_sil:
                gorev_listesi.remove(gorev)
                for g in gorev_listesi:
                    if g["sira"]>gorev_sil:
                        g["sira"]-=1
                print(f"Gorev silindi: {gorev['ad']}")
                return
        print("Gorev bulunamadi.")
        

def tamamlanan_gorevleri_sil(gorev_listesi):
        if not gorev_listesi:
            print("Gorev listesi bos.")
            return
        for gorev in gorev_listesi[:]:
            if gorev["durum"]=="Tamamlandi":
                gorev_listesi.remove(gorev)
                print(f"Gorev silindi: {gorev['ad']}")
        print("Tamamlanan gorevler silindi.")
        
def gorevleri_listele(gorev_listesi):
        if not gorev_listesi:
            print("Gorev listesi bos.")
        else:
            print("Gorevler:")
            gorev_listesi.sort(key=lambda x:x["sira"])
            for gorev in gorev_listesi:
                print(f"{gorev['sira']}. {gorev['ad']} - {gorev['durum']}")       


def tamamlanan_gorevleri_listele(gorev_listesi):
    print("Tamamlanan Gorevler:")
    gorev_listesi.sort(key=lambda x:x["sira"])
    for gorev in gorev_listesi:
        if gorev["durum"]=="Tamamlandi":
            print(f"{gorev['sira']}. {gorev['ad']} - {gorev['durum']}")
        
while True:
    secenek=int(input("""
    Ne yapmak istiyorsunuz?:
    1-Yeni bir gorev ekle
    2-Gorevi Tamamla
    3-Gorevi sil
    4-Tamamlanan gorevleri sil
    5-Gorevleri Listele
    6-Tamamlanan gorevleri listele
    7-Cikis
    Seceneginizi giriniz:"""))
    
    if secenek==1:
        gorev_ekle(gorevler)
        
    elif secenek==2:
        gorev_tamamla(gorevler)
    elif secenek==3:
        gorev_sil(gorevler)
    elif secenek==4:
        tamamlanan_gorevleri_sil(gorevler)
    elif secenek==5:
        gorevleri_listele(gorevler)
    elif secenek==6:
        tamamlanan_gorevleri_listele(gorevler)
    elif secenek==7:
        print("Cikis yapiliyor...")
        break
    else:
        print("Gecersiz secenek. Lutfen tekrar deneyin.")