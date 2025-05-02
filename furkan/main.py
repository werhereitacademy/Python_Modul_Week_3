#bazi yerlerinde yapay zekadan yardım alinmistir


gorevler = []

def gorev_ekle(gorev_adi):
    sira_numarasi = sonraki_sira_numarasi_al()
    gorev = {
        "Sıra Numarası": sira_numarasi,
        "Görev Adı": gorev_adi,
        "Durum": "Bekliyor"
    }
    gorevler.append(gorev)
    print(f"Görev '{gorev_adi}' {sira_numarasi} sıra numarası ile eklendi.")

def gorev_tamamla(sira_numarasi):
    gorev = gorev_bul(sira_numarasi)
    if gorev:
        gorev["Durum"] = "Tamamlandı"
        print(f"Görev '{gorev['Görev Adı']}' tamamlandı.")
    else:
        print("Görev bulunamadı.")

def gorev_sil(sira_numarasi):
    gorev = gorev_bul(sira_numarasi)
    if gorev:
        gorev["Durum"] = "Silindi"
        print(f"Görev '{gorev['Görev Adı']}' silindi.")
    else:
        print("Görev bulunamadı.")

def tamamlanan_gorevleri_listele():
    tamamlanan_gorevler = [gorev for gorev in gorevler if gorev["Durum"] == "Tamamlandı"]
    if tamamlanan_gorevler:
        print("Tamamlanan Görevler:")
        for gorev in tamamlanan_gorevler:
            print(f"{gorev['Sıra Numarası']}: {gorev['Görev Adı']}")
    else:
        print("Tamamlanan görev bulunamadı.")

def tum_gorevleri_listele():
    if gorevler:
        print("Tüm Görevler:")
        for gorev in sorted(gorevler, key=lambda x: x["Sıra Numarası"]):
            print(f"{gorev['Sıra Numarası']}: {gorev['Görev Adı']} - {gorev['Durum']}")
    else:
        print("Görev bulunamadı.")

def sonraki_sira_numarasi_al():
    kullanilan_numaralar = {gorev["Sıra Numarası"] for gorev in gorevler if gorev["Durum"] != "Silindi"}
    return next(num for num in range(1, len(gorevler) + 2) if num not in kullanilan_numaralar)

def gorev_bul(sira_numarasi):
    for gorev in gorevler:
        if gorev["Sıra Numarası"] == sira_numarasi:
            return gorev
    return None

def menu():
    print("\nGörev Yönetimi")
    print("1. Yeni görev ekle")
    print("2. Görev tamamla")
    print("3. Görev sil")
    print("4. Tamamlanan görevleri listele")
    print("5. Tüm görevleri listele")
    print("6. Çıkış")

def ana_program():
    while True:
        menu()
        secim = input("Seçiminizi yapın (1-6): ")
        if secim == "1":
            gorev_adi = input("Görev adını girin: ")
            gorev_ekle(gorev_adi)
        elif secim == "2":
            sira_numarasi = int(input("Tamamlamak istediğiniz görevin sıra numarasını girin: "))
            gorev_tamamla(sira_numarasi)
        elif secim == "3":
            sira_numarasi = int(input("Silmek istediğiniz görevin sıra numarasını girin: "))
            gorev_sil(sira_numarasi)
        elif secim == "4":
            tamamlanan_gorevleri_listele()
        elif secim == "5":
            tum_gorevleri_listele()
        elif secim == "6":
            print("Görev Yönetiminden çıkılıyor. İyi günler!")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

ana_program()
