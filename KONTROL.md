# Uygulama kontrol notları

Tarih: 21 Eylül 2026.

## İçerik bütünlüğü

- 5.946 kelime kaydı uygulamaya alındı; ana kelime dosyasıyla aynı.
- 39 dersin başlık, açıklama, kullanım, yapı, örnek, dikkat notu, karşılaştırma ve cevap alanları kontrol edildi.
- 12 zamanın her birinde 15 çevirili örnek var: toplam 180.
- Bütün derslerde 376 örnek, 60 fiilde 180 örnek ve 4 okumada 24 cümle bulunuyor.
- 60 fiilin tamamı mevcut sözlükte doğru fiil kaydına bağlandı.
- 205 alıştırma var. Boş cevap, yinelenen ders/soru kimliği, boş çeviri ve bozuk karakter kontrolleri geçti.
- Kelime verisinin önceki kontrol kapsamı üst dizindeki kontrol_raporu.md dosyasındadır. Bu aşama bütün kelime örneklerinin yeniden bağımsız dil uzmanı incelemesi değildir.

## Çalışma davranışı

TypeScript kontrolü ve üretim derlemesi geçti. Anlamlı otomatik kontroller şunları kapsıyor:

- Sık kısaltmalar, büyük harf ve noktalama; yanlış fiil veya olumsuzluk farkının yanlışlıkla kabul edilmemesi.
- Tekrarı gelenlerin önceliği, gelecekteki kartların dışarıda tutulması ve tekrar etmeyen kart kimlikleri.
- Kullanıcı kimliği olmadan kayıt reddi, kullanıcılar arası veri ayrımı.
- Kalıcı kayıt ve yeniden okuma; aynı istek kimliğinin tekrar gönderilmesinde çift sayım olmaması.
- Tekrar aralıkları, yanlış cevabın düzeltilmesi, kendini değerlendirme ve ders tamamlama.
- Geçersiz kelime/soru/boş cevap reddi.

Yerel tarayıcıda bütün menüler açıldı. Dersin anlatım ve örnek sekmeleri, kelime arama ve detay, fiil detayındaki V1/V2/V3, okuma çevirisi ve metindeki kelimeye dokunma kontrol edildi. 390×844 görünümde mobil menü, kelime listesi ve cümle sıralama ekranı incelendi. Beş sözcükten cümle kurup kaydetme akışı çalıştırıldı ve doğru cevap geri bildirimi doğrulandı. Geçici ekran boyutu ayarı geri alındı.

WebMCP kelime arama ve ders açma araçlarının geçerli girişleri, görünür sonucu ve geçersiz giriş reddi kontrol edildi.

## Açık sınırlar

- Seslendirme cihazın tarayıcı seslerine bağlıdır; insan kaydı değildir. Her cihazdaki sesin telaffuzu ayrı ayrı doğrulanmadı.
- Açık uçlu cevaplar kayıtlı alternatiflerle karşılaştırılır. Anlam bakımından tüm doğru cümleleri otomatik tanıyan bir yapay zekâ değerlendirmesi yoktur; kullanıcı kendi alternatifini karşılaştırıp doğru olarak işaretleyebilir.
- Yerel önizleme ile yayımlanan uygulamanın kayıtları ayrı veritabanlarındadır. Test kullanıcıları ve yerel deneme kayıtları yayına taşınmaz.
- İçerikler teknik kontroller ve editoryal gözden geçirmeden geçirildi; hatasızlık garantisi verilmez.
