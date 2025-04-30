# Görev Yönetim Sistemi
#1- Yeni bir görev ekle
#2- Bir görevi tamamla
#3- Bir görevi sil
#4- Tamamlanan görevleri listele
#5- Tüm görevleri durumlarıyla birlikte listele
#6- Çıkış

gorev_listesi = []
def add_gorev(ID, gorev_tanimi, gorev_durumu):
    """
    Yeni bir görev ekler.
    """
    gorev_bilgileri = {
        "ID": ID,
        "Görev Tanınım": gorev_tanimi,
        "Görev Durumu": gorev_durumu
    }
    gorev_listesi.append(gorev_bilgileri)
    return gorev_listesi

def menu():
    """
    Kullanıcıdan seçim alır.
    """
    print("***Görev Yönetim Sistemi***\n")
    print("1- Yeni bir görev ekle")
    print("2- Bir görevi durumunu değiştir")
    print("3- Bir görevi sil")
    print("4- Tamamlanan görevleri listele")
    print("5- Tüm görevleri durumlarıyla birlikte listele")
    print("6- Çıkış\n")

    secim = input("Seçiminizi yapın (1-6): ")
    if secim not in ["1", "2", "3", "4", "5", "6"]:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
        return menu()
    return secim

def uygun_id_al():
    mevctut_idler = sorted([int(gorev["ID"]) for gorev in gorev_listesi])
    for ID in range(1, len(mevctut_idler) + 2):
        if ID not in mevctut_idler:
            return str(ID)
        
    """
    Kullanıcıdan uygun bir ID alır.
    """

#1- Yeni bir görev ekle
while True:
    menu_secim = menu()
    if menu_secim == "1":
        #ID = input("Görev ID'sini girin: ")
        ID = uygun_id_al()
        if any(gorev["ID"] == ID for gorev in gorev_listesi):
            print("Bu ID'ye sahip bir görev zaten var. Lütfen başka bir ID girin.")
            continue
        # Görev tanımını ve durumunu al
        gorev_tanimi = input("Görev tanımını girin: ")
        gorev_durumu = input("Görev durumunu girin (Tamamlandı/Bekliyor/Silindi): ")
        if gorev_durumu not in ["Tamamlandı", "Bekliyor", "Silindi"]:
            print("Geçersiz görev durumu. Lütfen tekrar deneyin.")
            continue
        # Görev ekleme fonksiyonunu çağır
        add_gorev(ID, gorev_tanimi, gorev_durumu)
        print("Görev başarıyla eklendi.")
    elif menu_secim == "2":
        ID = input("Durumu değiştirmek istediğiniz görev ID'sini girin: ")
        if any(gorev["ID"] == ID for gorev in gorev_listesi):
            #print("Bu ID bulundu.") 
            # Görev durumunu güncelle
            gorev_durumu = input("Görev durumunu girin (Tamamlandı/Bekliyor/Silindi): ")
            if gorev_durumu not in ["Tamamlandı", "Bekliyor", "Silindi"]:
                print("Geçersiz görev durumu. Lütfen tekrar deneyin.")
                continue
            else:
                for gorev in gorev_listesi:
                    if gorev["ID"] == ID:
                        gorev["Görev Durumu"] = gorev_durumu
                        print("Görev durumu başarıyla güncellendi.")
        else:
            print("Bu ID'ye sahip bir görev bulunamadı.")
            continue
    
    elif menu_secim == "3":
        ID = input("Silmek istediğiniz görev ID'sini girin: ")
        if any(gorev["ID"] == ID for gorev in gorev_listesi):
            #print("Bu ID bulundu.") 
            # Görev silme işlemi
            for gorev in gorev_listesi:
                if gorev["ID"] == ID:
                    gorev_listesi.remove(gorev)
                    print("Görev başarıyla silindi.")
        else:
            print("Bu ID'ye sahip bir görev bulunamadı.")
            continue
 
    elif menu_secim == "4":
        # Tamamlanan görevleri listele
        tamamlanan_gorevler = [gorev for gorev in gorev_listesi if gorev["Görev Durumu"] == "Tamamlandı"]
        if tamamlanan_gorevler:
            print("Tamamlanan Görevler:")
            for gorev in tamamlanan_gorevler:
                print(f"ID: {gorev['ID']}, Görev Tanımı: {gorev['Görev Tanınım']}, Görev Durumu: {gorev['Görev Durumu']}")
        else:
            print("Tamamlanan görev bulunamadı.")
 
    elif menu_secim == "5":
        # Tüm görevleri listele
        if gorev_listesi:
            print("Tüm Görevler:\n")
            for gorev in gorev_listesi:
                print(f"ID: {gorev['ID']}, Görev Tanımı: {gorev['Görev Tanınım']}, Görev Durumu: {gorev['Görev Durumu']}\n")
        else:
            print("Görev listesi boş.")

    elif menu_secim == "6":
 
        print("Çıkış yapılıyor... İyi günler!")
        break
    else:
        print("Bu özellik henüz uygulanmadı.")


