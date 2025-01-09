gorevler = []
son_sira_no = 0 
def gorev_ekle(gorev_adi):
    global son_sira_no
    for gorev in gorevler:
        if gorev["Gorev Adi"] == gorev_adi:
            print("Bu Görev Daha Önce Tanımlanmış...")
            return
    silinmis_sira_nolari = [gorev["Sira No"] for gorev in gorevler if gorev["Durum"] == "Silindi"]

    if silinmis_sira_nolari:
       
        son_sira_no = min(silinmis_sira_nolari)
        for gorev in gorevler:
            if gorev["Sira No"] == son_sira_no:
                gorev["Durum"] = "Bekliyor"
                gorev["Gorev Adi"] = gorev_adi
                print(f"Silinmiş görev yeniden atandı: {gorev_adi}, {son_sira_no}")
                return
    else:
       
        son_sira_no = max([g["Sira No"] for g in gorevler], default=0) + 1

   
    yeni_gorev = {
        "Sira No": son_sira_no,
        "Gorev Adi": gorev_adi,
        "Durum": "Bekliyor"
    }
    gorevler.append(yeni_gorev)
    print(f"Yeni görev eklendi: {gorev_adi}, {son_sira_no}")

def gorev_tamamla(sira_no):
    for gorev in gorevler:
        if gorev["Sira No"] == sira_no and gorev["Durum"] == "Bekliyor":
            gorev["Durum"] = "Tamamlandi"
            print(f"Görev tamamlandı: {gorev['Gorev Adi']}")
            return
    print("Hata: Belirtilen sıra numarasıyla bekleyen bir görev bulunamadı.")

def silinmis_gorevleri_listele():
    silinenler = [gorev for gorev in gorevler if gorev["Durum"] == "Silindi"]
    if silinenler:
        print("Silinen Görevler:")
        for gorev in silinenler:
            print(f"{gorev['Sira No']}: {gorev['Gorev Adi']} - {gorev['Durum']}")
    else:
        print("Silinmiş görev bulunmamaktadır.")

def gorev_sil(sira_no):
    for gorev in gorevler:
        if gorev["Sira No"] == sira_no:
            gorev["Durum"] = "Silindi"
            print(f"Görev silindi: {gorev['Gorev Adi']}")
            return
    print("Hata: Belirtilen sıra numarasıyla bir görev bulunamadı.")

def tamamlanan_gorevleri_listele():
    tamamlananlar = [gorev for gorev in gorevler if gorev["Durum"] == "Tamamlandi"]
    if tamamlananlar:
        print("Tamamlanan Görevler:")
        for gorev in tamamlananlar:
            print(f"{gorev['Sira No']}: {gorev['Gorev Adi']} - {gorev['Durum']}")
    else:
        print("Tamamlanan görev bulunmamaktadır.")

def tum_gorevleri_listele():
    if gorevler:
        print("Tüm Görevler:")
        for gorev in sorted(gorevler, key=lambda x: x["Sira No"]):
            print(f"{gorev['Sira No']}: {gorev['Gorev Adi']} - {gorev['Durum']}")
    else:
        print("Hiçbir görev bulunmamaktadır.")

def cikis():
    print("Görev yöneticisinden çıkılıyor. Hoşça kalın!")


def main():
    while True:
        print("\nYapabileceğiniz işlemler:")
        print("1. Yeni bir görev ekle")
        print("2. Bir görevi tamamla")
        print("3. Bir görevi sil")
        print("4. Tamamlanan görevleri listele")
        print("5. Tüm görevleri listele")
        print("6. Silinmiş görevleri listele")
        print("7. Çıkış")

        secim = input("Bir işlem seçin (1-7): ")

        if secim == "1":
            gorev_adi = input("Yeni görev adını girin: ")
            gorev_ekle(gorev_adi)
        elif secim == "2":
            try:
                sira_no = int(input("Tamamlamak istediğiniz görevin sıra numarasını girin: "))
                gorev_tamamla(sira_no)
            except ValueError:
                print("Lütfen geçerli bir sayı girin.")
        elif secim == "3":
            try:
                sira_no = int(input("Silmek istediğiniz görevin sıra numarasını girin: "))
                gorev_sil(sira_no)
            except ValueError:
                print("Lütfen geçerli bir sayı girin.")
        elif secim == "4":
            tamamlanan_gorevleri_listele()
        elif secim == "5":
            tum_gorevleri_listele()
        elif secim == "6":
            silinmis_gorevleri_listele()
        elif secim == "7":
            cikis()
            break
        else:
            print("Geçersiz bir seçim yaptınız. Lütfen 1-7 arasında bir değer girin.")


main()
