# Turkish Text Preprocessing & Analysis Tool
Bu proje, Doğal Dil İşleme (NLP) projelerinde veriyi modele hazırlamak için gereken "Ön İşleme" (Preprocessing) adımlarını gerçekleştiren, Python ile yazılmış bir araçtır.

## Amaç
Harici bir NLP kütüphanesi (NLTK, Spacy vb.) kullanmadan, temel Python veri yapıları ve algoritmaları ile metin temizliği mantığını göstermek amacıyla geliştirilmiştir.

## Özellikler
Bu araç ham bir metni alır ve aşağıdaki işlemleri uygular:
* **Normalization:** Tüm harfleri küçük harfe çevirir.
* **Noise Removal:** Noktalama işaretlerini (`string.punctuation`) temizler.
* **Stopwords Removal:** Türkçe etkisiz kelimeleri (ve, ama, ile vb.) listeden filtreler.
* **Frequency Analysis:** Metin içinde en çok geçen kelimeleri ve sayılarını raporlar (`collections.Counter`).

## Nasıl Çalışır? 

**Girdi:**
"Merhaba Dünya!"

**Çıktı:**
* METİN ANALİZ RAPORU
* Toplam Anlamlı Kelime: 2
* Temizlenmiş Liste: ['merhaba', 'dünya'] 

En Çok Geçen Kelimeler:
* 'merhaba': 1 kez
* 'dünya': 1 kez
