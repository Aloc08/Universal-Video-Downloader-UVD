# Frequently Asked Questions (FAQ)

---

## ❓ What websites does UVD support?

UVD supports **all websites supported by yt-dlp**.

A full and always-updated list is available here:  
https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md

---

## ❓ Does UVD use external servers?

No.  
UVD runs **entirely on your local machine**.

- No cloud servers
- No proxies
- No middlemen

All downloads are performed directly between **your computer and the target website**, using yt-dlp.

---

## ❓ Are there any download limits?

No.  
UVD does **not impose any artificial limits**.

Any limitation depends solely on:
- the target website
- your internet connection
- the available formats and qualities

---

## ❓ Does UVD support playlists?

Yes.  
Playlists are handled **automatically**.

- If you provide a playlist URL, UVD downloads the entire playlist
- If you provide a single video URL, only that video is downloaded
- No additional flags are required

---

## ❓ Can I download both video and audio?

Yes.

You can choose between:
- Video formats with audio (AV1, VP9, MP4)
- Audio-only formats (Opus, MP3, FLAC)

---

## ❓ Can I choose the video quality?

Yes.

UVD supports quality selection from:
- 360p
- 480p
- 720p
- 1080p
- 1440p
- 4K
- 8K

If the requested quality is not available, UVD automatically falls back to the closest available format.

---

## ❓ Does UVD download subtitles?

Yes.

Supported subtitle features:
- Manual subtitles
- Auto-generated subtitles
- Multiple languages
- Download **all available subtitles**
- Automatic conversion to **SRT**

Example:
```bash
uvd <URL> -f mp4 ./videos -subs all
```

---

## ❓ Does UVD bypass DRM?

No.  
UVD **does not bypass DRM-protected content**.

If a video is protected by DRM, it **cannot be downloaded** by UVD.

---

## ❓ Is this project legal?

UVD itself is **legal software**.

However:

- Users are responsible for how they use it
- Users must comply with copyright laws and website ToS
- The authors assume **no responsibility for misuse**

---

## ❓ Why use UVD instead of commercial downloaders?

UVD focuses on simplicity, transparency and local execution:
- No subscriptions or accounts
- No advertisements or tracking
- Fully local execution
- No artificial limits
- Open source and transparent by design
- Not intended for commercial purposes

---

## ❓ Can I contribute to UVD?

Yes!

You can:
- Report bugs
- Suggest new features

Simply open an **issue** on GitHub.

---

## ❓ Where are downloaded files saved?

Files are saved in the output directory you specify.

If no directory is provided, UVD uses the default directory you can found in your videos system folder:

```text
/UVD_downloads
```

---

## ❓ What happens if a format or quality is not available?

UVD uses **smart fallback logic**.

If a requested format or quality is not available, it automatically downloads:

- the closest available quality
- or the best compatible format

---

## 📌 Troubleshooting

If you encounter an issue:

1. Make sure you are using the latest version
2. Check the `--help` output
3. Verify that the source website supports the requested format
4. Open an issue if the problem persists
