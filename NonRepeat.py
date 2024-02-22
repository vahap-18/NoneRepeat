import time

print(
    """
    ███████████████████████████████████████████
    █─██─█────█─██─█────█───█────█───█────█───█
    █──█─█─██─█──█─█─██─█─███─██─█─███─██─██─██
    █─█──█─██─█─█──█────█───█────█───█────██─██
    █─██─█─██─█─██─█─█─██─███─████─███─██─██─██
    █─██─█────█─██─█─█─██───█─████───█─██─██─██
    ███████████████████████████████████████████
    Author: A.Vahap Doğan

    Bu program verilen bir dosya içerisindeki listede tekrarlanan cümleleri siler.
    NOT: Programda kullanılacak dosyanın programın bulunduğu dosya yolu ile aynı olması gerekir ve dosya formatı yazılmalıdır.
    """)

def tekrarlari_sil(cumleler):
    temiz_cumleler = []
    for cumle in cumleler:
        if cumle not in temiz_cumleler:
            temiz_cumleler.append(cumle)
    return temiz_cumleler

def main():
    """
    Programın ana kontrol noktasıdır. Kullanıcıdan bir dosya adı alır,
    belirtilen dosyadaki cümleleri okur, tekrarlananları siler ve temizlenmiş
    cümleleri ekrana yazdırır.
    """
    dosya_konumu = input("Lütfen dosyanın tam konumunu girin: ")

    try:
        with open(dosya_konumu, 'r', encoding='utf-8') as dosya:
            cumleler = dosya.readlines()
            print("Fazlalıklardan arındırılıyorsun...")
            time.sleep(3)  # 3 saniye bekleme süresi
    except FileNotFoundError:
        print("Belirtilen dosya bulunamadı.")
        return

    # Dosyadan okunan satırlardaki yeni satır karakterlerini kaldırma
    cumleler = [cumle.strip() for cumle in cumleler]

    temiz_cumleler = tekrarlari_sil(cumleler)

    print("\nTekrarları Silinmiş Cümleler:")
    for cumle in temiz_cumleler:
        print(cumle)

if __name__ == "__main__":
    main()