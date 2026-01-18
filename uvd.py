"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 *  ▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
 *                                                                      
 *  Universal Video Downloader (UVD)                                                
 *  Download Videos in High Quality                                 
 *                                                                  
 *  Version:         5.0.0                                                    
 *  Data:            2026/01/17                                                
 *  Author:          Alessio Occulto (Aloc08), Filippo Occulto (FOcculto)                                           
 *  
 * ----------------------------------------------------------------------------
 *  DESCRIPTION:
 *  This script downloads a video online or audio in high quality 
 *  through its URL of the major websites. 
 *
 * ----------------------------------------------------------------------------
 *  SOFTWARE:
 *  - Language:       Python
 *  - APIs / Libs:    yt-dlp, FFMpeg
 *
 * ----------------------------------------------------------------------------
 *  CREDITS:
 *  Alessio Occulto
 *  Filippo Occulto
 *  2026. Licensed under Mit License.
 *  ______________________________________
 *  Contacts: 
 *    -E-Mail: alessio.occulto.dev@gmail.com
 *
 * ----------------------------------------------------------------------------
 *  NOTES:
 *  - Tested on: Windows and Linux
 *  - Any modification to the code could render the program unoperable 
 *
 *  ▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


import os
import sys
import subprocess
import shlex

DEFAULT_OUTPUT_DIR = "./downloaded_videos"
BASE_TEMPLATE = "%(title)s_%(id)s"
YT_DLP_BIN = "yt-dlp"
PROG_VER = "5.0.0"
PROG_NAME = "UVD"


def run_cmd(cmd) -> None:
    print("Exec:", " ".join(shlex.quote(c) for c in cmd))
    subprocess.run(cmd, check=True)


def mkdir(DIR: str) -> None:
    os.makedirs(DIR, exist_ok=True)


"""AV1 max quality."""
def down_av1(url: str, dir: str) -> None:
    
    mkdir(dir)
    out_tmpl = os.path.join(dir, BASE_TEMPLATE + ".av1.%(ext)s")

    cmd = [
        YT_DLP_BIN,
        "--yes-playlist",
        "-f", "bestvideo[vcodec*=av01]+bestaudio/bestvideo+bestaudio/best",
        "--merge-output-format", "mkv",  
        "-o", out_tmpl,
        url,
    ]

    print("\n=== Downloading AV1 video file format (max quality if exists) ===")
    run_cmd(cmd)

"""VP9"""
def down_vp9(url: str, dir: str) -> None:
    
    mkdir(dir)
    out_tmpl = os.path.join(dir, BASE_TEMPLATE + ".vp9.%(ext)s")

    cmd = [
        YT_DLP_BIN,
        "--yes-playlist",
        "-f", "bestvideo[vcodec*=vp9]+bestaudio/bestvideo+bestaudio/best",
        "--merge-output-format", "mkv", 
        "-o", out_tmpl,
        url,
    ]

    print("\n=== Downloading VP9 video file format (fallback AV1) ===")
    run_cmd(cmd)


"""H.264(MP4)."""
def down_h264(url: str, dir: str) -> None:
    
    mkdir(dir)

    out_tmpl = os.path.join(dir, BASE_TEMPLATE + ".h264.%(ext)s")

    cmd = [
        YT_DLP_BIN,
        
        "--yes-playlist",
        "-f", "bestvideo[vcodec^=avc1]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "--merge-output-format", "mp4",
        "-o", out_tmpl,
        url,
    ]

    print("\n=== Downloading H.264 (MPEG4) video file format ===\n")
    run_cmd(cmd)


def down_audio_opus(url: str, dir: str) -> None:

    mkdir(dir)

    out_tmpl = os.path.join(dir, BASE_TEMPLATE + ".audio.opus.%(ext)s")
    cmd = [
        YT_DLP_BIN,
        "--yes-playlist",
        "-f", "bestaudio",
        "-x",
        "--audio-format", "opus",
        "-o", out_tmpl,
        url,
    ]
    print("\n=== Downloading Opus Audio Track ===\n")
    run_cmd(cmd)

def down_mp3(url: str, dir: str):

    mkdir(dir)
    out_tmpl = os.path.join(dir, BASE_TEMPLATE + ".mp3")

    cmd = [
        YT_DLP_BIN,
        "--yes-playlist",
        "-f", "bestaudio",              
        "--extract-audio",            
        "--audio-format", "mp3",      
        "--audio-quality", "0",       
        "-o", out_tmpl,
        url,
    ]

    print("\n=== Downloading MP3 Audio Track ===")
    run_cmd(cmd)


def down_flac(url: str, dir: str):

    mkdir(dir)
    out_tmpl = os.path.join(dir, BASE_TEMPLATE + ".flac")

    cmd = [
        YT_DLP_BIN,
        "--yes-playlist",
        "-f", "bestaudio",            
        "--extract-audio",            
        "--audio-format", "flac",   
        "--audio-quality", "0",      
        "-o", out_tmpl,
        url,
    ]

    print("\n=== Downloading FLAC Audio Track ===")
    run_cmd(cmd)


def down_quality(url: str, dir: str, quality: str):

    mkdir(dir)
    out_tmpl = os.path.join(dir, BASE_TEMPLATE + ".av1.%(ext)s")

    match quality:
        case "-360p": qfilter = "[height<=360]"
        case "-480p": qfilter = "[height<=480]"
        case "-720p": qfilter = "[height<=720]"
        case "-1080p": qfilter = "[height<=1080]"
        case "-1440p": qfilter = "[height<=1440]"
        case "-4k":   qfilter = "[height<=2160]"
        case "-8k":   qfilter = "[height<=4320]"
        case _:       qfilter = ""

    fmt = f"bestvideo[vcodec*=av01]{qfilter}+bestaudio/best"

    cmd = [
        YT_DLP_BIN,
        "-f", fmt,
        "--yes-playlist",
        "--merge-output-format", "mkv",
        "--js-runtime", "node",
        "--hls-prefer-ffmpeg",
        "-o", out_tmpl,
        url,
    ]

    print(f"\n=== Downloading AV1 with ({quality}) quality and fallback ===")
    run_cmd(cmd)


def down_subtitles(url: str, dir: str, lang: str = "en,it"):

    mkdir(dir)

    cmd = [
        YT_DLP_BIN,
        "--yes-playlist",
        "--skip-download",
        "--write-sub",
        "--write-auto-sub",
        "--convert-subs", "srt",
        "-o", os.path.join(dir, BASE_TEMPLATE + ".%(ext)s"),
        url,
    ]

    if lang == "all":
        cmd.append("--all-subs")
    else:
        cmd.extend(["--sub-langs", lang])

    print(f"\n=== Downloading subtitles ({lang}) ===")
    run_cmd(cmd)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[" + PROG_NAME + "] Error: Missing or bad arguments.\n["+ PROG_NAME + "] Type py "+ PROG_NAME + ".py --help for help.\n");
        sys.exit(1)

    if(sys.argv[1] == "--help" or sys.argv[1] == "-h"):
        print("\n[" + PROG_NAME + "] Use: py " + PROG_NAME + ".py <YOUTUBE_URL> <FORMAT/QUALITY> <DOWNLOAD_DIRECTORY>  | -subs <SUBTITLES_LANGUAGES>")
        print("formats with best quality: -av1 -vp9 -mp4 -opus -mp3 -flac")
        print("qualities: -360p -480p -720p -1080p -1440p -4k -8k -none")
        print("subtitles: -subs [example: -none -subs en,en-US,it]. Use key-word all as language to download all subtitles avaiable.")
        print("Note: To use default directory write none if you download subs either put empty space (./downloaded_videos)")
        print("--lang-codes for language codes")
        print("--help for help (this page).\n\n")
        print("\nVersion: " + PROG_VER)
        print(PROG_NAME + ". All rights reserved")
        sys.exit(2)
    if(sys.argv[1] == "--version" or sys.argv[1] == "-v"):
        print("[" + PROG_NAME + "]" + " " + PROG_VER)
        sys.exit(3)
    if(sys.argv[1] == "--lang-codes"):
        print("[" + PROG_NAME + "] Languages Codes:\n\n")
        print("en, ab-en, aa-en, af-en, ak-en, sq-en, am-en, ar-en, hy-en, as-en, ay-en, az-en, bn-en, ba-en, eu-en, be-en, bho-en, bs-en, br-en, bg-en, my-en, ca-en, ceb-en, zh-Hans-en, zh-Hant-en, co-en, hr-en, cs-en, da-en, dv-en, nl-en, dz-en, en-en, eo-en, et-en, ee-en, fo-en, fj-en, fil-en, fi-en, fr-en, gaa-en, gl-en, lg-en, ka-en, de-en, el-en, gn-en, gu-en, ht-en, ha-en, haw-en, iw-en, hi-en, hmn-en, hu-en, is-en, ig-en, id-en, iu-en, ga-en, it-en, ja-en, jv-en, kl-en, kn-en, kk-en, kha-en, km-en, rw-en, ko-en, kri-en, ku-en, ky-en, lo-en, la-en, lv-en, ln-en, lt-en, lua-en, luo-en, lb-en, mk-en, mg-en, ms-en, ml-en, mt-en, gv-en, mi-en, mr-en, mn-en, mfe-en, ne-en, new-en, nso-en, no-en, ny-en, oc-en, or-en, om-en, os-en, pam-en, ps-en, fa-en, pl-en, pt-en, pt-PT-en, pa-en, qu-en, ro-en, rn-en, ru-en, sm-en, sg-en, sa-en, gd-en, sr-en, crs-en, sn-en, sd-en, si-en, sk-en, sl-en, so-en, st-en, es-en, su-en, sw-en, ss-en, sv-en, tg-en, ta-en, tt-en, te-en, th-en, bo-en, ti-en, to-en, ts-en, tn-en, tum-en, tr-en, tk-en, uk-en, ur-en, ug-en, uz-en, ve-en, vi-en, war-en, cy-en, fy-en, wo-en, xh-en, yi-en, yo-en, zu-en, ab, aa, af, ak, sq, am, ar, hy, as, ay, az, bn, ba, eu, be, bho, bs, br, bg, my, ca, ceb, zh-Hans, zh-Hant, co, hr, cs, da, dv, nl, dz, eo, et, ee, fo, fj, fil, fi, fr, gaa, gl, lg, ka, de, el, gn, gu, ht, ha, haw, iw, hi, hmn, hu, is, ig, id, iu, ga, it, ja, jv, kl, kn, kk, kha, km, rw, ko-orig, ko, kri, ku, ky, lo, la, lv, ln, lt, lua, luo, lb, mk, mg, ms, ml, mt, gv, mi, mr, mn, mfe, ne, new, nso, no, ny, oc, or, om, os, pam, ps, fa, pl, pt, pt-PT, pa, qu, ro, rn, ru, sm, sg, sa, gd, sr, crs, sn, sd, si, sk, sl, so, st, es, su, sw, ss, sv, tg, ta, tt, te, th, bo, ti, to, ts, tn, tum, tr, tk, uk, ur, ug, uz, ve, vi, war, cy, fy, wo, xh, yi, yo, zu    ")
        sys.exit(3)

    video_url = sys.argv[1]

    if len(sys.argv) > 2:
        fmt = sys.argv[2]

    if len(sys.argv) > 3:
        directory = sys.argv[3]
        if(directory == "none"): directory = DEFAULT_OUTPUT_DIR
    else:
        directory = DEFAULT_OUTPUT_DIR

    # URL Check
    try:
        subprocess.run(
        [YT_DLP_BIN, "--simulate", "--no-playlist", video_url],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True
            )
    except subprocess.CalledProcessError:
        print("[" + PROG_NAME + "] Error: Unsupported or invalid URL.\n[" + PROG_NAME + "] Type py " + PROG_NAME + ".py --help for help.\n")
        sys.exit(1)

    
    error = 0

    # Format Check
    match fmt:

        case "-av1":    # AV1
            try:
                down_av1(video_url, directory)
            except subprocess.CalledProcessError as e:
                error = 1
                print("\n[" + PROG_NAME + "] AV1 not avaiable or an error occured while attempting to download the video file:", e)

        case "-vp9":    # VP9
            try:
                down_vp9(video_url, directory)
            except subprocess.CalledProcessError as e:
                error = 1
                print("\n[" + PROG_NAME + "] VP9 not avaiable or an error occured while attempting to download the video file:", e)

        case "-mp4":    # H.264 (MP4)
            try:
                down_h264(video_url, directory)
            except subprocess.CalledProcessError as e:
                error = 1
                print("\n[" + PROG_NAME + "] H.264 not avaiable or an error occured while attempting to download the video file:", e)
    
        case "-opus":   # OPUS
            try:
                down_audio_opus(video_url, directory)
            except subprocess.CalledProcessError as e:
                print("\n[" + PROG_NAME + "] Opus not avaiable or an error occured while attempting to download the audio file:", e)

        case "-mp3":    # MP3
            try:
                down_mp3(video_url, directory)
            except subprocess.CalledProcessError as e:
                print("\n[" + PROG_NAME + "] MP3 not avaiable or an error occured while attempting to download the audio file:", e)

        case "-flac":   # FLAC
            try:
                down_flac(video_url, directory)
            except subprocess.CalledProcessError as e:
                print("\n[" + PROG_NAME +"] Flac not avaiable or an error occured while attempting to download the audio file:", e)

        case "-360p" | "-480p" | "-720p" | "-1080p" | "-1440p" | "-4k" | "-8k":
            try:
                down_quality(video_url, directory, fmt)
            except subprocess.CalledProcessError as e:
                print("\n[" + PROG_NAME + "] An error occured while attempting to download the video file:", e)

        case _:
            print("[" + PROG_NAME + "] Warning: Select a video format or quality.\n[" + PROG_NAME + "] Type py " + PROG_NAME + ".py --help for help.\n");
            

    if len(sys.argv) > 5:
        subs = sys.argv[5]

        try:
            down_subtitles(video_url, directory, subs)
        except subprocess.CalledProcessError as e:
            print("\n[" + PROG_NAME + "] Subtitles are not available or an error occurred while downloading:",e)

    if(error == 0): 
        print("\n[" + PROG_NAME + "] Done. Check your folder:", os.path.abspath(directory))


