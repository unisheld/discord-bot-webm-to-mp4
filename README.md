# 📦 disBot-webm-mp4

Простой Discord-бот, который конвертирует `.webm` файлы в `.mp4` по тегу.

---

### Пример использования:

1. Кто-то отправляет `.webm`:

```bash
some_video.webm
```

2. Ты отвечаешь на сообщение и упоминаешь бота:

```bash
@WebmBot конвертируй!
```

3. Бот скачает `.webm`, сконвертирует в `.mp4` и отправит обратно.

---

##  Возможности

- Поддержка цитируемых сообщений
- Только если упомянуть бота
- Автоудаление временных файлов
- Проверка наличия `ffmpeg`

---

##  Установка

1. Клонируй репозиторий:

```bash
git clone https://github.com/unisheld/discord-webm-mp4.git
cd discord-webm-mp4
```

2. Установи зависимости:

```bash
pip install -r requirements.txt
```
3. Создай .env файл:

```bash
DISCORD_TOKEN=твой_токен_бота
```

4. Убедись, что ffmpeg установлен и доступен из PATH:

```bash
ffmpeg -version
```

## Запуск
```bash
python bot.py
```