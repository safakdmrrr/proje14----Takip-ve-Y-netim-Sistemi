import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QComboBox
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

class CalisanEklemePenceresi(QWidget):
    def __init__(self, ana_pencere):
        super().__init__()
        self.ana_pencere = ana_pencere
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Çalışan Ekle')
        layout = QVBoxLayout()

        self.ad_label = QLabel("Çalışan Adı:")
        self.ad_input = QLineEdit()
        layout.addWidget(self.ad_label)
        layout.addWidget(self.ad_input)

        self.kaydet_button = QPushButton("Kaydet")
        self.kaydet_button.clicked.connect(self.kaydet)
        layout.addWidget(self.kaydet_button)

        self.setLayout(layout)

    def kaydet(self):
        ad = self.ad_input.text()
        if ad.strip():
            self.ana_pencere.calisan_ekle(ad)
            self.close()
        else:
            print("Hata: Lütfen geçerli bir çalışan adı girin.")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.calisanlar = []
        self.projeler = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('İş Takip ve Yönetim Sistemi')
        layout = QVBoxLayout()

        self.calisanlar_label = QLabel("Çalışanlar:")
        self.calisanlar_combobox = QComboBox()
        layout.addWidget(self.calisanlar_label)
        layout.addWidget(self.calisanlar_combobox)

        self.proje_label = QLabel("Proje Adı:")
        self.proje_input = QLineEdit()
        layout.addWidget(self.proje_label)
        layout.addWidget(self.proje_input)

        self.gorev_label = QLabel("Görev Adı:")
        self.gorev_input = QLineEdit()
        layout.addWidget(self.gorev_label)
        layout.addWidget(self.gorev_input)

        self.ilerleme_label = QLabel("İlerleme:")
        self.ilerleme_input = QLineEdit()
        layout.addWidget(self.ilerleme_label)
        layout.addWidget(self.ilerleme_input)

        self.calisan_ekle_button = QPushButton("Çalışan Ekle")
        self.calisan_ekle_button.clicked.connect(self.ac_calisan_ekleme_penceresi)
        layout.addWidget(self.calisan_ekle_button)

        self.proje_olustur_button = QPushButton("Proje Oluştur")
        self.proje_olustur_button.clicked.connect(self.proje_olustur)
        layout.addWidget(self.proje_olustur_button)

        self.gorev_ata_button = QPushButton("Görev Ata")
        self.gorev_ata_button.clicked.connect(self.gorev_ata)
        layout.addWidget(self.gorev_ata_button)

        self.setLayout(layout)
        self.show()

    def calisan_ekle(self, ad):
        self.calisanlar.append(ad)
        self.calisanlar_combobox.addItem(ad)

    def proje_olustur(self):
        ad = self.proje_input.text()
        baslangic_tarihi = datetime.now()
        bitis_tarihi = datetime.now()  # Burada bitiş tarihini elle girmeniz gerekir.
        proje = Proje(ad, baslangic_tarihi, bitis_tarihi)
        self.projeler.append(proje)
        self.proje_input.clear()

    def gorev_ata(self):
        calisan_ad = self.calisanlar_combobox.currentText()
        calisan = next((calisan for calisan in self.calisanlar if calisan == calisan_ad), None)
        proje_ad = self.proje_input.text()
        proje = next((proje for proje in self.projeler if proje.ad == proje_ad), None)
        if calisan and proje:
            gorev = Gorev(self.gorev_input.text(), calisan)
            calisan.gorev_ata(gorev)
            proje.gorev_ekle(gorev)
            self.gorev_input.clear()
        else:
            print("Hata: Belirtilen çalışan veya proje bulunamadı.")

    def ac_calisan_ekleme_penceresi(self):
        self.calisan_ekleme_penceresi = CalisanEklemePenceresi(self)
        self.calisan_ekleme_penceresi.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
