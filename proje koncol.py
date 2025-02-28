# Kullanıcı verilerini saklamak için değişkenler
ad = None
cinsiyet = None
yas = None
toplam_kolesterol = None
hdl_kolesterol = None
sistolik_kan_basinci = None
sigara_kullanimi = None
diyabet_durumu = None
tansiyon_ilaci = None

while True:
    # Ana Menü
    print("\n🏥 Kalp Sağlığı Risk Değerlendirme Sistemi")
    print("1. Yeni Kullanıcı Ekle")
    print("2. Risk Hesapla")
    print("3. Çıkış")
    
    secim = input("Seçiminizi yapın (1-3): ")

    if secim == "1":
        # Kullanıcıdan verileri al
        ad = input("Adınızı girin: ")
        cinsiyet = input("Cinsiyetinizi girin (Erkek/Kadın): ").lower()
        yas = int(input("Yaşınızı girin: "))
        toplam_kolesterol = float(input("Toplam kolesterol (mg/dl): "))
        hdl_kolesterol = float(input("HDL kolesterol (mg/dl): "))
        sistolik_kan_basinci = int(input("Sistolik kan basıncı (mmHg): "))

        # Sigara kullanımı
        sigara = input("Sigara kullanıyor musunuz? (Evet/Hayır): ").lower()
        sigara_kullanimi = 1 if sigara == "evet" else 0

        # Diyabet durumu
        diyabet = input("Şeker hastası mısınız? (Evet/Hayır): ").lower()
        diyabet_durumu = 1 if diyabet == "evet" else 0

        # Tansiyon ilacı kullanımı
        tansiyon = input("Tansiyon ilacı kullanıyor musunuz? (Evet/Hayır): ").lower()
        tansiyon_ilaci = 1 if tansiyon == "evet" else 0

        print("\n✅ Kullanıcı verileri alındı. Şimdi risk hesaplamaya geçebilirsiniz.")

    elif secim == "2":
        # Eğer kullanıcı veri girmediyse hata vermesin
        if None in (ad, cinsiyet, yas, toplam_kolesterol, hdl_kolesterol, sistolik_kan_basinci, sigara_kullanimi, diyabet_durumu, tansiyon_ilaci):
            print("⚠ Lütfen önce 'Yeni Kullanıcı Ekle' seçeneğini kullanarak veri girin!")
            continue

        # Risk hesaplama fonksiyonu
        def hesapla_risk(cinsiyet, toplam_puan):
            if cinsiyet == "erkek":
                risk = 1 - (0.9402 ** toplam_puan)
            else:  # Kadınlar için
                risk = 1 - (0.98767 ** toplam_puan)
            return risk

        # Risk seviyesini belirleme fonksiyonu
        def risk_seviyesi_belirle(risk_orani):
            if risk_orani < 0.10:
                return "Düşük"
            elif risk_orani < 0.20:
                return "Orta"
            else:
                return "Yüksek"

        # Toplam puanı hesaplama (basitleştirilmiş formül)
        toplam_puan = (yas / 10) + (toplam_kolesterol / 50) + (hdl_kolesterol / 40) + (sistolik_kan_basinci / 120) + sigara_kullanimi + diyabet_durumu + tansiyon_ilaci

        # Risk hesaplama
        risk_orani = hesapla_risk(cinsiyet, toplam_puan)

        # Risk seviyesini belirleme
        sonuc = risk_seviyesi_belirle(risk_orani)

        # Kullanıcıya sonucu gösterme
        print("\n📌 Kullanıcı Bilgileri:")
        print(f"Ad: {ad}, Yaş: {yas}, Cinsiyet: {cinsiyet.capitalize()}")
        print(f"Kolesterol: {toplam_kolesterol} mg/dl, HDL: {hdl_kolesterol} mg/dl")
        print(f"Sistolik Kan Basıncı: {sistolik_kan_basinci} mmHg")
        print(f"Sigara Kullanımı: {'Evet' if sigara_kullanimi else 'Hayır'}")
        print(f"Diyabet: {'Evet' if diyabet_durumu else 'Hayır'}")
        print(f"Tansiyon İlacı Kullanımı: {'Evet' if tansiyon_ilaci else 'Hayır'}")

        # Risk sonucunu yazdırma
        print(f"\n🔍 Risk Oranınız: %{round(risk_orani * 100, 2)}")
        print(f"📊 Risk Seviyeniz: {sonuc}")

    elif secim == "3":
        print("\n📌 Programdan çıkılıyor... Teşekkürler!")
        break  # Döngüyü kır ve çıkış yap

    else:
        print("\n⚠ Hatalı giriş yaptınız! Lütfen 1, 2 veya 3 seçin.")
