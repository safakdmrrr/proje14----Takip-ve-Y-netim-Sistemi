from datetime import datetime

class Calisan:
    def __init__(self, ad):
        self.ad = ad
        self.gorevler = []

    def gorev_ata(self, gorev):
        self.gorevler.append(gorev)

class Gorev:
    def __init__(self, ad, sorumlu):
        self.ad = ad
        self.sorumlu = sorumlu
        self.ilermleme = 0

    def ilerleme_guncelle(self, ilerleme):
        self.ilermleme = ilerleme

class Proje:
    def __init__(self, ad, baslangic_tarihi, bitis_tarihi):
        self.ad = ad
        self.baslangic_tarihi = baslangic_tarihi
        self.bitis_tarihi = bitis_tarihi
        self.gorevler = []

    def gorev_ekle(self, gorev):
        self.gorevler.append(gorev)

def yeni_calisan_olustur():
    ad = input("Yeni çalışanın adını girin: ")
    return Calisan(ad)

def yeni_gorev_olustur():
    ad = input("Yeni görevin adını girin: ")
    calisan_ad = input("Görevi üstlenecek çalışanın adını girin: ")
    sorumlu = next((calisan for calisan in calisanlar if calisan.ad == calisan_ad), None)
    if sorumlu:
        return Gorev(ad, sorumlu)
    else:
        print("Hata: Belirtilen isimde bir çalışan bulunamadı.")
        return None

def ilerleme_guncelle(gorev):
    ilerleme = int(input("Görevin ilerleme yüzdesini girin: "))
    gorev.ilerleme_guncelle(ilerleme)

if __name__ == "__main__":
    calisanlar = []
    projeler = []

    while True:
        print("\n1. Yeni çalışan ekle")
        print("2. Yeni proje oluştur")
        print("3. Çalışana görev ata")
        print("4. Proje için görev ekle")
        print("5. Görev ilerlemesini güncelle")
        print("6. Çıkış")

        secim = input("Yapmak istediğiniz işlemi seçin: ")

        if secim == "1":
            calisan = yeni_calisan_olustur()
            calisanlar.append(calisan)
            print(f"{calisan.ad} adlı çalışan eklendi.")
        elif secim == "2":
            ad = input("Yeni proje adını girin: ")
            baslangic_tarihi = datetime.now()
            bitis_tarihi = input("Proje bitiş tarihini YYYY-MM-DD formatında girin: ")
            bitis_tarihi = datetime.strptime(bitis_tarihi, "%Y-%m-%d")
            proje = Proje(ad, baslangic_tarihi, bitis_tarihi)
            projeler.append(proje)
            print(f"{proje.ad} adlı proje oluşturuldu.")
        elif secim == "3":
            if calisanlar and projeler:
                calisan_ad = input("Görevi alacak çalışanın adını girin: ")
                calisan = next((calisan for calisan in calisanlar if calisan.ad == calisan_ad), None)
                if calisan:
                    proje_ad = input("Görev atanacak proje adını girin: ")
                    proje = next((proje for proje in projeler if proje.ad == proje_ad), None)
                    if proje:
                        gorev = yeni_gorev_olustur()
                        if gorev:
                            calisan.gorev_ata(gorev)
                            proje.gorev_ekle(gorev)
                            print(f"{gorev.ad} adlı görev {calisan.ad} adlı çalışana atanmıştır.")
                    else:
                        print("Hata: Belirtilen isimde bir proje bulunamadı.")
                else:
                    print("Hata: Belirtilen isimde bir çalışan bulunamadı.")
            else:
                print("Hata: Önce çalışan ve proje oluşturulmalıdır.")
        elif secim == "4":
            if projeler:
                proje_ad = input("Görev eklenecek proje adını girin: ")
                proje = next((proje for proje in projeler if proje.ad == proje_ad), None)
                if proje:
                    gorev = yeni_gorev_olustur()
                    if gorev:
                        proje.gorev_ekle(gorev)
                        print(f"{gorev.ad} adlı görev {proje.ad} adlı projeye eklenmiştir.")
                else:
                    print("Hata: Belirtilen isimde bir proje bulunamadı.")
            else:
                print("Hata: Önce proje oluşturulmalıdır.")
        elif secim == "5":
            if projeler:
                proje_ad = input("İlerleme güncellenecek proje adını girin: ")
                proje = next((proje for proje in projeler if proje.ad == proje_ad), None)
                if proje:
                    print("Görevler:")
                    for gorev in proje.gorevler:
                        print(gorev.ad)
                    gorev_ad = input("İlerleme güncellenecek görev adını girin: ")
                    gorev = next((gorev for gorev in proje.gorevler if gorev.ad == gorev_ad), None)
                    if gorev:
                        ilerleme_guncelle(gorev)
                        print(f"{gorev.ad} adlı görevin ilerlemesi güncellenmiştir.")
                    else:
                        print("Hata: Belirtilen isimde bir görev bulunamadı.")
                else:
                    print("Hata: Belirtilen isimde bir proje bulunamadı.")
            else:
                print("Hata: Önce proje oluşturulmalıdır.")
        elif secim == "6":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
