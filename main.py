"""
🎥 Project 5: YouTube Video Downloader (Using yt-dlp)
👨‍💻 Created by: Hashir Adnan
🌐 Website: www.techthf.xyz
🗓️ Date: [Insert today’s date]

📌 Description:
This Python script allows users to download any YouTube video using the yt-dlp library.
It's more reliable than pytube and supports both long-form videos and Shorts.

📦 Features:
- Accepts any YouTube video URL
- Automatically downloads the best available resolution
- Uses yt-dlp (modern, fast, and stable)

🧰 Technologies Used:
- Python
- yt-dlp (https://github.com/yt-dlp/yt-dlp)

💡 Future Improvements:
- Let user select resolution
- Option to download audio only
- Show download progress bar

"""

import yt_dlp

url = input("🎥 Enter YouTube video URL: ")

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

