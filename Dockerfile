# Используем легковесный Python образ
FROM python:3.10-slim

# Обновляем пакеты и устанавливаем ffmpeg
RUN apt-get update && apt-get install -y ffmpeg && apt-get clean

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект внутрь контейнера
COPY . .

# Запускаем бота
CMD ["python", "bot.py"]
