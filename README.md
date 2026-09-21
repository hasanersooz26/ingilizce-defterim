# İngilizce Defterim

Kişisel İngilizce çalışma uygulaması. Türkçe açıklamalarla kelime tekrarı, dil bilgisi, okuma, dinleme ve cümle pratiği sunar. CEFR alanı veya A1–B2 sınıflaması kullanılmaz.

## İçerik

- 5.946 kelime kaydı; asıl words.json dosyasının aynı kopyası.
- 39 ders: 12 zaman, 10 yardımcı fiil konusu, 10 dil bilgisi konusu, 4 kalıp konusu ve 3 sık karıştırılan kelime konusu.
- Zaman başına 15 örnek; derslerde toplam 376 İngilizce–Türkçe örnek.
- 60 fiil, her birinde V1/V2/V3, üç çevirili örnek ve sözlük bağlantısı.
- 4 okuma/diyalog, 24 çevirili cümle.
- 205 alıştırma: cümle yazma, boşluk doldurma, fiil biçimi, 12 kelime sıralama ve 12 olumsuz/soru dönüşümü.

## Nasıl çalışır?

Günlük akış 10 kelime, 1 konu ve 3 soru önerir. Tekrar edilecek kelimeler önce gelir; sonra yeni kelimeler seçilir. Tekrar edelim 10 dakika, zorlandım 1 gün; hatırladım yanıtı 1, 3, 7, 14, 30 ve 60 günlük aralıklara ilerler. Bu anlaşılır bir tekrar planıdır; öğrenme garantisi veya kişiye göre doğrulanmış bir optimizasyon değildir.

İlerleme, yanlışlar ve ders tamamlamaları D1 üzerinde kullanıcıya göre saklanır. localStorage yalnızca cihazın dinleme tercihini saklar. Son 7 gün, İstanbul tarihine göre hesaplanır. Aynı işlem kimliğiyle yeniden gönderilen kayıt iki kez sayılmaz. Yanlış cevap doğru yanıtlandığında aktif yanlışlar listesinden çıkar; geçmişte kaç kez zorlanıldığı korunur.

Cevap kontrolü deterministiktir. Noktalama, büyük harf, yaygın kısaltmalar ve kayıtlı alternatifler kabul edilir. Açık uçlu cevaplarda tüm eşanlamlı ifadeleri anlayan bir yapay zekâ puanlaması yoktur. Kullanıcı model cevaplarla karşılaştırıp kendi doğru alternatifini işaretleyebilir. Bu özellik açıkça kendini değerlendirme olarak sunulur.

Seslendirme tarayıcının SpeechSynthesis desteğini kullanır; İngiliz/Amerikan tercihi ve yavaş dinleme vardır. Ses kalitesi ve mevcut sesler cihaza bağlıdır. İnsan ses kaydı veya konuşma puanlama özelliği yoktur.

## Geliştirme

Node.js 22.13 veya üzeri gerekir. Kurulum: npm run install:ci. Geliştirme: npm run dev. Derleme: npm run build. Derlenmiş Worker kontrolü: npm run start.

Yerel giriş, starter'ın yalnızca loopback geliştirme ortamında etkin olan giriş benzetimiyle yapılır. Yayında Sites özel erişimi ve yönlendirdiği kullanıcı kimliği kullanılır. Kullanıcı kimliğini tarayıcı verisinden kabul eden bir uygulama yolu yoktur.

Yeni veritabanında drizzle/0000_tearful_payback.sql uygulanır. Yayında migration'ı Sites uygular. Yerelde derlemeden sonra:

node --import ./scripts/sites-env.mjs ./node_modules/wrangler/bin/wrangler.js d1 execute DB --local --config dist/server/wrangler.json --persist-to .wrangler/state --file drizzle/0000_tearful_payback.sql

Aynı migration'ı aynı veritabanına tekrar uygulamayın. Yeni değişikliklerde npm run db:generate ile yeni migration ekleyin.

## Kontroller

- node node_modules/typescript/bin/tsc --noEmit
- node --experimental-strip-types --test tests/study.test.mjs
- Yerel derlenmiş Worker 8787 portunda çalışırken node tests/api-check.mjs. Bu test ayrı bir QA kullanıcı kimliğiyle yalnızca yerel veritabanına yazar.

İçerik üretimi: Python ile content/build-content.py ve content/build-verbs.py. Hazır JSON'lar uygulamayla birlikte tutulur; uygulamayı kullanmak için Python gerekmez.

## Kaynak ve kapsam

Kelime verisi kullanıcının sağladığı KelimeLog HTML dosyasından düzenlenmiştir. Önceki kontrol kapsamı üst dizindeki kontrol_raporu.md dosyasındadır. Resmî Oxford kapsamı iddiası yapılmaz.

Dersler, çeviriler ve alıştırmalar bu uygulama için yazıldı. Kullanım ayrımları için başvurulan kaynaklar:

- https://dictionary.cambridge.org/grammar/british-grammar/could
- https://dictionary.cambridge.org/grammar/british-grammar/modality-tense
- https://dictionary.cambridge.org/grammar/british-grammar/modality-meanings-and-uses
- https://learnenglish.britishcouncil.org/free-resources/grammar/b1-b2/future-continuous-future-perfect
- https://downloads.bbc.co.uk/learningenglish/intermediate/unit30/b2_u30_6min_grammar_future_perfect_continuous.pdf

Örnekler bu kaynaklardan topluca kopyalanmadı. Teknik içerik kontrolleri bağımsız bir uzman tarafından her cümlenin incelendiği anlamına gelmez.
