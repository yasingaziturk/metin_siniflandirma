Metin Sınıflandırmada Ön işleme (preprocessing)
Metin sınıflandırma problemi sırasıyla şu aşamalardan oluşur. Ön işleme (preprocessing),
Öznitelik çıkarımı (Feature extraction), Öznitelik Seçimi (Feature Selection), Sınıflandırıcının Eğitilmesi
(Training) ve Sınıflandırının Test Edilmesi (Testing).
Ön işleme aşamasının amacı, metin içerisinde gerekli işlemleri yaparak, öznitelik sayısının
azaltılmasını ve öznitelik çıkarımı aşamasından önce gereksiz karakterin kaldırılmasını sağlamaktır.

Cümle 1: Bu film cok guzel, ailecek beğendik
Cümle 2: bu filmi beğendim, çok güzel

Yukarıdaki cümle örnekleri için eğer herhangi bir ön işleme adımı uygulanmazsa, “Bu” kelimesi ile “bu”
kelimesi, “film” kelimesi ile “filmi” , “cok” kelimesi ile “çok” kelimesi, “beğendim” kelimesi ile
“beğendik” kelimesi farklı öznitelikler olarak ele alınır. Bu durumda aynı şeyleri ifade etmesine rağmen
özniteliklerin sayısının artmasına neden olur.

1) Metinlerin normalizasyonu: Kullanıcılar yorum yazarken bazı durumlarda kelimeleri eksik veya
yanlış yazabilmektedirler. Bu adımda Zemberek kütüphanesine ait fonksiyonlar kullanılarak metin
üzerinde düzeltmeler yapılmaktadır. Bu fonksiyonlar ayrıca büyük harfleri küçük harflere
dönüştürmekte ve metin içerisindeki fazla boşlukları kaldırmaktadır.
Örnek cümle ve çıktısı:


Girdi: Bu fılm cok guzelll, begendm
Çıktı: bu film çok güzel , beğendim


2) Metindeki kelimelerin köklerinin bulunması ve fiilerdeki olumsuz durumların ele alınması: İlk
adımı uyguladıktan sonra, diğer adım kelimelerin köklerinin bulunmasıdır. “beğendim” ve “beğendik”
kelimeleri, veya “film” ve “filmi” kelimeleri aldığı eklerden dolayı farklı olsa da aynı şeyleri ifade
etmektedir. Bu kelimeleri “beğen” ve “film” köklerine dönüştürmemiz gerekmektedir. Aşağıdaki kod
bir kelimeyi girdi olarak alır, kökünü bulur ve olumsuz bir ifadeyse sonuna “NEG” ekler. “beğenmedim”
girdisi “beğenNEG” haline dönüşür. Aşağıdaki kod tek bir kelime için çalışır, verilen bir metin için kodu
güncellemeniz gerekmektedir. Metin kelimelere bölünerek, her bir kelime için kök işlemi uygulanıp
tekrar birleştirilerek metin haline getirilmesi gerekmektedir.

3) Duygu belirten emoji ifadelerinin tespiti: Kullanıcılar yorumlarda “:)” “:(“ benzeri emoji ifadelerini
kullanmaktadırlar. Noktalama işaretlerini kaldırmadan önce bu emojilerin kelimelere ( örn,
POSEMOTİON, NEGEMOTİON) dönüştürülerek ele alınması gerekmektedir.

4) Noktalama işaretlerinin kaldırılması: Metin içerisindeki “, ; ? ! . “ gibi noktalama işaretlerinin
kaldırılması gerekmektedir.

5) Fazla boşlukların kaldırılması: Önişleme adımlarından sonra elde edilen kelime dizisi boşluklara
göre ayrılıp, her bir kelime veya kelime grubu öznitelik olarak kullanılacağı için, metin içerisindeki
fazla boşlukların kaldırılması gerekmektedir.

Veri Seti

Veri setinde 1750 pozitif ve 1750 negatif olmak üzere toplam 3500 ürün yorumu bulunmaktadır.
