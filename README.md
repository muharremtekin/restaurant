# Restaurant Management System

Bu proje, modern bir restoran yönetim sistemi için Django ve Django REST Framework kullanılarak geliştirilmiş bir web uygulamasıdır.

## 🚀 Özellikler

- 👤 Kullanıcı Kimlik Doğrulama ve Yetkilendirme
- 🍽️ Menü Yönetimi
- 📅 Rezervasyon Sistemi
- 🛒 Sipariş Takibi
- 💬 Müşteri Yorumları
- 📊 Yönetici Paneli

## 🛠 Teknolojiler

- Python 3.8+
- Django 5.0
- Django REST Framework
- MySQL
- Bootstrap 5
- JavaScript (ES6+)

## 📋 Gereksinimler

```bash
Python 3.8 veya üzeri
MySQL 8.0 veya üzeri
pip (Python paket yöneticisi)
virtualenv veya venv (sanal ortam için)
```

## 🔧 Kurulum

1. Projeyi klonlayın
```bash
git clone https://github.com/your-username/restaurant-project.git
cd restaurant-project
```

2. Sanal ortam oluşturun ve aktif edin
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

3. Gerekli paketleri yükleyin
```bash
pip install -r requirements.txt
```

4. .env dosyasını oluşturun
```bash
# .env dosyası örneği
DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=restaurant_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306
```

5. Veritabanı migrations'larını yapın
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Admin kullanıcısı oluşturun
```bash
python manage.py createsuperuser
```

7. Sunucuyu başlatın
```bash
python manage.py runserver
```

## 📁 Proje Yapısı

```
restaurant_project/
├── api/                    # API uygulaması
│   ├── models.py          # Veritabanı modelleri
│   ├── serializers.py     # API serializers
│   ├── views.py           # API views
│   └── urls.py            # API URL patterns
├── authentication/         # Kimlik doğrulama uygulaması
├── static/                # Statik dosyalar
│   ├── css/
│   ├── js/
│   └── img/
├── templates/             # HTML şablonları
├── manage.py
└── requirements.txt
```

## 🔌 API Endpoints

### Menü İşlemleri
- `GET /api/menu-items/` - Tüm menü öğelerini listele
- `GET /api/menu-items/{id}/` - Belirli bir menü öğesinin detaylarını getir
- `POST /api/menu-items/` - Yeni menü öğesi ekle (Admin)
- `PUT /api/menu-items/{id}/` - Menü öğesi güncelle (Admin)
- `DELETE /api/menu-items/{id}/` - Menü öğesi sil (Admin)

### Rezervasyon İşlemleri
- `GET /api/reservations/` - Kullanıcının rezervasyonlarını listele
- `POST /api/reservations/` - Yeni rezervasyon oluştur
- `PUT /api/reservations/{id}/` - Rezervasyon güncelle
- `DELETE /api/reservations/{id}/` - Rezervasyon iptal et

### Sipariş İşlemleri
- `GET /api/orders/` - Kullanıcının siparişlerini listele
- `POST /api/orders/` - Yeni sipariş oluştur
- `GET /api/orders/{id}/` - Sipariş detaylarını getir

## 👥 Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir özellik branch'i oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Bir Pull Request oluşturun

## 📝 Test

Testleri çalıştırmak için:
```bash
python manage.py test
```

## 🔒 Güvenlik

- API erişimi için token tabanlı kimlik doğrulama kullanılmaktadır
- Hassas veriler için .env dosyası kullanılmaktadır
- Cross-Site Request Forgery (CSRF) koruması aktiftir
- SQL Injection koruması için ORM kullanılmaktadır

## 📜 Lisans

Bu proje MIT lisansı altında lisanslanmıştır - Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 📧 İletişim

Proje Sorumlusu - [@your-twitter](https://twitter.com/your-twitter)

Proje Linki: [https://github.com/your-username/restaurant-project](https://github.com/your-username/restaurant-project)
