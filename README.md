# Tekrar Eden Cümleleri Temizleyen Python Programı

Bu Python programı, verilen bir metin dosyasındaki tekrar eden cümleleri tespit ederek temizler ve kullanıcının isteğine bağlı olarak sonucu kaydeder. Program büyük/küçük harf duyarlılığı olmadan çalışır, yani "Merhaba" ve "merhaba" gibi cümleler tekrar olarak kabul edilir.

## Özellikler

- **Dosya Okuma**: Kullanıcının belirttiği bir metin dosyasını okur.
- **Tekrar Silme**: Tekrar eden cümleleri tespit eder ve bunları temizler.
- **Büyük/Küçük Harf Duyarlılığı**: Cümlelerin karşılaştırılmasında büyük/küçük harf farkı gözetmez.
- **Dosya Kaydetme**: Temizlenmiş cümleler ya mevcut dosyaya kaydedilir ya da kullanıcı tarafından belirtilen yeni bir dosyaya yazılır.
- **İlerleme Göstergesi**: Temizleme işlemi sırasında ilerleme gösterilir.
- **Kullanıcı Dostu Geri Bildirim**: Hatalı dosya adı veya işlem sırasında kullanıcıya geri bildirim verilir ve yeniden deneme imkânı sunulur.

## Kullanım

1. **Programı Başlatma**: Program çalıştırıldığında kullanıcıdan dosya yolu istenir. Bu dosya, programın bulunduğu dizinde olmalı ya da tam dosya yolu belirtilmelidir.
   
2. **Dosya Yolu Girişi**: Programın istediği dosya yolunu doğru biçimde girin. Eğer dosya bulunamazsa, kullanıcıya yeniden deneme veya çıkma seçeneği sunulur.

3. **Cümleleri Temizleme**: Program dosyayı okur ve tekrar eden cümleleri siler.

4. **Sonucu Kaydetme**: Program, sonucu mevcut dosyaya yazma veya yeni bir dosya olarak kaydetme seçeneği sunar.

## Örnek

Bir dosyanın tam yolunu girdikten sonra program şu adımları takip eder:

1. Dosya içeriğini okur.
2. Tekrar eden cümleleri temizler.
3. Sonuçları ekrana yazdırır.
4. Dosyayı günceller veya yeni dosya olarak kaydeder.

## Gereksinimler

Bu programda herhangi bir dış kütüphane kullanılmamıştır. Python 3.x sürümüyle çalışır.

## Çalıştırma

```bash
python program.py
