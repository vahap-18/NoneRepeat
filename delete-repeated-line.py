import os
import time

def tekrarlari_sil(cumleler):
    """
    Tekrar eden cümleleri siler.
    Büyük/küçük harf duyarlılığı olmadan çalışır.
    """
    temiz_cumleler = []
    for cumle in cumleler:
        if cumle.lower() not in [c.lower() for c in temiz_cumleler]:  # Büyük/küçük harf duyarlılığı olmadan kontrol
            temiz_cumleler.append(cumle)
    return temiz_cumleler

def dosya_konumu_gir():
    """
    Kullanıcıdan dosya konumu alır ve geçerli olup olmadığını kontrol eder.
    Geçersizse kullanıcıya tekrar deneme veya çıkış yapma seçeneği sunar.
    """
    while True:
        dosya_konumu = input("Lütfen dosyanın tam konumunu girin (çıkmak için 'q' yazın): ")
        if dosya_konumu.lower() == 'q':
            return None
        if os.path.isfile(dosya_konumu):
            return dosya_konumu
        else:
            print("Belirtilen dosya bulunamadı. Tekrar deneyin.")

def dosyaya_kaydet(cumleler, orijinal_dosya):
    """
    Tekrarları silinmiş cümleleri yeni bir dosyaya kaydeder.
    Kullanıcıya dosyayı yeni bir isimle kaydetme seçeneği sunar.
    """
    yeni_dosya = input("Temizlenmiş cümleleri kaydetmek için yeni dosya adını girin (orijinali güncellemek için Enter'a basın): ")
    if not yeni_dosya:
        yeni_dosya = orijinal_dosya

    with open(yeni_dosya, 'w', encoding='utf-8') as dosya:
        for cumle in cumleler:
            dosya.write(cumle + "\n")
    print(f"Cümleler başarıyla '{yeni_dosya}' dosyasına kaydedildi.")

def main():
    print("""
    ███████████████████████████████████████████
    █─██─█────█─██─█────█───█────█───█────█───█
    █──█─█─██─█──█─█─██─█─███─██─█─███─██─██─██
    █─█──█─██─█─█──█────█───█────█───█────██─██
    █─██─█─██─█─██─█─█─██─███─████─███─██─██─██
    █─██─█────█─██─█─█─██───█─████───█─██─██─██
    ███████████████████████████████████████████
    Author: A.Vahap Doğan
    
    Bu program, bir dosyadaki tekrar eden cümleleri siler.
    Dosya yolunu girin ve işlemi başlatın.
    """)

    dosya_konumu = dosya_konumu_gir()
    if dosya_konumu is None:
        print("Programdan çıkılıyor...")
        return

    try:
        with open(dosya_konumu, 'r', encoding='utf-8') as dosya:
            cumleler = dosya.readlines()
            print("Fazlalıklardan arındırılıyor...")
            for i in range(1, 101, 20):
                print(f"İşlem ilerlemesi: %{i}")
                time.sleep(0.5)
    except FileNotFoundError:
        print("Belirtilen dosya bulunamadı.")
        return

    cumleler = [cumle.strip() for cumle in cumleler]  # Satır başı ve sonu boşlukları temizle
    temiz_cumleler = tekrarlari_sil(cumleler)

    print("\nTekrarları Silinmiş Cümleler:")
    for cumle in temiz_cumleler:
        print(cumle)

    dosyaya_kaydet(temiz_cumleler, dosya_konumu)

if __name__ == "__main__":
    main()
