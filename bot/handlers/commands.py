import asyncio
import os
import random

import yt_dlp
from aiogram import F, Router, exceptions, types
from aiogram.filters import CommandStart
from enums import Links, Messages

router = Router()


async def download_video(url: str) -> str:
    opts = {
        "format": "bestvideo[vcodec^=avc1][ext=mp4]+bestaudio[acodec^=mp4a]/mp4",
        "merge-output-format": "mp4",
        "outtmpl": "%(title)s.%(ext)s",
        "noplaylist": True,
        "quiet": True,
        "postprocessors": [
            {
                "key": "FFmpegVideoConvertor",
                "preferedformat": "mp4",
            }
        ],
    }

    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return {
            "filename": ydl.prepare_filename(info),
            "width": info.get("width", 0),
            "height": info.get("height", 0),
        }


def link_button(text: str, url: str) -> types.InlineKeyboardMarkup:
    return types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text=text, url=url)]])


@router.message(F.text.startswith(tuple(Links.STANDART.value)))
async def handle_standart_download(message: types.Message):
    url = message.text
    eyes_emoji = [types.reaction_type_emoji.ReactionTypeEmoji(emoji="👀")]

    await message.react(eyes_emoji)
    msg = await message.answer(Messages.VideoProcessing.value.format(url=url))

    try:
        info = await download_video(url)

        await msg.edit_text(Messages.VideoSuccess.value.format(url=url))

        await message.answer_video(
            video=types.FSInputFile(info["filename"]),
            caption=Messages.Caption.value.format(url=url),
            width=info["width"],
            height=info["height"],
        )

    except exceptions.TelegramEntityTooLarge:
        await msg.edit_text(Messages.VideoNotSent.value.format(url=url))
        return

    except Exception:
        await msg.edit_text(Messages.VideoError.value.format(url=url))
        return

    await message.delete()
    await msg.delete()
    os.remove(info["filename"])

    if random.randint(1, 5) == 1:
        promo_msg = await message.answer(Messages.Promo.value)
        await asyncio.sleep(15)
        await promo_msg.delete()


@router.message(CommandStart())
async def start(message: types.Message) -> None:
    await message.answer(
        text=Messages.Start.value.format(username=message.from_user.username),
        reply_markup=link_button("📰 A Telegram channel with news", "t.me/nikhilbadyal_projects"),
    )
