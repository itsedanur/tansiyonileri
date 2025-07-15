# TSYN: Tansiyon Analiz Uygulaması

TSYN (Tansiyon SYmptomları ve Normalleştirme) projesi, kullanıcıların sabah ve akşam tansiyon verilerini analiz ederek riskli durumları tespit eden bir yapay zeka uygulamasıdır. Streamlit ile geliştirilmiş bu uygulama, kullanıcı dostu arayüzü sayesinde hem eğitim hem de sağlık verisi analizi amacıyla kullanılabilir.

# Özellikler

- 🧠 K-means kümeleme ile sistolik-diyastolik tansiyon analizi
- 📊 Sabah ve akşam değerlerini ayrı ayrı değerlendirme
- 🖼️ Streamlit arayüzü ile kolay kullanım
- ✅ Hatalı veya eksik veriler için toleranslı işleme

# Proje Yapısı

tansiyonileri/
├── app.py # Streamlit arayüzü
├── tsyn/ # Tüm modüller burada
│ ├── init.py
│ ├── config.py # Ayarlar
│ ├── data_loader.py # Excel dosyası okuma
│ ├── model.py # KMeans modeli ve mantığı
│ ├── preprocessing.py # Tansiyon verilerini ayrıştırma
│ └── viz.py # Görselleştirme fonksiyonları
├── tansiyon.xlsx # Örnek veri dosyası
└── README.md # 

# Kurulum

 Gerekli paketleri kur:
   ```bash
   pip install streamlit pandas scikit-learn matplotlib openpyxl

   
Uygulamayı çalıştır:
streamlit run app.py

 Kullanılan Kütüphaneler

streamlit
pandas
numpy
scikit-learn
matplotlib


Eda Nur Unal
