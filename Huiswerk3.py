# Soru 1: Görev Yöneticisi Uygulaması
# Proje Açıklaması: Bu ödevde, Python programlama dilini kullanarak bir görev yöneticisi uygulaması oluşturacaksınız. 
# Bu uygulama kullanıcıların görevlerini eklemelerine, tamamlamalarına, silmelerine ve listelemelerine olanak tanıyacaktır.

# Gereksinimler:
# 1- Görevler bir Python listesinde saklanacak ve her görev bir sözlük olarak temsil edilecektir. 
# Her görevin aşağıdaki özelliklere sahip olması gerekir:

# Sıra Numarası (Otomatik olarak atanır)

# Görev Adı

# Durum (Tamamlandı, Bekliyor veya Silindi)

# 2- Kullanıcının yapabileceği işlemler:

# Yeni bir görev ekle

# Bir görevi tamamla

# Bir görevi sil

# Tamamlanan görevleri listele

# Tüm görevleri durumlarıyla birlikte listeleyin

# Çıkış

# 3- Görevler eklenme sırasına göre otomatik olarak sıra numarası almalıdır.

# 4- Silinen görev numaralarının yerine yeni görevler kaydedilmeli.

# 5- Görevler listelenirken sıra numarasına göre sıralanmalıdır.

# 6- Her işlemden sonra kullanıcıya uygun geri bildirim verilmelidir. Örneğin, yeni bir görev eklendiğinde, 
# görevin eklendiğini belirten bir mesaj görmelidir.


# Görevler listesi ve sıra numarası
gorevler = []
gorev_id_sirasi = 1

# Yeni görev ekleme fonksiyonu
def gorev_ekle(gorev_adi):
    global gorev_id_sirasi
    gorev = {
        "id": gorev_id_sirasi,
        "adi": gorev_adi,
        "durum": "Bekliyor"
    }
    gorevler.append(gorev)
    gorev_id_sirasi += 1
    print(f"Görev eklendi: {gorev_adi} (ID: {gorev['id']})")

# Görev tamamlama fonksiyonu
def gorev_tamamla(gorev_id):
    for gorev in gorevler:
        if gorev["id"] == gorev_id and gorev["durum"] == "Bekliyor":
            gorev["durum"] = "Tamamlandı"
            print(f"Görev tamamlandı: {gorev['adi']} (ID: {gorev_id})")
            return
    print(f"Tamamlanacak görev bulunamadı (ID: {gorev_id})")

# Görev silme fonksiyonu
def gorev_sil(gorev_id):
    for gorev in gorevler:
        if gorev["id"] == gorev_id and gorev["durum"] != "Silindi":
            gorev["durum"] = "Silindi"
            print(f"Görev silindi: {gorev['adi']} (ID: {gorev_id})")
            return
    print(f"Silinecek görev bulunamadı (ID: {gorev_id})")

# Tamamlanan görevleri listeleme fonksiyonu
def tamamlanan_gorevleri_listele():
    tamamlananlar = [gorev for gorev in gorevler if gorev["durum"] == "Tamamlandı"]
    if tamamlananlar:
        print("Tamamlanan Görevler:")
        for gorev in tamamlananlar:
            print(f"{gorev['id']}. {gorev['adi']} (Durum: {gorev['durum']})")
    else:
        print("Tamamlanan")