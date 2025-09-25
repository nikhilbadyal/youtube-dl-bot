from enum import Enum


class Links(Enum):
    STANDART = [
        # YouTube
        "https://www.youtube.com/",
        "https://youtu.be/",
        "https://www.youtube.com/shorts/",
        "https://youtube.com/shorts/",
        # TikTok
        "https://www.tiktok.com/",
        "https://vt.tiktok.com/",
        "https://vm.tiktok.com/",
        # Instagram
        "https://www.instagram.com/reel/",
        "https://instagram.com/reel/",
        "https://www.instagram.com/share/",
        # Twitter (X)
        "https://x.com/",
        "https://twitter.com/",
        # Facebook
        "https://www.facebook.com/reel/",
        "https://www.facebook.com/share/",
    ]


class Messages(Enum):
    VideoProcessing = "<code>{url}</code>\n\n⏳ Your video is being processed..."
    VideoSuccess = "<code>{url}</code>\n\n✅ Your video has been successfully downloaded. Sending..."
    VideoNotSent = "<code>{url}</code>\n\n❌ Unfortunately, the video exceeds Telegram limits."
    VideoError = "<code>{url}</code>\n\n⚠️ An error occurred during the download."

    Promo = (
        "Hi! I'm <b>@free_yt_dl_bot</b> — 100% free, no ads, no forced subscriptions.\n\n"
        "If you like my work, support me by checking out my "
        "<b><a href='https://t.me/anekobtw_c'>Telegram news channel</a></b> 😊\n\n"
        "<b>This message will self-delete in 15 seconds.</b>"
    )  # fmt: skip

    Caption = "<b><i><a href='https://t.me/free_yt_dl_bot'>via</a> | <a href='{url}'>link</a></i></b>"

    Start = (
        "Hello, @{username}! Just send the link to the video.\n\n"

        "ℹ️ <b>We don’t collect any data.</b>\n\n"

        "❗ <b>If the bot isn’t working, don’t worry</b> — your request will be processed automatically once we're back online.\n\n"

        "🙏 <b>Please don’t block the bot</b> — it needs to message you when the download is ready."
    )  # fmt: skip
