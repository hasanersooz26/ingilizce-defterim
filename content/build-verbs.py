import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
words=json.loads((root/'public'/'words.json').read_text(encoding='utf-8-sig'))
raw="""be|was / were|been|olmak|I am ready.|Hazırım.|We were tired yesterday.|Dün yorgunduk.|I have been to London.|Londra'da bulundum.
have|had|had|sahip olmak; yemek yemek|I have breakfast at seven.|Saat yedide kahvaltı yaparım.|I had breakfast early.|Erken kahvaltı yaptım.|I have had breakfast.|Kahvaltı yaptım.
do|did|done|yapmak|I do my homework after school.|Ödevimi okuldan sonra yaparım.|I did my homework yesterday.|Dün ödevimi yaptım.|I have done my homework.|Ödevimi bitirdim.
go|went|gone|gitmek|I go to work by bus.|İşe otobüsle giderim.|I went to work early.|İşe erken gittim.|She has gone home.|O eve gitti; henüz dönmedi.
come|came|come|gelmek|I come here every week.|Her hafta buraya gelirim.|I came here yesterday.|Dün buraya geldim.|He has come to help us.|Bize yardım etmeye geldi.
get|got|got / gotten|almak; edinmek; hâle gelmek|I get many emails.|Çok e-posta alırım.|I got your message.|Mesajını aldım.|I have got better at cooking.|Yemek yapmada daha iyi hâle geldim.
make|made|made|yapmak; üretmek|I make coffee every morning.|Her sabah kahve yaparım.|I made a cake yesterday.|Dün kek yaptım.|I have made a mistake.|Bir hata yaptım.
take|took|taken|almak; götürmek|I take the bus to work.|İşe otobüsle giderim.|I took a photo.|Bir fotoğraf çektim.|I have taken your advice.|Tavsiyene uydum.
give|gave|given|vermek|I give my cat food every morning.|Her sabah kedime mama veririm.|I gave her a book.|Ona bir kitap verdim.|I have given him my number.|Ona numaramı verdim.
see|saw|seen|görmek|I see my friends on Sundays.|Pazar günleri arkadaşlarımla görüşürüm.|I saw Ece yesterday.|Dün Ece'yi gördüm.|I have seen this film.|Bu filmi izledim.
know|knew|known|bilmek; tanımak|I know the answer.|Cevabı biliyorum.|I knew the answer yesterday.|Dün cevabı biliyordum.|I have known her for years.|Onu yıllardır tanıyorum.
think|thought|thought|düşünmek; sanmak|I think it is useful.|Bence bu faydalı.|I thought you were at home.|Evde olduğunu sanmıştım.|I have thought about your idea.|Fikrin hakkında düşündüm.
say|said|said|söylemek; demek|I say hello to my neighbours.|Komşularıma selam veririm.|I said hello to him.|Ona selam verdim.|I have said enough.|Yeterince şey söyledim.
tell|told|told|anlatmak; söylemek|I tell my sister everything.|Kız kardeşime her şeyi anlatırım.|I told her the news.|Ona haberi söyledim.|I have told you the truth.|Sana gerçeği söyledim.
find|found|found|bulmak|I find this book helpful.|Bu kitabı faydalı buluyorum.|I found my keys.|Anahtarlarımı buldum.|I have found a new job.|Yeni bir iş buldum.
feel|felt|felt|hissetmek|I feel happy today.|Bugün mutlu hissediyorum.|I felt tired yesterday.|Dün yorgun hissettim.|I have felt better since Monday.|Pazartesiden beri kendimi daha iyi hissediyorum.
leave|left|left|ayrılmak; bırakmak|I leave home at eight.|Evden saat sekizde çıkarım.|I left my phone at home.|Telefonumu evde bıraktım.|She has left the office.|O ofisten ayrıldı.
put|put|put|koymak|I put my keys on the shelf.|Anahtarlarımı rafa koyarım.|I put the bag on the table.|Çantayı masanın üstüne koydum.|I have put the milk in the fridge.|Sütü buzdolabına koydum.
bring|brought|brought|getirmek|I bring lunch from home.|Öğle yemeğimi evden getiririm.|I brought some fruit.|Biraz meyve getirdim.|I have brought your book.|Kitabını getirdim.
eat|ate|eaten|yemek|I eat vegetables every day.|Her gün sebze yerim.|I ate soup for lunch.|Öğle yemeğinde çorba içtim.|I have already eaten.|Zaten yemek yedim.
drink|drank|drunk|içmek|I drink water with my meals.|Yemeklerle birlikte su içerim.|I drank tea this morning.|Bu sabah çay içtim.|I have drunk enough water today.|Bugün yeterince su içtim.
sleep|slept|slept|uyumak|I sleep for eight hours.|Sekiz saat uyurum.|I slept well last night.|Dün gece iyi uyudum.|I have slept in a tent before.|Daha önce çadırda uyudum.
write|wrote|written|yazmak|I write in my notebook.|Defterime yazarım.|I wrote a letter yesterday.|Dün bir mektup yazdım.|I have written three emails.|Üç e-posta yazdım.
read|read|read|okumak|I read before bed.|Yatmadan önce kitap okurum.|I read that book last week.|O kitabı geçen hafta okudum.|I have read this article.|Bu makaleyi okudum.
speak|spoke|spoken|konuşmak|I speak Turkish.|Türkçe konuşurum.|I spoke to her yesterday.|Dün onunla konuştum.|I have spoken to the manager.|Müdürle konuştum.
buy|bought|bought|satın almak|I buy bread every morning.|Her sabah ekmek alırım.|I bought a new coat.|Yeni bir mont aldım.|I have bought the tickets.|Biletleri aldım.
meet|met|met|tanışmak; buluşmak|I meet my friends on Fridays.|Cuma günleri arkadaşlarımla buluşurum.|I met him last year.|Onunla geçen yıl tanıştım.|I have met her before.|Onunla daha önce tanıştım.
run|ran|run|koşmak|I run in the park.|Parkta koşarım.|I ran five kilometres yesterday.|Dün beş kilometre koştum.|I have run a marathon.|Bir maraton koştum.
understand|understood|understood|anlamak|I understand the question.|Soruyu anlıyorum.|I understood the explanation.|Açıklamayı anladım.|I have understood your point.|Ne demek istediğini anladım.
begin|began|begun|başlamak|I begin work at nine.|İşe saat dokuzda başlarım.|The lesson began at ten.|Ders saat onda başladı.|The film has begun.|Film başladı.
become|became|become|olmak; hâline gelmek|I become tired after long walks.|Uzun yürüyüşlerden sonra yorulurum.|She became a doctor.|O doktor oldu.|We have become friends.|Arkadaş olduk.
keep|kept|kept|saklamak; tutmak|I keep my promises.|Sözlerimi tutarım.|I kept the receipt.|Fişi sakladım.|I have kept your letter.|Mektubunu sakladım.
hear|heard|heard|duymak|I hear birds every morning.|Her sabah kuş sesleri duyarım.|I heard a noise.|Bir ses duydum.|I have heard the news.|Haberi duydum.
sit|sat|sat|oturmak|I sit by the window.|Pencerenin yanında otururum.|I sat next to Ece.|Ece'nin yanına oturdum.|I have sat here before.|Daha önce burada oturdum.
stand|stood|stood|ayakta durmak|I stand near the door.|Kapının yakınında ayakta dururum.|I stood in the queue.|Sırada bekledim.|I have stood here for an hour.|Bir saattir burada ayakta duruyorum.
pay|paid|paid|ödemek|I pay by card.|Kartla öderim.|I paid the bill.|Hesabı ödedim.|I have paid the rent.|Kirayı ödedim.
send|sent|sent|göndermek|I send a message every day.|Her gün bir mesaj gönderirim.|I sent you a photo.|Sana bir fotoğraf gönderdim.|I have sent the email.|E-postayı gönderdim.
wear|wore|worn|giymek; üzerinde olmak|I wear glasses.|Gözlük takarım.|I wore a blue shirt.|Mavi bir gömlek giydim.|I have worn this coat for years.|Bu montu yıllardır giyiyorum.
lose|lost|lost|kaybetmek|I often lose my keys.|Anahtarlarımı sık sık kaybederim.|I lost my ticket.|Biletimi kaybettim.|I have lost my wallet.|Cüzdanımı kaybettim.
choose|chose|chosen|seçmek|I choose fresh fruit.|Taze meyve seçerim.|I chose the red bag.|Kırmızı çantayı seçtim.|I have chosen a course.|Bir kurs seçtim.
work|worked|worked|çalışmak|I work at home.|Evde çalışırım.|I worked yesterday.|Dün çalıştım.|I have worked here before.|Daha önce burada çalıştım.
study|studied|studied|ders çalışmak; öğrenim görmek|I study English.|İngilizce çalışırım.|I studied last night.|Dün gece ders çalıştım.|I have studied this topic.|Bu konuyu çalıştım.
play|played|played|oynamak; çalmak|I play tennis.|Tenis oynarım.|I played tennis yesterday.|Dün tenis oynadım.|I have played this game before.|Daha önce bu oyunu oynadım.
help|helped|helped|yardım etmek|I help my parents.|Aileme yardım ederim.|I helped my friend.|Arkadaşıma yardım ettim.|I have helped many people.|Birçok insana yardım ettim.
want|wanted|wanted|istemek|I want some water.|Biraz su istiyorum.|I wanted to help.|Yardım etmek istedim.|I have always wanted to travel.|Her zaman seyahat etmek istemişimdir.
need|needed|needed|ihtiyaç duymak|I need a pen.|Bir kaleme ihtiyacım var.|I needed more time.|Daha fazla zamana ihtiyacım vardı.|I have needed help several times.|Birkaç kez yardıma ihtiyaç duydum.
ask|asked|asked|sormak; istemek|I ask questions in class.|Derste soru sorarım.|I asked her a question.|Ona bir soru sordum.|I have asked for help.|Yardım istedim.
answer|answered|answered|cevaplamak|I answer emails every morning.|Her sabah e-postaları cevaplarım.|I answered the question.|Soruyu cevapladım.|I have answered all the questions.|Bütün soruları cevapladım.
call|called|called|aramak; çağırmak|I call my mother every day.|Annemi her gün ararım.|I called you yesterday.|Seni dün aradım.|I have called him twice.|Onu iki kez aradım.
visit|visited|visited|ziyaret etmek|I visit my grandparents often.|Büyükanne ve büyükbabamı sık sık ziyaret ederim.|I visited Ece last week.|Geçen hafta Ece'yi ziyaret ettim.|I have visited Rome.|Roma'yı ziyaret ettim.
watch|watched|watched|izlemek|I watch the news.|Haberleri izlerim.|I watched a film last night.|Dün gece bir film izledim.|I have watched this video.|Bu videoyu izledim.
listen|listened|listened|dinlemek|I listen to music.|Müzik dinlerim.|I listened to the teacher.|Öğretmeni dinledim.|I have listened to this song many times.|Bu şarkıyı birçok kez dinledim.
open|opened|opened|açmak|I open the window every morning.|Her sabah pencereyi açarım.|I opened the door.|Kapıyı açtım.|I have opened the box.|Kutuyu açtım.
close|closed|closed|kapatmak|I close the shop at six.|Dükkânı saat altıda kapatırım.|I closed the window.|Pencereyi kapattım.|I have closed the door.|Kapıyı kapattım.
start|started|started|başlamak|I start work at nine.|İşe saat dokuzda başlarım.|I started a new job.|Yeni bir işe başladım.|I have started learning English.|İngilizce öğrenmeye başladım.
finish|finished|finished|bitirmek|I finish work at five.|İşi saat beşte bitiririm.|I finished the report.|Raporu bitirdim.|I have finished my homework.|Ödevimi bitirdim.
stop|stopped|stopped|durmak; durdurmak|I stop at red lights.|Kırmızı ışıkta dururum.|I stopped the car.|Arabayı durdurdum.|It has stopped raining.|Yağmur durdu.
try|tried|tried|denemek; çabalamak|I try new recipes.|Yeni tarifler denerim.|I tried to call you.|Seni aramaya çalıştım.|I have tried sushi.|Suşi denedim.
use|used|used|kullanmak|I use this app every day.|Bu uygulamayı her gün kullanırım.|I used your pen.|Kalemini kullandım.|I have used this tool before.|Daha önce bu aracı kullandım.
learn|learned / learnt|learned / learnt|öğrenmek|I learn new words every day.|Her gün yeni kelimeler öğrenirim.|I learned ten words yesterday.|Dün on kelime öğrendim.|I have learned a lot.|Çok şey öğrendim."""
notes={
'be':'V1 kişiye göre am/is/are olur. V2: I/he/she/it was; you/we/they were.',
'get':'V3 got İngiliz İngilizcesinde yaygındır; Amerikan İngilizcesinde birçok anlamda gotten kullanılır. Have got sahiplik kalıbı ayrıca öğrenilir.',
'read':'Yazılış aynı; V1 /riːd/, V2 ve V3 /red/ diye okunur.',
'learn':'Learned düzenli, learnt alternatif düzensiz biçimdir. İkisi de kabul edilir.',
'stop':'Kısa vurgulu ünlü + tek son ünsüz: p çiftlenir; stopped.',
'study':'Ünsüz + y sonunda y → i olur: studied.',
'try':'Ünsüz + y sonunda y → i olur: tried.',
'play':'Ünlü + y: y değişmez; played.',
'listen':'Bir şeyi dinlemek: listen to something.',
'go':'Gone gitti ve henüz dönmedi anlamı taşıyabilir; been to gidip dönme deneyiminde kullanılır.'
}
verbs=[]
for i,line in enumerate(raw.splitlines()):
    w,v2,v3,meaning,en1,tr1,en2,tr2,en3,tr3=line.split('|')
    match=next((x['id'] for x in words if x['word']==w and 'verb' in x['part_of_speech']),None)
    verbs.append(dict(word=w,v2=v2,v3=v3,meaning=meaning,regular=i>=40,note=notes.get(w,''),wordId=match,examples=[dict(en=en1,tr=tr1),dict(en=en2,tr=tr2),dict(en=en3,tr=tr3)]))
(root/'content'/'verbs.json').write_text(json.dumps(verbs,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'{len(verbs)} verbs; {sum(v["wordId"] is not None for v in verbs)} dictionary links')
