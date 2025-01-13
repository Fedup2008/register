# 🎉 Register Project 🎉

📌 *Bu loyiha foydalanuvchilarning ro'yxatdan o'tish ma'lumotlarini saqlash uchun ishlab chiqilgan bo'lib, ma'lumotlar avtomatik ravishda database va Telegram botga yuboriladi.*

---

## 🚀 Xususiyatlar
✅ Foydalanuvchi ro'yxatdan o'tish shaklini to'ldiradi  
✅ Ma'lumotlar database-ga saqlanadi  
✅ Ma'lumotlar Telegram bot orqali administratorga yuboriladi  

---

## 📌 Talablar

Loyihani ishga tushirish uchun quyidagi dasturlar o'rnatilgan bo'lishi kerak:

- 🐍 Python 3.x
- 🗄️ PostgreSQL yoki MySQL (yoki boshqa mos keluvchi database)
- 🤖 Telegram Bot API tokeni

---

## 🔧 O'rnatish

### 1️⃣ **Loyihani yuklab oling**

```bash
  git clone https://github.com/username/register-project.git
  cd register-project
```

### 2️⃣ **Virtual muhitni yaratish va faollashtirish**

```bash
  python -m venv venv
  source venv/bin/activate  # Linux/MacOS uchun
  venv\Scripts\activate  # Windows uchun
```

### 3️⃣ **Kerakli kutubxonalarni o'rnatish**

```bash
  pip install -r requirements.txt
```

### 4️⃣ **Database sozlamalarini o'rnatish**

📂 `.env` faylini yarating va quyidagilarni kiriting:

```
DB_HOST=localhost
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
ADMIN_CHAT_ID=your_admin_chat_id
```

### 5️⃣ **Ma'lumotlar bazasini yaratish**

```bash
  python manage.py migrate  # Django uchun
  alembic upgrade head  # SQLAlchemy uchun
```

### 6️⃣ **Loyihani ishga tushirish**

```bash
  python main.py
```

---

## 📌 Foydalanish

1️⃣ Foydalanuvchi ro'yxatdan o'tish formasi orqali ma'lumotlarini yuboradi.  
2️⃣ Ma'lumotlar database-ga yoziladi.  
3️⃣ Telegram bot orqali administratorga xabar yuboriladi.  

---

## 👤 Muallif

**📝 Ismingiz** – [GitHub Profilingiz](https://github.com/username)

---

## 📜 Litsenziya

Bu loyiha **MIT** litsenziyasi asosida tarqatiladi. 📜

