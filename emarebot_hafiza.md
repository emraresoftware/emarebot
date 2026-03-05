# 🧠 Emarebot Hafıza — Kozmopol Proje Dokümantasyonu

> 🔗 **Ortak Hafıza:** [`EMARE_ORTAK_HAFIZA.md`](/Users/emre/Desktop/Emare/EMARE_ORTAK_HAFIZA.md) — Tüm Emare ekosistemi, sunucu bilgileri, standartlar ve proje envanteri için bak.


> **Bu dosya yazılımın tüm detaylarını içerir.**
> Nerede kaldığımızı, ne yaptığımızı, hangi teknolojileri kullandığımızı ve
> bir sonraki adımda ne yapacağımızı hatırlamak için taşınabilir referans dosyasıdır.
>
> **Son güncelleme:** 3 Mart 2026
> **Çalışma ortamı:** macOS 26.3, Python 3.12.12 (Homebrew), Tcl/Tk 9.0
> **Python yolu:** `/usr/local/bin/python3.12`
> **Proje dizini:** `/Users/emre/Desktop/trendyol_bot_kozmo`

---

## 1. PROJE NE?

**Kozmopol**, Trendyol üzerinde kozmetik ve kişisel bakım ürünleri satan bir mağazanın
müşteri sorularını **otomatik olarak yanıtlayan** masaüstü uygulamasıdır.

### Temel Yetenekler
- Trendyol Seller API üzerinden gelen müşteri sorularını otomatik çeker
- Anahtar kelime eşleştirmesi → Bulanık eşleştirme → Gemini AI zinciriyle yanıt üretir
- Eşleşme bulunamazsa soruyu "Bekleyen" kuyruğuna atar (manuel onay)
- Ürün yorumlarını çekerek AI yanıtlarını zenginleştirir
- Kargo/iade takibi, sipariş görüntüleme
- Günlük rapor, istatistikler, kategori analizi
- Kelime kara listesi ile hassas içerik filtresi
- Mesai saatleri dışında otomatik mesaj gönderimi
- Açık/Koyu tema desteği (Emare Finance Design Guide uyumlu)

### Kimin İçin?
Trendyol satıcılarının müşteri hizmetlerini otomasyona geçirmesi için geliştirilmiş
bağımsız masaüstü yazılımı. Sunucu gerektirmez, `.env` dosyasıyla konfigüre edilir.

---

## 2. VERSİYON GEÇMİŞİ

| Versiyon | Tarih | Satır | Açıklama |
|----------|-------|-------|----------|
| v1.0 | İlk versiyon | 411 | Temel Tkinter bot, basit anahtar kelime eşleştirme |
| v2.0 | 2 Mart 2026 | 2.159 | Gemini AI eklendi, 6 sekmeli UI, kargo/iade takibi, istatistikler |
| v2.5 | 2 Mart 2026 | ~2.500 | Yorum entegrasyonu, AI eğitimi için review çekme, Yorumlar sekmesi |
| v3.0 | 3 Mart 2026 | 3.603 | Tüm özellikler: 9 sekme, şablon sistemi, kara liste, mesai saatleri, bildirimler |
| v3.0-modüler | 3 Mart 2026 | 3.627 | Monolith → 20 dosyalı modüler yapıya geçiş |
| v3.0-design | 3 Mart 2026 | 3.627 | Emare Finance Design Guide renk paleti ve tipografi uygulandı |

### Yedek Dosyalar
| Dosya | Satır | Boyut |
|-------|-------|-------|
| `kozmopol_v1_backup.py` | 411 | 17K |
| `kozmopol_v2_backup.py` | 2.159 | 82K |
| `kozmopol_v3_monolith_backup.py` | 3.603 | 139K |
| `kozmopol.py` | 3.603 | 139K — eski monolith, artık kullanılmıyor |

---

## 3. DOSYA & KLASÖR YAPISI

```
trendyol_bot_kozmo/
│
├── main.py                          ← GİRİŞ NOKTASI (python3.12 main.py)
├── config.py                        ← Tüm sabitler, API keys, tema, kategoriler
│
├── core/                            ← İŞ MANTIĞI
│   ├── __init__.py
│   ├── data.py                      ← Veri depoları, JSON I/O, yardımcı fonksiyonlar
│   ├── matcher.py                   ← Anahtar kelime + bulanık eşleştirme
│   ├── processor.py                 ← Soru işleme zinciri, arka plan thread
│   └── metrics.py                   ← Performans metrikleri, günlük rapor
│
├── api/                             ← DIŞ SERVİSLER
│   ├── __init__.py
│   ├── trendyol.py                  ← Trendyol Seller API (Q&A, sipariş, iade, yorum)
│   └── gemini.py                    ← Google Gemini AI entegrasyonu
│
├── ui/                              ← KULLANICI ARAYÜZÜ (Tkinter)
│   ├── __init__.py
│   ├── app.py                       ← Ana App penceresi, tema sistemi, ttk stilleri
│   ├── dialogs.py                   ← Ortak düzenleme diyaloğu
│   ├── tab_responses.py             ← Otomatik Yanıtlar sekmesi
│   ├── tab_pending.py               ← Bekleyen Sorular sekmesi
│   ├── tab_templates.py             ← Şablonlar sekmesi
│   ├── tab_orders.py                ← Kargo & İade sekmesi
│   ├── tab_log.py                   ← Soru Geçmişi sekmesi
│   ├── tab_reviews.py               ← Yorumlar sekmesi
│   ├── tab_ai.py                    ← AI Ayarları sekmesi
│   ├── tab_stats.py                 ← İstatistikler sekmesi
│   └── tab_settings.py              ← Ayarlar sekmesi
│
├── automated_responses.json         ← ~30 anahtar kelime→yanıt kuralı
├── question_log.json                ← Yanıtlanan soru geçmişi
├── pending_questions.json           ← Bekleyen sorular kuyruğu
├── response_templates.json          ← 6 yanıt şablonu
├── word_blacklist.json              ← 10 yasaklı kelime
├── app_settings.json                ← Uygulama ayarları
├── .env                             ← API anahtarları (gizli)
├── .env.example                     ← .env şablonu
├── requirements.txt                 ← Bağımlılıklar
├── DESIGN_GUIDE.md                  ← Emare Finance tasarım rehberi
└── kozmopol.log                     ← Uygulama log dosyası
```

---

## 4. DOSYA DETAYLARI — SATIR SAYILARI

| Dosya | Satır | Görev |
|-------|-------|-------|
| `config.py` | 375 | Sabitler, ortam değişkenleri, kategoriler, tema, varsayılanlar |
| `main.py` | 52 | Giriş noktası: veri yükle → App oluştur → thread başlat → mainloop |
| `core/data.py` | 288 | Tüm veri depoları, JSON okuma/yazma, normalize, kategorize, bildirim |
| `core/matcher.py` | 88 | exact_keyword_match, fuzzy_keyword_match, get_quick_suggestions |
| `core/processor.py` | 203 | process_question zinciri, arka plan polling thread |
| `core/metrics.py` | 170 | get_performance_metrics, generate_daily_report, sentiment analizi |
| `api/trendyol.py` | 226 | Trendyol API çağrıları (Q&A, sipariş, iade, yorum) |
| `api/gemini.py` | 77 | generate_gemini_response — AI yanıt üretimi |
| `ui/app.py` | 452 | Ana pencere, ttk stilleri, topbar, tema toggling |
| `ui/dialogs.py` | 79 | Ortak düzenleme penceresi |
| `ui/tab_responses.py` | 294 | Otomatik Yanıtlar CRUD + CSV import/export |
| `ui/tab_pending.py` | 357 | Bekleyen Sorular: onayla/düzenle/reddet/toplu işlem |
| `ui/tab_templates.py` | 211 | Şablon yönetimi, {{değişken}} sistemi |
| `ui/tab_orders.py` | 153 | Sipariş ve iade listesi (Trendyol API) |
| `ui/tab_log.py` | 177 | Soru geçmişi, filtre, günlük rapor, CSV export |
| `ui/tab_reviews.py` | 237 | Ürün yorumları çekme, analiz, filtreleme |
| `ui/tab_ai.py` | 208 | Gemini yapılandırma (model, sıcaklık, prompt) + test |
| `ui/tab_stats.py` | 184 | Kart istatistikleri, yöntem dağılımı, kategori, saatlik grafik |
| `ui/tab_settings.py` | 234 | Mesai, bildirim, polling, kara liste, varsayılanlara dön |
| **TOPLAM (modüler)** | **~3.627** | |

---

## 5. TEKNOLOJİ YIĞINI

| Teknoloji | Versiyon | Kullanım |
|-----------|----------|----------|
| **Python** | 3.12.12 (Homebrew) | Ana dil |
| **Tkinter / ttk** | Tcl/Tk 9.0.3 | Masaüstü GUI çerçevesi |
| **Trendyol Seller API** | REST | Q&A, sipariş, iade, yorum endpoints |
| **Google Gemini AI** | `google-generativeai` 0.8.6 | Akıllı yanıt üretimi |
| **requests** | 2.32.5 | HTTP istekleri |
| **python-dotenv** | 1.2.2 | .env ortam değişkenleri |
| **difflib** | stdlib | SequenceMatcher ile bulanık eşleştirme |
| **threading** | stdlib | Arka plan API polling |
| **csv** | stdlib | İmport/export |
| **json** | stdlib | Veri kalıcılığı |

### Bağımlılıklar (requirements.txt)
```
requests
python-dotenv
google-generativeai
```

### Çalıştırma
```bash
cd /Users/emre/Desktop/trendyol_bot_kozmo
/usr/local/bin/python3.12 main.py
```

> **⚠️ NOT:** Sistem Python'u (3.9.6) Tcl/Tk 8.5 içerdiğinden macOS 26 ile uyumsuz.
> Homebrew Python 3.12 + python-tk@3.12 kullanılmalı.

---

## 6. API ENTEGRASYONLARI

### 6.1 Trendyol Seller API

| Endpoint | Dosya | Fonksiyon |
|----------|-------|-----------|
| `GET /integration/qna/sellers/{supplierId}` | `api/trendyol.py` | `get_customer_questions()` |
| `PUT /integration/qna/sellers/{supplierId}` | `api/trendyol.py` | `answer_question(qid, text)` |
| `GET /integration/order/sellers/{supplierId}` | `api/trendyol.py` | `get_orders(days)` |
| `GET /integration/order/sellers/{supplierId}/claims` | `api/trendyol.py` | `get_claims()` |
| `GET /reviews` (ürün bazlı) | `api/trendyol.py` | `fetch_product_reviews()`, `fetch_all_reviews()` |

**Kimlik doğrulama:** HTTP Basic Auth (`API_KEY`, `API_SECRET_KEY`)

### 6.2 Google Gemini AI

| Parametre | Varsayılan | Açıklama |
|-----------|-----------|----------|
| Model | `gemini-2.0-flash` | Hızlı, düşük maliyetli model |
| Temperature | 0.3 | Tutarlı yanıtlar için düşük |
| Max tokens | 500 | Kısa yanıtlar |
| Güven eşiği | 0.7 | Altındaki yanıtlar bekleyen kuyruğuna |
| Bulanık eşik | 0.65 | Fuzzy matching minimum skoru |
| Auto-send | false | AI yanıtları otomatik gönderilmesin (onay gerekli) |

**Sistem promptu özeti (11 kural):**
1. Nazik ve profesyonel ol
2. "Merhaba" ile başla, "Saygılar Kozmopol" ile bitir
3. Tıbbi bilgi verme, üretici firmaya yönlendir
4. Kargo: Trendyol Express + Kolay Gelsin Kargo
5. İade: Trendyol müşteri hizmetlerine yönlendir
6. Ürün orijinalliğini onayla
7. Hamile/emziren sorularında dikkatli ol
8. Maks 3-4 cümle
9. Emin değilsen `[MANUAL_REVIEW]` ekle
10. Müşteri yorumlarından yararlan
11. Olumlu yorumları öne çıkar, olumsuzlara çözüm öner

---

## 7. SORU İŞLEME ZİNCİRİ (Processing Pipeline)

```
Trendyol API'den soru çekildi
        │
        ▼
┌─ 1. Mesai Saati Kontrolü ─────────────────────────┐
│   Mesai dışı + checkbox aktif → OUT_OF_SERVICE_MSG │
└────────────────────────────────────────────────────┘
        │ (mesai içi)
        ▼
┌─ 2. Anahtar Kelime Eşleştirme (exact) ───────────┐
│   automated_responses içinde AND mantığıyla arar   │
│   Tüm kelimeler metinde varsa → yanıt bul         │
└────────────────────────────────────────────────────┘
        │ (eşleşme yok)
        ▼
┌─ 3. Bulanık Eşleştirme (fuzzy) ──────────────────┐
│   SequenceMatcher ile %65+ benzerlik aranır        │
│   En iyi eşleşme bulunursa → yanıt kullan         │
└────────────────────────────────────────────────────┘
        │ (eşleşme yok)
        ▼
┌─ 4. Gemini AI ───────────────────────────────────┐
│   Sistem promptu + örnek yanıtlar + ürün yorumları │
│   → AI yanıt üretir                                │
│   Güven > %70 + auto_send → otomatik gönder       │
│   Güven < %70 → bekleyen kuyruğuna at              │
│   Kara liste tespit → onaya al                     │
└────────────────────────────────────────────────────┘
        │ (AI devre dışı veya başarısız)
        ▼
┌─ 5. Bekleyen Kuyruğu ───────────────────────────┐
│   pending_questions.json'a kaydet                  │
│   Manuel onay/düzenleme/reddet bekle               │
└────────────────────────────────────────────────────┘
```

**Arka plan thread:** Her `poll_interval` saniyede (varsayılan 300) Trendyol API'yi sorgular.

---

## 8. VERİ MODELLERİ

### 8.1 automated_responses.json
```json
{
  "('anahtar', 'kelime')": "Merhaba, yanıt metni... Saygılar",
  "('kargo', 'ne zaman')": "Merhaba, gönderilerimiz 1-3 iş günü..."
}
```
- Key: Virgülle ayrılmış anahtar kelimeler (tuple string)
- Value: Yanıt metni

### 8.2 question_log.json
```json
[
  {
    "question_id": 123456,
    "question": "Ürün orijinal mi?",
    "answer": "Merhaba, tüm ürünlerimiz orijinaldir...",
    "method": "keyword",
    "product_info": "Ürün Adı | Marka",
    "category": "urun",
    "timestamp": "2026-03-02T14:30:00"
  }
]
```

### 8.3 pending_questions.json
```json
[
  {
    "question_id": 789,
    "question": "Bu ürünü hamile kullanabilir mi?",
    "suggested_answer": "Merhaba, ...",
    "confidence": 0.55,
    "category": "hamile",
    "status": "pending",
    "timestamp": "2026-03-03T10:15:00"
  }
]
```
- Status değerleri: `pending`, `no_match`, `sent`, `rejected`

### 8.4 response_templates.json
```json
[
  {
    "name": "Kargo Bilgisi",
    "text": "Merhaba, gönderilerimizi ... {{ek_bilgi}} Saygılar",
    "variables": ["ek_bilgi"],
    "category": "kargo"
  }
]
```

---

## 9. SORU KATEGORİLERİ

| Kod | Etiket | İkon | Renk | Anahtar Kelimeler (örnek) |
|-----|--------|------|------|---------------------------|
| `kargo` | Kargo / Teslimat | 📦 | `#6366f1` | kargo, teslimat, nerede, takip |
| `iade` | İade / Para İade | ↩️ | `#ef4444` | iade, para iade, iptal, değişim |
| `urun` | Ürün Bilgisi | 🧴 | `#22c55e` | orijinal, içindekiler, nasıl kullanılır |
| `skt` | Son Kullanma Tarihi | 📅 | `#f59e0b` | skt, son kullanma, tarih |
| `sac_boyasi` | Saç Boyası | 💇 | `#9333ea` | boya, saç boyası, ton, renk |
| `hamile` | Hamile / Emziren | 🤰 | `#ec4899` | hamile, emziren, bebek, gebelik |
| `paketleme` | Paketleme / Özen | 📋 | `#8b5cf6` | paket, kırık, hasar, akmış |
| `hediye` | Hediye / Özel İstek | 🎁 | `#4f46e5` | hediye, not, mesaj, sürpriz |
| `diger` | Diğer | ❓ | `#6b7280` | (eşleşmeyenler) |

---

## 10. TASARIM SİSTEMİ (Emare Finance Design Guide)

### Marka Renk Paleti (Indigo)
| Token | HEX | Kullanım |
|-------|-----|----------|
| brand-50 | `#eef2ff` | Açık arka plan, hover bg, kart bg (light) |
| brand-100 | `#e0e7ff` | Border, kart çerçeve, highlight |
| brand-200 | `#c7d2fe` | Status bar fg, scrollbar |
| brand-500 | `#6366f1` | **Ana marka rengi (Primary)** — sekmeler, butonlar, accent |
| brand-600 | `#4f46e5` | Hover/active, soru metin rengi |
| brand-700 | `#4338ca` | Pressed buton, koyu accent |
| brand-900 | `#312e81` | Dark tema kart bg |
| brand-950 | `#1e1b4b` | Status bar bg, koyu arka plan |

### Ek Renkler
| Renk | HEX | Kullanım |
|------|-----|----------|
| purple | `#9333ea` | Gradient bitiş, saç boyası kategori |
| green | `#22c55e` | Başarı, ürün kategori |
| amber | `#f59e0b` | Uyarı, SKT kategori |
| red | `#ef4444` | Hata, iade kategori, danger buton |
| pink | `#ec4899` | Hamile kategori |
| cyan | `#06b6d4` | İstatistik accent |

### Tipografi
- **Font ailesi:** Inter → SF Pro Display → Helvetica Neue → Segoe UI
- **Hero:** 20px bold
- **H1:** 16px bold
- **H2:** 14px bold
- **Body:** 12px regular
- **Small:** 10px
- **Stat number:** 28px bold
- **Mono:** SF Mono → Menlo → Courier

### Light Tema
- Arka plan: `#ffffff`
- Kart bg: `brand-50`
- Kart border: `brand-100`
- Metin: `gray-800`
- Status bar: `brand-950` bg / `brand-200` fg

### Dark Tema
- Arka plan: `#0f0a2e` (hero fallback)
- Kart bg: `brand-900`
- Kart border: `brand-800`
- Metin: `brand-100`
- Accent: `brand-400`

---

## 11. UI SEKME DETAYLARI (9 SEKME)

### 📋 Otomatik Yanıtlar (`tab_responses.py`)
- Arama/filtre çubuğu
- Kaydırmalı kart listesi (Canvas + Scrollbar)
- Her kart: kategori badge, soru (brand-500), cevap
- Tıklayarak düzenle (soru veya cevap)
- Yeni ekle, seçiliyi sil
- CSV import/export
- Yenile butonu

### ⏳ Bekleyen Sorular (`tab_pending.py`)
- Treeview tablosu (kategori, zaman, soru, AI önerisi, güven, durum)
- Kategori filtresi (combobox)
- Onayla ve Gönder / Düzenle ve Gönder / Reddet
- Şablondan Yanıt (template ile cevapla)
- Tümünü Onayla / Tümünü Reddet (toplu)
- Yanıt Olarak Kaydet (yeni kural oluştur)
- Tamamlananları Temizle

### 📑 Şablonlar (`tab_templates.py`)
- PanedWindow: sol listbox + sağ önizleme
- `{{değişken}}` sistemi ile dinamik şablonlar
- Kategori bazlı
- Ekle / Düzenle / Sil

### 📦 Kargo & İade (`tab_orders.py`)
- Gün seçici (3/7/14/30)
- Siparişler Treeview (sipariş no, tarih, durum, kargo, ürün, müşteri)
- İadeler Treeview (talep no, tarih, durum, sebep, ürün)
- Threading ile API çağrısı

### 📊 Soru Geçmişi (`tab_log.py`)
- Yöntem filtresi + Kategori filtresi
- Treeview (zaman, kategori, soru, yanıt, yöntem)
- Çift tıkla → detay penceresi
- Günlük Rapor (metin rapor)
- CSV dışa aktarım

### ⭐ Yorumlar (`tab_reviews.py`)
- Yorumları API'den Çek butonu
- Ürün filtresi + Min puan filtresi + Arama
- Treeview (ürün, kullanıcı, puan, tarih, yorum)
- Yorum Analizi → sentiment stats, kelime frekansı
- Temizle butonu

### 🤖 AI Ayarları (`tab_ai.py`)
- Sol panel: Gemini yapılandırma
  - Aktif/deaktif, auto-send, model seçimi, sıcaklık, max token
  - Güven eşiği, bulanık eşik
  - Sistem promptu (ScrolledText)
- Sağ panel: AI Test
  - Soru yaz → Test Et → tüm pipeline sonuçlarını göster
  - Kategori, anahtar kelime, bulanık, ilgili yorumlar, Gemini yanıt

### 📈 İstatistikler (`tab_stats.py`)
- 6 büyük kart: Toplam Soru, Bugün, Bu Hafta, Oto Yanıt Kuralı, Bekleyen, Oto Çözüm Oranı
- Yanıt Yöntemi Dağılımı (bar chart)
- Kategori Dağılımı (bar chart)
- Saatlik Dağılım (08:00-22:00)

### ⚙️ Ayarlar (`tab_settings.py`)
- Mesai Saatleri (başlangıç, bitiş, çalışma günleri)
- Bildirimler (masaüstü bildirimi toggle + test)
- API Sorgulama aralığı (saniye)
- Kelime Kara Listesi (ekle/sil)
- Genel: auto-kategorize, max yanıt uzunluğu
- Tüm Ayarları Kaydet / Varsayılanlara Dön

---

## 12. MİMARİ KARARLAR

### Neden Modüler Yapı?
3.603 satırlık tek dosya yönetilemez hale geldi. 20 dosyalı yapıya geçildi:
- **config.py**: Tüm sabitler tek yerde
- **core/**: İş mantığı (UI'dan bağımsız test edilebilir)
- **api/**: Dış servis çağrıları izole
- **ui/**: Her sekme bağımsız sınıf

### Tab Composition Pattern
Her sekme `__init__(self, app, parent)` ile oluşturulur:
- `app`: Ana App referansı (`_set_status`, `refresh_stats`, `_bind_mousewheel` vb.)
- `parent`: ttk.Frame (notebook sekmesi)

### Circular Import Çözümü
`core/processor.py` → `ui/app.py` erişimi lazy import ile:
```python
import ui.app as _app_mod
app = getattr(_app_mod, '_app_instance', None)
```

### Thread Safety
- `data_lock = threading.Lock()` ile veri erişimi korunur
- UI güncellemeleri `app.after(0, callback)` ile ana thread'de yapılır

---

## 13. .env YAPISI

```env
SUPPLIER_ID=xxxxxxxxx
API_KEY=yyyyyyyyyyyyyy
API_SECRET_KEY=zzzzzzzzzzzzz
GEMINI_API_KEY=AI_xxxxxxxxxxxxxx
```

> **SUPPLIER_ID:** Trendyol satıcı kimliği
> **API_KEY / API_SECRET_KEY:** Trendyol Seller API kimlik bilgileri
> **GEMINI_API_KEY:** Google AI Studio'dan alınan API anahtarı

---

## 14. BİLİNEN SORUNLAR & NOTLAR

| Sorun | Durum | Çözüm |
|-------|-------|-------|
| macOS 26 + sistem Python 3.9 Tk 8.5 uyumsuz | ✅ Çözüldü | Homebrew Python 3.12 + python-tk@3.12 kullan |
| `google-generativeai` paketi deprecated | ⚠️ Uyarı | İleride `google-genai` paketine geçiş yapılmalı |
| GEMINI_API_KEY tanımsız | ℹ️ Normal | .env'de key yoksa AI devre dışı, uygulama çalışmaya devam eder |
| `kozmopol.py` hâlâ dizinde | ℹ️ Temizlik | Eski monolith dosyası. Silinebilir (yedek zaten var) |
| Dark tema toggle | ℹ️ Kısıtlı | Tema değiştirmek uygulamayı yeniden build eder ama bazı tk widget'ları tam geçiş yapmayabilir |

---

## 15. SON DURUM — NEREDE KALDIK?

### Tamamlananlar ✅
1. ✅ v1.0 → v2.0 → v3.0 geliştirme (özellik ekleme)
2. ✅ Gemini AI entegrasyonu + yorum eğitimi
3. ✅ 3.603 satır monolith → 20 dosyalı modüler yapı
4. ✅ Emare Finance Design Guide uygulandı (renk paleti, tipografi, kart stillleri)
5. ✅ Syntax doğrulama (22/22 dosya OK)
6. ✅ Import doğrulama (tüm modüller OK)
7. ✅ Uygulama başarıyla çalıştırıldı

### Yapılabilecek Sonraki Adımlar 🔜
- [ ] `google-generativeai` → `google-genai` paketine geçiş (deprecated uyarısını çözer)
- [ ] Dark tema tam widget desteği (tk.Frame, tk.Label bg/fg propagation)
- [ ] Ürün bazlı otomatik yanıt öğrenme (sık sorulan → otomatik kural)
- [ ] Çoklu dil desteği (şu an sadece Türkçe)
- [ ] Toplu ürün yorum çekme optimizasyonu (sayfalama iyileştirme)
- [ ] Test dosyaları yazılması (pytest)
- [ ] Bildirim sistemi iyileştirme (macOS native bildirimler)
- [ ] Dashboard grafikler (matplotlib veya tkinter Canvas ile)
- [ ] Export: PDF rapor oluşturma
- [ ] Eski `kozmopol.py` monolith dosyasını silme (yedeği var)

---

## 16. HIZLI REFERANS — KOMUTLAR

```bash
# Uygulamayı başlat
cd /Users/emre/Desktop/trendyol_bot_kozmo
/usr/local/bin/python3.12 main.py

# Syntax kontrolü (tüm dosyalar)
/usr/local/bin/python3.12 -c "
import py_compile
files = ['config.py','main.py','core/data.py','core/matcher.py',
         'core/processor.py','core/metrics.py','api/trendyol.py',
         'api/gemini.py','ui/app.py','ui/dialogs.py',
         'ui/tab_responses.py','ui/tab_pending.py','ui/tab_templates.py',
         'ui/tab_orders.py','ui/tab_log.py','ui/tab_reviews.py',
         'ui/tab_ai.py','ui/tab_stats.py','ui/tab_settings.py']
for f in files:
    py_compile.compile(f, doraise=True)
print('OK')
"

# Bağımlılık yükleme
/usr/local/bin/pip3.12 install --break-system-packages requests python-dotenv google-generativeai
```

---

*Bu dosya taşınabilir bir proje hafızasıdır. Yeni bir oturumda bu dosyayı paylaşarak
kaldığınız yerden devam edebilirsiniz.*
