import string
from collections import Counter


def nlp_temizleyici(metin):
    # Küçük harfe çevirme:
    metin = metin.lower()

    # Noktalama işaretlerini kaldırma:
    for isaret in string.punctuation:
        metin = metin.replace(isaret, "")

    # Kelimelere ayırma:
    kelimeler = metin.split()

    # Stopwords (etkisiz kelimeler) temizliği:
    etkisiz_kelimeler = ["ve", "ile", "ama", "fakat", "lakin", "bir", "bu", "şu", "o", "ki", "da", "de", "daha", "çok"]

    # Filtreleme döngüsü:
    oz_kelimeler = []

    for kelime in kelimeler:
        if kelime not in etkisiz_kelimeler:
            if not kelime.isdigit():
                oz_kelimeler.append(kelime)

    return oz_kelimeler



girdi = input("Analiz edilecek metni girin: ")

# Fonksiyonu çağırma:
sonuc_kelimeler = nlp_temizleyici(girdi)

# Analiz raporu:
kelime_sayisi = len(sonuc_kelimeler)
frekanslar = Counter(sonuc_kelimeler)


print("METİN ANALİZ RAPORU")
print(f"Toplam Anlamlı Kelime: {kelime_sayisi}")
print(f"Temizlenmiş Liste: {sonuc_kelimeler}")
print("En Çok Geçen Kelimeler:")

for kelime, sayi in frekanslar.most_common(3):
    print(f"'{kelime}': {sayi} kez")


