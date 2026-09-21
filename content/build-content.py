import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
lessons=[]
def pairs(text):
    return [dict(zip(('en','tr'),line.split('|',1))) for line in text.strip().splitlines() if line.strip()]
def lesson(id,group,title,subtitle,intro,usage,forms,examples,tips,compare,questions):
    lessons.append(dict(id=id,group=group,title=title,subtitle=subtitle,intro=intro,usage=usage,forms=forms,examples=pairs(examples),tips=tips,comparison=compare,questions=[dict(id=f'{id}-{i+1}',prompt=q[0],answers=q[1].split('~'),explanation=q[2]) for i,q in enumerate(questions)]))

lesson('present-simple','tenses','Present Simple','Rutinler ve genel doğrular',
'Her gün yaptığın bir işi ya da genel bir gerçeği anlatırken kullanırsın. “Her sabah kahve içerim” bir alışkanlıktır; tam şu anda içiyor olman gerekmez.',
['Alışkanlıklar: every day, usually, often.','Genel doğrular ve kalıcı görülen durumlar.','Tarife ve programlar: The train leaves at six.'],
['Olumlu: I/you/we/they + V1; he/she/it + V1-s','Olumsuz: do not / does not + V1','Soru: Do / Does + özne + V1?','Kısa cevap: Yes, I do. / No, she does not.','Be ayrı çalışır: I am; you/we/they are; he/she/it is. Are you ready?'],
'''I drink tea every morning.|Her sabah çay içerim.
I do not drink coffee at night.|Geceleri kahve içmem.
Do you drink tea every morning?|Her sabah çay içer misin?
She works in a hospital.|O, bir hastanede çalışır.
She does not work on Sundays.|Pazar günleri çalışmaz.
Does she work here?|O burada mı çalışıyor?
They walk to school.|Okula yürüyerek giderler.
They do not walk to school in winter.|Kışın okula yürüyerek gitmezler.
Do they walk to school?|Okula yürüyerek mi giderler?
My brother studies English.|Erkek kardeşim İngilizce çalışır.
He does not study late at night.|Gece geç saatlerde ders çalışmaz.
Does he study every day?|Her gün ders çalışır mı?
The shop opens at nine.|Dükkân saat dokuzda açılır.
Water freezes at zero degrees Celsius.|Su, sıfır santigrat derecede donar.
I am tired after work.|İşten sonra yorgun olurum.''',
['Does she works? yanlış; üçüncü tekil kişi bilgisi does ile belirtilir: Does she work?','He/she/it ile -s/-es gelir: works, watches. Ünsüz + y: study → studies.','Always/usually/often çoğunlukla asıl fiilden önce, be fiilinden sonra gelir.'],
'I work at home: genel düzenim. I am working at home today: bugüne özgü durum.',
[('O her gün çalışır. İngilizce yaz.','She works every day.~He works every day.','He/she ile olumlu cümlede work → works olur.'),('She ___ (go) to work by bus. Boşluğu doldur.','goes','She üçüncü tekil kişidir; go fiili goes olur.')])

lesson('present-continuous','tenses','Present Continuous','Şu anda ve bu aralar olanlar',
'Bir eylemi sürerken gösterir. “Şu anda yemek yapıyorum” ya da “Bu ay evden çalışıyorum” diyebilirsin. Bazı kesinleşmiş gelecek düzenlemelerinde de kullanılır.',
['Konuşma anında sürmekte olan işler.','Geçici durumlar ve değişimler.','Zamanı ve düzenlemesi belli gelecek planları.'],
['Olumlu: özne + am/is/are + V-ing','Olumsuz: am not / is not / are not + V-ing','Soru: Am/Is/Are + özne + V-ing?','Kısa cevap: Yes, she is. / No, they are not.'],
'''I am cooking dinner now.|Şimdi akşam yemeği yapıyorum.
I am not cooking today.|Bugün yemek yapmıyorum.
Are you cooking dinner?|Akşam yemeği mi yapıyorsun?
She is reading a book.|O, bir kitap okuyor.
She is not watching television.|O, televizyon izlemiyor.
Is she reading my book?|O benim kitabımı mı okuyor?
They are learning English.|Onlar İngilizce öğreniyorlar.
They are not listening to music.|Onlar müzik dinlemiyorlar.
Are they waiting for us?|Bizi mi bekliyorlar?
We are staying with friends this week.|Bu hafta arkadaşlarımızda kalıyoruz.
It is getting cold.|Hava soğuyor.
The children are playing outside.|Çocuklar dışarıda oynuyor.
I am meeting Ece tomorrow.|Yarın Ece ile buluşuyorum.
Why are you smiling?|Neden gülümsüyorsun?
He is looking for his keys.|O, anahtarlarını arıyor.''',
['I working yanlış; am/is/are gerekir.','make → making, run → running; see → seeing.','Know, believe, own gibi durum fiilleri çoğunlukla continuous kullanılmaz: I know.'],
'She reads every evening: alışkanlık. She is reading now: şu an süren eylem.',
[('Şu anda İngilizce çalışıyorum.','I am studying English now.~I am studying English right now.~I am learning English now.','I ile am ve fiilin -ing biçimi kullanılır.'),('She ___ (read) a book now.','is reading','Şu anda süren eylem: is + reading.')])

lesson('past-simple','tenses','Past Simple','Geçmişte bitmiş olaylar',
'Geçmişte tamamlanmış bir olayı anlatır. Yesterday, last week veya in 2020 gibi bitmiş zamanlarla sık kullanılır. Zaman bazen bağlamdan anlaşılır.',
['Bitmiş geçmiş olayları.','Geçmişte art arda olan eylemler.','Geçmiş alışkanlıklar ve durumlar.'],
['Olumlu: özne + V2','Olumsuz: did not + V1','Soru: Did + özne + V1?','Kısa cevap: Yes, I did. / No, I did not.','Be: I/he/she/it was; you/we/they were. Was she ready?'],
'''I visited my friend yesterday.|Dün arkadaşımı ziyaret ettim.
I did not visit my friend yesterday.|Dün arkadaşımı ziyaret etmedim.
Did you visit your friend yesterday?|Dün arkadaşını ziyaret ettin mi?
She went to the market.|O, pazara gitti.
She did not go to work.|O, işe gitmedi.
Did she go alone?|O yalnız mı gitti?
We watched a film last night.|Dün gece bir film izledik.
We did not watch the match.|Maçı izlemedik.
Did you watch the match?|Maçı izlediniz mi?
He bought a new phone.|O, yeni bir telefon aldı.
I lost my keys on Monday.|Pazartesi günü anahtarlarımı kaybettim.
They arrived at six.|Saat altıda geldiler.
I was tired yesterday.|Dün yorgundum.
Were you at home last night?|Dün gece evde miydin?
She opened the door and smiled.|Kapıyı açtı ve gülümsedi.''',
['Did you went? yanlış; Did you go? doğru.','Düzenli fiile -ed gelir; düzensiz fiilin V2 biçimi öğrenilir.','Was/were sorularında did kullanılmaz: Were you tired?'],
'I lost my keys yesterday: geçmiş olay ve zamanı. I have lost my keys: şu anki sonucu ön planda.',
[('Dün işe gitmedim.','I did not go to work yesterday.~Yesterday I did not go to work.','Did not geçmişi taşır; went yerine go kullanılır.'),('Did she ___ (buy) the tickets?','buy','Did sonrasında yalın fiil gelir.')])

lesson('past-continuous','tenses','Past Continuous','Geçmişte o sırada olanlar',
'Geçmişte bir anın içindeymiş gibi anlatırsın: “Dün sekizde yemek yiyordum.” O sırada gerçekleşen kısa bir olay için genellikle Past Simple kullanılır.',
['Geçmişte belirli bir anda devam eden eylem.','Bir olayın arka planı.','Aynı anda süren iki geçmiş eylem.'],
['Olumlu: özne + was/were + V-ing','Olumsuz: was not / were not + V-ing','Soru: Was/Were + özne + V-ing?','Kısa cevap: Yes, I was. / No, they were not.'],
'''I was cooking when you called.|Sen aradığında yemek yapıyordum.
I was not sleeping when you called.|Sen aradığında uyumuyordum.
Were you working when I called?|Ben aradığımda çalışıyor muydun?
She was reading at eight.|Saat sekizde kitap okuyordu.
She was not watching television.|O sırada televizyon izlemiyordu.
Was she waiting outside?|Dışarıda mı bekliyordu?
They were walking home when it started to rain.|Yağmur başladığında eve yürüyorlardı.
They were not driving fast.|Hızlı sürmüyorlardı.
Were they talking about us?|Bizim hakkımızda mı konuşuyorlardı?
We were having dinner at seven.|Saat yedide akşam yemeği yiyorduk.
It was raining all afternoon.|Bütün öğleden sonra yağmur yağıyordu.
While I was studying, my sister was cooking.|Ben ders çalışırken kız kardeşim yemek yapıyordu.
The children were playing in the garden.|Çocuklar bahçede oynuyordu.
What were you doing at midnight?|Gece yarısı ne yapıyordun?
I dropped my phone while I was running.|Koşarken telefonumu düşürdüm.''',
['Süren olay: was cooking. Araya giren olay: called.','While çoğunlukla süren eylemle gelir; zaman seçimini sadece bağlaca göre yapma.'],
'I cooked dinner: yemeği yaptım. I was cooking dinner: o sırada yemek yapıyordum.',
[('Sen aradığında uyuyordum.','I was sleeping when you called.~When you called, I was sleeping.','Süren eylem was sleeping; araya giren kısa olay called.'),('They ___ (wait) at six yesterday.','were waiting','They ile were ve fiilin -ing biçimi kullanılır.')])

lesson('present-perfect','tenses','Present Perfect','Geçmiş ile şimdi arasındaki bağ',
'Olay geçmişte olur ama şimdiyle ilişkisi önemlidir. Bir deneyimi, yeni biten bir işi veya geçmişte başlayıp devam eden bir durumu anlatabilirsin. Türkçede tek bir kalıba bire bir karşılık gelmez.',
['Şimdiki sonucu önemli olan olaylar.','Şimdiye kadarki deneyimler.','Henüz bitmemiş dönemler ve süren durumlar.'],
['Olumlu: özne + have/has + V3','Olumsuz: have not / has not + V3','Soru: Have/Has + özne + V3?','Kısa cevap: Yes, I have. / No, she has not.'],
'''I have lost my keys.|Anahtarlarımı kaybettim; şu an bulamıyorum.
I have not finished my homework yet.|Ödevimi henüz bitirmedim.
Have you finished your homework?|Ödevini bitirdin mi?
She has visited London twice.|Londra'yı iki kez ziyaret etti.
She has not seen this film.|O, bu filmi izlemedi.
Has she ever tried sushi?|O hiç suşi denedi mi?
We have lived here for five years.|Beş yıldır burada yaşıyoruz.
They have just arrived.|Onlar az önce geldi.
I have already eaten.|Ben zaten yemek yedim.
Have you ever been to Rome?|Hiç Roma'da bulundun mu?
He has gone to the bank.|O, bankaya gitti; henüz dönmedi.
I have known her since school.|Onu okul yıllarından beri tanıyorum.
We have had three meetings this week.|Bu hafta şimdiye kadar üç toplantı yaptık.
It has stopped raining.|Yağmur durdu.
How long have you had this car?|Bu araba ne zamandır sende?''',
['I have seen him yesterday yerine I saw him yesterday. Yesterday bitmiş zamandır.','Since başlangıç: since Monday. For süre: for two days.','Been to: gidip dönmüş olma deneyimi. Gone to: gitmiş, hâlâ orada veya yolda.'],
'I have read this book: deneyim/sonuç. I read it last year: bitmiş geçmiş zaman.',
[('Ödevimi henüz bitirmedim.','I have not finished my homework yet.','Have not + V3 kullanılır; yet burada henüz demektir.'),('She has ___ (write) three emails.','written','Has sonrasında write fiilinin V3 biçimi written gelir.')])

lesson('present-perfect-continuous','tenses','Present Perfect Continuous','Bir süredir devam eden uğraş',
'Geçmişte başlayan bir eylemin süresini veya devam eden etkisini vurgular. “İki saattir çalışıyorum” derken sonuca değil çalışma sürecine odaklanırsın. Eylem az önce bitmiş de olabilir.',
['Geçmişte başlayıp şimdiye kadar süren eylem.','Yeni bitmiş bir eylemin görünen etkisi.','How long, for, since ile süreç vurgusu.'],
['Olumlu: özne + have/has been + V-ing','Olumsuz: have/has not been + V-ing','Soru: Have/Has + özne + been + V-ing?','Kısa cevap: Yes, I have. / No, she has not.'],
'''I have been studying for two hours.|İki saattir ders çalışıyorum.
I have not been sleeping well lately.|Son zamanlarda iyi uyuyamıyorum.
Have you been waiting long?|Uzun zamandır mı bekliyorsun?
She has been learning English since January.|Ocak ayından beri İngilizce öğreniyor.
She has not been feeling well.|Bir süredir kendini iyi hissetmiyor.
Has she been working all day?|Bütün gün mü çalışıyor?
They have been playing football.|Bir süredir futbol oynuyorlar.
We have been looking for a new flat.|Bir süredir yeni bir daire arıyoruz.
It has been raining all morning.|Bütün sabah yağmur yağıyor.
I have been reading this book for a week.|Bir haftadır bu kitabı okuyorum.
He has been running; his face is red.|Koşuyordu; yüzü kıpkırmızı.
Why have you been crying?|Neden ağlıyordun?
We have been talking about our plans.|Bir süredir planlarımız hakkında konuşuyoruz.
They have been building a bridge since March.|Mart ayından beri köprü yapıyorlar.
How long have you been living here?|Ne zamandır burada yaşıyorsun?''',
['Have been knowing yerine have known kullanılır; know çoğunlukla durum fiilidir.','Kaç tane bitti? have written three emails. Ne kadar süredir? have been writing for an hour.'],
'I have cleaned the room: sonuç. I have been cleaning the room: süreç ve emek.',
[('İki saattir bekliyorum.','I have been waiting for two hours.','Have been + waiting; for two hours süreyi belirtir.'),('She ___ (study) since nine. Süreci vurgula.','has been studying','Süre vurgusunda has been + V-ing kullanılır.')])

lesson('past-perfect','tenses','Past Perfect','Geçmişteki bir olaydan daha önce',
'Geçmişteki bir noktadan geriye bakarsın. “Ben geldiğimde o gitmişti”: önce gitme, sonra benim gelmem. İki geçmiş olayın sırasını açıklamak için kullanılır; her eski olayda gerekli değildir.',
['Geçmişteki bir olaydan önce tamamlanan eylem.','Geçmişteki bir durumun daha önceki nedeni.','By the time, already, before gibi ifadelerle geçmiş sırası.'],
['Olumlu: özne + had + V3','Olumsuz: had not + V3','Soru: Had + özne + V3?','Kısa cevap: Yes, I had. / No, she had not.'],
'''She had left before I arrived.|Ben gelmeden önce o gitmişti.
I had not eaten before the meeting.|Toplantıdan önce yemek yememiştim.
Had you met him before the party?|Partiden önce onunla tanışmış mıydın?
We had finished dinner when they arrived.|Onlar geldiğinde yemeğimizi bitirmiştik.
The train had already left when we reached the station.|İstasyona vardığımızda tren çoktan gitmişti.
He had lost his phone, so he could not call.|Telefonunu kaybetmişti, bu yüzden arayamadı.
I had never flown before that trip.|O yolculuktan önce hiç uçağa binmemiştim.
They had booked a room before they travelled.|Seyahate çıkmadan önce bir oda ayırtmışlardı.
She had not heard the news when I called.|Ben aradığımda haberi duymamıştı.
Had they cleaned the room before you arrived?|Sen gelmeden önce odayı temizlemişler miydi?
By noon, I had sent all the emails.|Öğlene kadar bütün e-postaları göndermiştim.
It had stopped raining by the time we left.|Biz ayrıldığımızda yağmur durmuştu.
I recognised her because I had seen her photo.|Fotoğrafını daha önce gördüğüm için onu tanıdım.
He was tired because he had worked all night.|Bütün gece çalıştığı için yorgundu.
We had lived there for ten years before we moved.|Taşınmadan önce orada on yıl yaşamıştık.''',
['Had tüm öznelerde aynıdır.','Had went yanlış; had gone doğru.','Olayların sırası zaten açıksa her cümleyi Past Perfect yapmana gerek yok.'],
'When I arrived, she left: geldim, sonra gitti. When I arrived, she had left: ben gelmeden gitmişti.',
[('Ben gelmeden önce o gitmişti.','She had left before I arrived.~He had left before I arrived.~Before I arrived, she had left.','Önce olan eylem had left ile anlatılır.'),('They had ___ (eat) before we arrived.','eaten','Had sonrasında eat fiilinin V3 biçimi eaten gelir.')])

lesson('past-perfect-continuous','tenses','Past Perfect Continuous','Geçmişte o ana kadar süren eylem',
'Geçmişteki bir olaydan önce ne kadar süredir bir işle uğraşıldığını anlatır. “Otobüs geldiğinde yarım saattir bekliyorduk.” Beklemenin süresi ön plandadır.',
['Geçmiş bir noktaya kadar süren eylem.','Geçmişte görülen bir etkinin önceki nedeni.'],
['Olumlu: özne + had been + V-ing','Olumsuz: had not been + V-ing','Soru: Had + özne + been + V-ing?','Kısa cevap: Yes, I had. / No, they had not.'],
'''We had been waiting for thirty minutes when the bus arrived.|Otobüs geldiğinde otuz dakikadır bekliyorduk.
I had not been sleeping well before the holiday.|Tatilden önce bir süredir iyi uyuyamıyordum.
Had you been working long when I called?|Ben aradığımda uzun süredir mi çalışıyordun?
She had been studying for hours before she took a break.|Mola vermeden önce saatlerdir ders çalışıyordu.
He was tired because he had been running.|Bir süredir koştuğu için yorgundu.
It had been raining all night, so the ground was wet.|Bütün gece yağmur yağdığı için yer ıslaktı.
They had been living there for a year when we met.|Tanıştığımızda bir yıldır orada yaşıyorlardı.
I had been looking for my keys before you found them.|Sen bulmadan önce bir süredir anahtarlarımı arıyordum.
We had been talking for an hour when she arrived.|O geldiğinde bir saattir konuşuyorduk.
Had she been crying before you saw her?|Sen onu görmeden önce ağlıyor muydu?
He had not been exercising regularly before he joined the gym.|Spor salonuna yazılmadan önce düzenli egzersiz yapmıyordu.
The children had been playing outside, so their shoes were muddy.|Çocuklar dışarıda oynadığı için ayakkabıları çamurluydu.
I had been learning English for six months when I got the job.|İşe girdiğimde altı aydır İngilizce öğreniyordum.
They had been driving for three hours when they stopped.|Durduklarında üç saattir araba sürüyorlardı.
How long had you been waiting when the doctor arrived?|Doktor geldiğinde ne kadar süredir bekliyordun?''',
['Geçmişte bir referans noktası gerekir; bunu aynı cümle ya da bağlam sağlar.','Had been working süreç; had finished tamamlanmış sonuç.'],
'I had read the book: kitap bitmişti. I had been reading for an hour: bir saattir okuyordum.',
[('Otobüs geldiğinde bir saattir bekliyorduk.','We had been waiting for an hour when the bus arrived.~We had been waiting for one hour when the bus arrived.','Had been waiting, geçmişte otobüsün gelişine kadar süren beklemeyi anlatır.'),('She had been ___ (work) all day.','working','Been sonrasında süreç anlatımında V-ing gelir.')])

lesson('future-simple','tenses','Future Simple','Will ile gelecek',
'Konuşma anında verilen karar, söz verme veya geleceğe ilişkin düşünce için will kullanabilirsin. Gelecek yalnızca will ile anlatılmaz; planın türüne göre başka yapılar da seçilir.',
['Anlık karar ve yardım teklifi.','Söz verme.','Geleceğe ilişkin tahmin veya düşünce.'],
['Olumlu: özne + will + V1','Olumsuz: will not (won’t) + V1','Soru: Will + özne + V1?','Kısa cevap: Yes, I will. / No, I will not.'],
'''I will call you tomorrow.|Seni yarın arayacağım.
I will not forget your birthday.|Doğum gününü unutmayacağım.
Will you help me?|Bana yardım eder misin?
I think it will rain tomorrow.|Sanırım yarın yağmur yağacak.
She will probably arrive late.|Muhtemelen geç gelecek.
They will not agree with us.|Bizimle aynı fikirde olmayacaklar.
Will they come to the meeting?|Toplantıya gelecekler mi?
The phone is ringing. I will answer it.|Telefon çalıyor. Ben açarım.
I am tired. I will take a break.|Yorgunum. Bir mola vereceğim.
We will help you carry the bags.|Çantaları taşımana yardım edeceğiz.
I promise I will be on time.|Söz veriyorum, zamanında geleceğim.
When will you be ready?|Ne zaman hazır olacaksın?
It will be fine.|Her şey yolunda olacak.
I will send it when I get home.|Eve varınca onu göndereceğim.
Will there be enough food?|Yeterince yemek olacak mı?''',
['Will goes yanlış; will go doğru.','Gelecek zaman bağlacında when I get home kullanılır; bu anlamda when I will get home değil.'],
'I will answer: şimdi karar verdim. I am going to study tonight: önceden niyet ettim.',
[('Seni yarın arayacağım.','I will call you tomorrow.~Tomorrow I will call you.','Will sonrasında call yalın biçimde kalır.'),('She will ___ (help) us.','help','Will bütün öznelerde yalın fiil alır.')])

lesson('future-continuous','tenses','Future Continuous','Gelecekte o sırada',
'Gelecekte belirli bir anda sürüyor olacak eylemi anlatır. “Yarın bu saatte uçuyor olacağım.” Bir sahneyi geleceğin içine yerleştirirsin.',
['Gelecekte belli bir anda süren eylem.','Beklenen akış içindeki planlar.','Birinin planını nazikçe sorma.'],
['Olumlu: özne + will be + V-ing','Olumsuz: will not be + V-ing','Soru: Will + özne + be + V-ing?','Kısa cevap: Yes, I will. / No, she will not.'],
'''I will be working at ten tomorrow.|Yarın saat onda çalışıyor olacağım.
I will not be sleeping at that time.|O saatte uyuyor olmayacağım.
Will you be working this evening?|Bu akşam çalışıyor olacak mısın?
She will be flying to London this time tomorrow.|Yarın bu saatte Londra'ya uçuyor olacak.
They will be waiting at the station.|İstasyonda bekliyor olacaklar.
We will be having dinner at seven.|Saat yedide akşam yemeği yiyor olacağız.
He will not be using the car tomorrow.|Yarın arabayı kullanıyor olmayacak.
Will you be using your laptop tonight?|Bu gece dizüstü bilgisayarını kullanacak mısın?
The children will be sleeping when we get home.|Eve vardığımızda çocuklar uyuyor olacak.
I will be studying all afternoon.|Bütün öğleden sonra ders çalışıyor olacağım.
We will be travelling during the holidays.|Tatilde seyahat ediyor olacağız.
What will you be doing at noon?|Öğlen ne yapıyor olacaksın?
She will be staying with her parents next week.|Gelecek hafta ailesinin yanında kalıyor olacak.
They will not be working on Sunday.|Pazar günü çalışıyor olmayacaklar.
I will be thinking of you.|Seni düşünüyor olacağım.''',
['Will be work yanlış; will be working doğru.','Kısa cevapta Yes, I will be yerine çoğunlukla Yes, I will kullanılır.'],
'I will call at eight: olay. I will be talking at eight: o anda süren eylem.',
[('Yarın saat onda çalışıyor olacağım.','I will be working at ten tomorrow.~Tomorrow I will be working at ten.','Will be working gelecekte o anda devam eden eylemdir.'),('They will be ___ (wait) for us.','waiting','Will be sonrasında burada V-ing gerekir.')])

lesson('future-perfect','tenses','Future Perfect','Gelecekte o zamana kadar bitmiş',
'Gelecekte bir son noktayı düşün, sonra o noktadan geriye bak: “Cumaya kadar raporu bitirmiş olacağım.” Önemli olan o zamana kadar işin tamamlanmasıdır.',
['Gelecekte bir zamana kadar tamamlanacak iş.','Gelecekte bir noktada ulaşılmış süre veya miktar.'],
['Olumlu: özne + will have + V3','Olumsuz: will not have + V3','Soru: Will + özne + have + V3?','Kısa cevap: Yes, I will. / No, they will not.'],
'''I will have finished the report by Friday.|Cumaya kadar raporu bitirmiş olacağım.
I will not have finished by noon.|Öğlene kadar bitirmiş olmayacağım.
Will you have finished by six?|Saat altıya kadar bitirmiş olacak mısın?
She will have arrived by the time we leave.|Biz ayrılana kadar o gelmiş olacak.
They will have built the bridge by next year.|Gelecek yıla kadar köprüyü yapmış olacaklar.
We will have eaten before the film starts.|Film başlamadan önce yemek yemiş olacağız.
He will have saved enough money by December.|Aralık ayına kadar yeterince para biriktirmiş olacak.
Will they have received the letter by Monday?|Pazartesiye kadar mektubu almış olacaklar mı?
I will have read the book by tomorrow.|Yarına kadar kitabı okumuş olacağım.
She will not have left when you arrive.|Sen geldiğinde henüz ayrılmamış olacak.
By next month, we will have lived here for ten years.|Gelecek ay burada on yıldır yaşıyor olacağız.
The shop will have closed by then.|O zamana kadar dükkân kapanmış olacak.
How many lessons will you have completed by June?|Hazirana kadar kaç ders tamamlamış olacaksın?
We will have cleaned the house before our guests arrive.|Misafirlerimiz gelmeden önce evi temizlemiş olacağız.
He will have written three chapters by Sunday.|Pazara kadar üç bölüm yazmış olacak.''',
['By Friday: en geç cumaya kadar. Until Friday: cumaya dek süren durum.','Will has yanlış; özne ne olursa olsun will have kullanılır.'],
'I will be writing at six: o sırada sürüyor. I will have written it by six: o saate kadar bitmiş.',
[('Cumaya kadar raporu bitirmiş olacağım.','I will have finished the report by Friday.~By Friday I will have finished the report.','Will have + finished tamamlanmış olacak işi anlatır.'),('She will have ___ (leave) by then.','left','Leave fiilinin V3 biçimi left kullanılır.')])

lesson('future-perfect-continuous','tenses','Future Perfect Continuous','Gelecekte o ana kadar ne kadar süredir?',
'Gelecekteki bir noktaya kadar devam eden eylemin toplam süresini öne çıkarır. “Saat beşte üç saattir çalışıyor olacağım.” Günlük konuşmada daha az gerekir; süre mantığını anlaman yeterli bir başlangıçtır.',
['Gelecekte bir noktaya ulaşınca birikmiş olacak eylem süresi.','For ile toplam süre; by ile gelecekteki referans noktası.'],
['Olumlu: özne + will have been + V-ing','Olumsuz: will not have been + V-ing','Soru: Will + özne + have been + V-ing?','Kısa cevap: Yes, I will. / No, she will not.'],
'''By five, I will have been working for three hours.|Saat beşte üç saattir çalışıyor olacağım.
By June, she will have been learning English for a year.|Haziranda bir yıldır İngilizce öğreniyor olacak.
Will you have been waiting for an hour by then?|O zamana kadar bir saattir bekliyor olacak mısın?
By noon, they will have been driving for six hours.|Öğlen altı saattir araba sürüyor olacaklar.
We will have been living here for ten years next month.|Gelecek ay burada on yıldır yaşıyor olacağız.
By the time you arrive, I will have been cooking for two hours.|Sen geldiğinde iki saattir yemek yapıyor olacağım.
She will have been studying all day by dinner time.|Akşam yemeği saatine kadar bütün gün ders çalışmış olacak.
By July, he will have been training for six months.|Temmuzda altı aydır antrenman yapıyor olacak.
Will they have been travelling for a week by Friday?|Cuma günü bir haftadır seyahat ediyor olacaklar mı?
By ten, we will have been walking for four hours.|Saat onda dört saattir yürüyor olacağız.
I will not have been working here for a year until May.|Mayıs ayına kadar burada çalışma sürem bir yılı doldurmuş olmayacak.
By December, she will have been teaching for twenty years.|Aralıkta yirmi yıldır öğretmenlik yapıyor olacak.
How long will you have been studying by six?|Saat altıda ne kadar süredir ders çalışıyor olacaksın?
By the end of this week, they will have been repairing the road for a month.|Bu haftanın sonunda bir aydır yolu onarıyor olacaklar.
By tomorrow, it will have been raining for three days.|Yarın üç gündür yağmur yağıyor olacak.''',
['Yapı uzundur ama parçaları düzenlidir: will + have + been + V-ing.','Know gibi durum fiilleriyle genellikle Future Perfect seç: will have known.'],
'Will have written ten pages: miktar/sonuç. Will have been writing for two hours: süre.',
[('Saat beşte üç saattir çalışıyor olacağım.','By five I will have been working for three hours.~I will have been working for three hours by five.','Gelecekteki bir noktaya kadar süren eylem: will have been working.'),('She will have been ___ (teach) for ten years.','teaching','Will have been ardından V-ing kullanılır.')])

# More lesson groups and verbs are added below. All examples are authored for this app.
def write():
    (ROOT/'content'/'lessons.json').write_text(json.dumps(lessons,ensure_ascii=False,indent=2),encoding='utf-8')

if __name__=='__main__':
    exec(compile((ROOT/'content'/'build-extras.py').read_text(encoding='utf-8'),'build-extras.py','exec'))
    write()
