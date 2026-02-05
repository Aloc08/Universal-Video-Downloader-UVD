![Version](https://img.shields.io/badge/6.0.0-155875)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)](#)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](#)
[![License](https://img.shields.io/badge/license-MIT-green)](#)
<p align="left">
  <img src=https://github.com/Aloc08/Universal-Video-Downloader-UVD/blob/ceb403d302d9dffce8f083e171834f9e2425d9cb/Logo/UVD_logo.png width=150)>
  <img src="https://raw.githubusercontent.com/yt-dlp/yt-dlp/master/.github/banner.svg" width="130">
  <img src="https://github.com/Aloc08/Universal-Video-Downloader-UVD/blob/31935bbf13331e543def6c6b5a9f42b4ac65058d/Logo/ffmpeg_logo.svg" width="40">
  <img src="https://github.com/Aloc08/Universal-Video-Downloader-UVD/blob/31935bbf13331e543def6c6b5a9f42b4ac65058d/Logo/Deno_Logo.svg" width="80">
</p>


---

# Universal-Video-Downloader

**UVD** is a lightweight and powerful command-line multimedia downloader built on top of **yt-dlp**, designed to download videos, audio tracks, subtitles, and playlists from **all websites supported by yt-dlp**.
Everything runs **locally on your machine**, so **no external servers** are used.
No subscriptions or accounts are needed.

---

## Features

### What UVD adds
- Simplified CLI syntax for common download tasks
- 📂 Automatic playlist handling:
  - Playlists are automatically detected when a playlist URL is provided.
  - No additional flags are required.
- 🔄 Smart format and quality fallback
- Subtitle download
- Unified handling of video, audio and subtitles

### Powered by yt-dlp
- 🌐 Multi-site support
    - The full list is available [here](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md).
- ⚙️ Fully local execution
- 🚫 No download limits
- 🚫 No external servers

### 🎞️ Video download formats:
  - AV1 (MKV)
  - VP9 (MKV)
  - H.264 / MP4
  - Quality selection from **360p up to 8K**
### 🎵 Audio extraction:
  - Opus
  - MP3
  - FLAC
### 📝 Subtitles:
  - Manual subtitles
  - Auto-generated subtitles
  - Download all available languages
  - Automatic conversion to **SRT**

---

## How to use

### 💽 Executable version - Windows

With this version, no additional downloads are required besides the executable itself.

➡️ It is recommended to add the program to your system **PATH**. 
This allows you to run it from any command prompt.
If you need help with this procedure, please refer to '`how_to_path.md`'.

---

### 📦 Bundled Version - Linux & macOS

With this version it's needed:
- **Python 3.10 or newer**

> ⚠️ `yt-dlp` and `ffmpeg` are bundled in the releases to simplify setup for end users.  
> ❌ No other installations are needed. For expert users you can download them manually and add them to `path`.

To use the program with python, you need to do so: 
```bash
py main_uvd.py <args>
```

---

### 🛠️ Building your own executable from source (For expert users only)

0 - Advanced users can build their own **executable** starting from the source code using **PyInstaller**.
    To do this, you must download the `Bundled Version` release, as it already contains all **required** **dependencies** (such as yt-dlp, ffmpeg and deno) included in the project structure.

1 - First make sure you have **Python 3.10** or newer installed.

2 - **Download** and extract the `Bundled Version` of the release.

3 - Install PyInstaller:
```
pip install pyinstaller
```

4 - From the project root directory, run:
```
pyinstaller --onefile --add-data ".\bin\:.\bin" .\main_uvd.py
```

5 - Done! Once the build process is complete, the executable will be available in the `dist/` folder.

---

## 🚀 Usage

### 📃 General syntax

```bash
UVD [-h] [-f {av1,vp9,mp4,opus,mp3,flac}] [-q {360p,480p,720p,1080p,1440p,4k,8k}] [-dir DIRECTORY] [-s [SUBS]]
    [-v]
    url
```

### 🆘 Help & Info
```bash
positional arguments:
  url                   Multimedia URL to download

options:
  -h, --help                                        show this help message and exit
  -f, --format {av1,vp9,mp4,opus,mp3,flac}          Format to download [av1, vp9, mp4, opus, mp3, flac | default: none  | i for info]
  -q, --quality {360p,480p,720p,1080p,1440p,4k,8k}  Quality to download [360p, 480p, 720p, 1080p, 1440p, 4k, 8k | default: best]
  -dir, --directory DIRECTORY                       Directory where the file will be saved (default: pc videos dir)
  -s, --subs [SUBS]                                 Subtitles languages to download (comma separated, e.g. en,it,en-US or 'all')
  -v, --version                                     Show program's version
```
---

## 💫 Why UVD?

UVD focuses on simplicity, transparency and local execution:
- No subscriptions or accounts
- No advertisements or tracking
- Fully local execution
- No artificial limits
- Open source and transparent by design
- Not intended for commercial purposes

---

## Supported Platforms

- Windows
- Linux
- macOS (not yet tested)

---

## ⚠️ Notes

 - **UVD does not bypass *DRM***.
 - Available formats and qualities depend on the source website.

---

## 🔐 Privacy
UVD does not collect user data, track activity, or store cookies.
Network traffic is handled entirely by yt-dlp and external services.
For additional privacy, users may choose to use a VPN.

---

## ⚖️ Legal Disclaimer

This software is provided for **educational and personal use only**.
Users are responsible for complying with the terms of service and copyright laws of the websites they download content from.
**The author assumes no liability for misuse**.

UVD makes use of third-party software, including **yt-dlp**, **FFmpeg** and **Deno**, which are subject to their respective licenses and trademarks rights.

All product names, logos, trademarks, and registered trademarks are property of their respective owners and are used for identification purposes only.

**This project is not affiliated, associated, authorized, endorsed by, or in any way officially connected to any other software or platform**.  

---

## 💡 Contributing

Found a bug? Have a suggestion? Want to contribute?  
Feel free to [open an issue](https://github.com/Aloc08/Universal-Video-Downloader/issues).

---

## ☕ Donations

If you enjoy this project and want to support its development, consider buying me a coffee!  
Your contribution helps keep the project alive and motivates further updates and features.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/R5R01HZ2ZF)

---

## Credits

Developed and maintained by [Aloc08](https://github.com/Aloc08) 
with the contribution of [FOcculto](https://github.com/FOcculto).

---

## License

This project is licensed under the [MIT LICENSE](LICENSE).

