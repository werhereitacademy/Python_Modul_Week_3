# Görev listesi
gorevler = []

# Sıra numarası takipçisi
siradaki_numara = 1

# Görev ekleme fonksiyonu
def gorev_ekle(gorev_adi):
    global siradaki_numara
    gorev = {
        "sira": siradaki_numara,
        "ad": gorev_adi,
        "durum": "Bekliyor"
    }
    gorevler.append(gorev)
    print(f"Görev eklendi: {siradaki_numara} - {gorev_adi}")
    siradaki_numara += 1

# Görev tamamlama fonksiyonu
def gorev_tamamla(sira_no):
    for gorev in gorevler:
        if gorev["sira"] == sira_no and gorev["durum"] != "Silindi":
            gorev["durum"] = "Tamamlandı"
            print(f"Görev tamamlandı: {sira_no}")
            return
    print("Görev bulunamadı veya zaten silinmiş.")

# Görev silme fonksiyonu
def gorev_sil(sira_no):
    for gorev in gorevler:
        if gorev["sira"] == sira_no and gorev["durum"] != "Silindi":
            gorev["durum"] = "Silindi"
            print(f"Görev silindi: {sira_no}")
            return
    print("Görev bulunamadı veya zaten silinmiş.")

# Tamamlanan görevleri listeleme fonksiyonu
def tamamlanan_gorevleri_listele():
    tamamlananlar = list(filter(lambda g: g["durum"] == "Tamamlandı", gorevler))
    if not tamamlananlar:
        print("Tamamlanan görev yok.")
    else:
        for g in sorted(tamamlananlar, key=lambda x: x["sira"]):
            print(f'{g["sira"]}. {g["ad"]} - {g["durum"]}')

# Tüm görevleri listeleme fonksiyonu
def tum_gorevleri_listele():
    if not gorevler:
        print("Henüz hiç görev yok.")
    else:
        for g in sorted(gorevler, key=lambda x: x["sira"]):
            print(f'{g["sira"]}. {g["ad"]} - {g["durum"]}')

# Ana menü fonksiyonu
def ana_menu():
    while True:
        print("\nGörev Listesi Uygulaması")
        print("1. Görev Ekle")
        print("2. Görev Tamamla")
        print("3. Görev Sil")
        print("4. Tamamlanan Görevleri Listele")
        print("5. Tüm Görevleri Listele")
        print("6. Çıkış")
        print()
        # Kullanıcıdan seçim alma
        
        print("--"*30)
        secim = input("Seçiminizi yapın (1-6): ")
        print()
        # Seçim kontrolü
        
        if secim == "1":
            gorev_adi = input("Görev adını girin: ")
            gorev_ekle(gorev_adi)
        elif secim == "2":
            sira_no = int(input("Tamamlamak istediğiniz görev numarasını girin: "))
            gorev_tamamla(sira_no)
        elif secim == "3":
            sira_no = int(input("Silmek istediğiniz görev numarasını girin: "))
            gorev_sil(sira_no)
        elif secim == "4":
            tamamlanan_gorevleri_listele()
        elif secim == "5":
            tum_gorevleri_listele()
        elif secim == "6":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")          
ana_menu()
