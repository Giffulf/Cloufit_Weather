# Cloufit Weather 🌦️👔  

**Умный гид по выбору одежды по погоде**  
*Разработан в рамках учебного проекта в [Название ВУЗа]*

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi)](https://fastapi.tiangolo.com/)
[![OpenWeather](https://img.shields.io/badge/OpenWeather-API-green)](https://openweathermap.org)

## 📌 О проекте  

Cloufit — веб-приложение, которое:  
✅ Анализирует погоду с помощью OpenWeather API  
✅ Даёт персонализированные рекомендации по одежде  
✅ Учитывает ваш гардероб, стиль и метеочувствительность  
✅ Показывает визуальные примеры образов  

**Целевая аудитория**:  
- Жители регионов с переменчивой погодой  
- Путешественники  
- Люди, следящие за комфортом и стилем  

## 🚀 Быстрый старт  

### 1. Установка  

```
# Клонировать репозиторий
git clone https://github.com/Giffulf/Cloufit_Weather.git
cd Cloufit_Weather

# Создать виртуальное окружение (Windows)
python -m venv .venv
.venv\Scripts\activate.bat

# Установить зависимости
pip install -r requirements.txt
```

### 2. Настройка  
1. Получите API-ключ на [OpenWeatherMap](https://openweathermap.org/api)  
2. Создайте файл `.env` в корне проекта:  
```
ini
   OPENWEATHER_API_KEY=ваш_ключ
```

### 3. Запуск  
```
fastapi dev main.py
```
Откройте [http://localhost:8000](http://localhost:8000)  

## 🛠 Технологии  

| Компонент       | Технологии                          |
|-----------------|-------------------------------------|
| Backend         | Python, FastAPI, SQLAlchemy         |
| Frontend        | HTML/CSS, Bootstrap, Jinja2         |
| Данные о погоде | OpenWeatherMap API                  |
| Инфраструктура  | Docker, Nginx (для продакшена)      |

## 👥 Команда проекта  

| Роль               | Участник                          | Контакты                     |
|--------------------|-----------------------------------|------------------------------|
| Руководитель       | Зиновьев Данил Федорович         | danil.zinovev.16@mail.ru     |
| Backend-разработчик | Ширяева Юлиана Александровна     | giffulf@mail.ru              |
| Frontend-разработчик| Кравцова Екатерина Дмитриевна    | ekaterina19kravtsova@gmail.com |
| Аналитик           | Буракова Полина Андреевна        | POL-BUR27@YANDEX.RU          |

*Учебный проект © 2024 | [МИИГАиК]*  
