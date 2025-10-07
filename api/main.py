import asyncio
import os

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from yt_dlp import YoutubeDL

os.makedirs("files", exist_ok=True)

# Get public URL from environment variable or use default
public_url = os.getenv("PUBLIC_URL", "http://localhost:8000")

app = FastAPI()


class DownloadRequest(BaseModel):
    url: str


app.mount("/files", StaticFiles(directory="files"), name="files")


@app.get("/health")
def health():
    return {"status": "ok"}


def process_download(request: DownloadRequest):
    ydl_opts = {
        "outtmpl": "files/%(title)s.%(ext)s",
        "format": (
            "bestvideo[ext=mp4][vcodec^=avc1]+bestaudio[ext=m4a]/"
            "best[ext=mp4][vcodec^=avc1]/"
            "best"
        ),  # fmt: skip
        "merge_output_format": "mp4",
        "writethumbnail": True,
        "postprocessors": [
            # {"key": "FFmpegThumbnailsConvertor", "format": "png"},
            {"key": "FFmpegThumbnailsConvertor", "format": "png"},
            {"key": "FFmpegFixupStretched"},
        ],
        "postprocessor_args": ["-c:v", "copy", "-c:a", "copy"],
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(request.url)
        video_filename = ydl.prepare_filename(info)
        thumbnail_filename = os.path.splitext(video_filename)[0] + ".png"

        return {
            "status": "success",
            "video_url": f"{public_url}/files/{os.path.basename(video_filename)}",
            "thumbnail_url": f"{public_url}/files/{os.path.basename(thumbnail_filename)}",
            "filesize": os.path.getsize(video_filename),
        }


@app.post("/download")
async def download_video(request: DownloadRequest):
    return await asyncio.to_thread(process_download, request)


if __name__ == "__main__":
    asyncio.run(uvicorn.run("main:app", host="0.0.0.0", port=8000))
