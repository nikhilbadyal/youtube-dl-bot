# `youtube-dl-bot`

![version](https://img.shields.io/badge/Version-3.7.0-blue)
![license](https://img.shields.io/badge/License-CC-red)
![python](https://img.shields.io/badge/Python-3.8%2B-blue)

A Telegram bot for downloading videos from different platforms directly in your chats.

**Live Bot**: [@free_yt_dl_bot](https://t.me/free_yt_dl_bot)

## 🛠️ Setup

### Traditional Setup

**1. Install Python**

**2. Install [ffmpeg](https://ffmpeg.org/download.html)**

**3. Acquire bot token from [@BotFather](https://t.me/BotFather)**

**4. Create a `.env` file in `bot/` folder with:**

```
TOKEN = your_telegram_bot_token_here
```

**5. Clone and install dependencies:**

```bash
$ git clone https://github.com/anekobtw/youtube-dl-bot.git
$ cd youtube-dl-bot/bot
$ pip install -r requirements.txt
```

**6. Run the bot**

```bash
$ python main.py
```

### Docker Setup (Recommended)

**1. Acquire bot token from [@BotFather](https://t.me/BotFather)**

**2. Clone the repository:**

```bash
$ git clone https://github.com/anekobtw/youtube-dl-bot.git
$ cd youtube-dl-bot
```

**3. Create a `.env` file in the root directory with:**

```bash
cp .env.example .env
```

Edit the `.env` file and add your bot token:
```
TOKEN=your_telegram_bot_token_here
PUBLIC_URL=http://localhost:8000
```

**4. Build and run with Docker Compose:**

```bash
$ docker-compose up -d
```

This will start both the API service (port 8000) and the bot service.

**5. Check logs:**

```bash
$ docker-compose logs -f bot
```

**6. Stop the services:**

```bash
$ docker-compose down
```

## Contributing 🤝
Pull requests, bug reports, and feature suggestions are welcome! Please read our [Code of Conduct](https://github.com/anekobtw/youtube-dl-bot/blob/main/CODE_OF_CONDUCT.md)

## License 📄
©️ All rights reserved by [@anekobtw](https://github.com/anekobtw). Unauthorized copying or redistribution is prohibited.

> // Maintained with ❤️ by [@anekobtw](https://github.com/anekobtw)
