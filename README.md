# FilmArsivsistemiData
Film Arşiv Sistemi projesi için verilerin hazırlanma kısmı

# Projenin İçeriği
Proje için veriler MongoDB'de saklanmıştır. Projelerin çalıştırılma sırası: CleaningData, StemmingWithZemberek, StopWordsTurkish.
## CleaningData
DB'de tutlan veriler içerisindeki noktalama işaretleri ve bazı işaretler temizlendi
## StemmingWithZemberek
DB'de tutlan veriler zemberek kütüphanesi yardımı ile köklerine ayırılmıştır. Köklerine ayırma işlei için stemming yöntemi kullanılmıştır. Zemberek ile stemming yöntenmi 
kullanılırken zemberek-full.jar kiti kullanılımıştır.
## StopWordsTurkish
Verilerin içerdiği Türkçe ama, ancak vb. gibi kelimeler temizlenmiştir. Bu işlemleri gerçekleştirmek için stop_word_turkish.txt dosyasından faydalanılmıştır.




