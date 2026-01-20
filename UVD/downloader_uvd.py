# downloader_uvd.py

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 *  ▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
 *                                                                      
 *  Universal Video Downloader (UVD)                                                
 *  Download Videos in High Quality                                 
 *                                                                  
 *  Version:         6.0.0                                                    
 *  Data:            2026/01/20                                               
 *  Author:          Alessio Occulto (Aloc08)                                         
 *  
 * ----------------------------------------------------------------------------
 *  DESCRIPTION:
 *  This software can download online multimedia in high quality 
 *  through its URL and from the major websites. 
 *
 * ----------------------------------------------------------------------------
 *  downloader_uvd.py:
 *  Occupies of downloading multimedia file from the internet
 *
 * ----------------------------------------------------------------------------
 *  SOFTWARE:
 *  - Language:       Python
 *  - APIs / Libs:    yt-dlp, FFMpeg, argparse
 *
 * ----------------------------------------------------------------------------
 *  CREDITS:
 *  Alessio Occulto
 *  Filippo Occulto
 *  2026. Licensed Under MIT License.
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
from utils_uvd import Utils
from config_uvd import BASE_TEMPLATE, YT_DLP_BIN
from config_uvd import PROG_NAME
from error_codes_uvd import ErrorCodes

class Downloader:

    @staticmethod
    def download_video_or_audio(url: str, fmt: str, quality: str, dir: str):
        
        Utils.mkdir(dir)

        fmt = fmt.lower()
        quality = quality.lower()
        format_type = Utils.check_format(fmt)
        quality_is_ok = Utils.check_quality(quality)

        if fmt != "none":
            out_tmpl = os.path.join(dir, f"{BASE_TEMPLATE}.{fmt.lower()}.%(ext)s")
        else:
            out_tmpl = os.path.join(dir, f"{BASE_TEMPLATE}.%(ext)s")


        if format_type == "invalid":
            print("[" + PROG_NAME + "] Error " + str(ErrorCodes.FORMAT_NOT_VALID) + ": Format not valid.\n[" + PROG_NAME + "] Type .\\" + PROG_NAME + " --help for help.\n");
            sys.exit(ErrorCodes.FORMAT_NOT_VALID)

        if quality_is_ok == False:
            print("[" + PROG_NAME + "] Error " + str(ErrorCodes.QUALITY_NOT_VALID) + ": Quality not valid.\n[" + PROG_NAME + "] Type .\\" + PROG_NAME + " --help for help.\n");
            sys.exit(ErrorCodes.QUALITY_NOT_VALID)

        if format_type == "video":

            match quality:
                case "360p":    qfilter = "[height<=360]"
                case "480p":    qfilter = "[height<=480]"
                case "720p":    qfilter = "[height<=720]"
                case "1080p":   qfilter = "[height<=1080]"
                case "1440p":   qfilter = "[height<=1440]"
                case "4k":      qfilter = "[height<=2160]"
                case "8k":      qfilter = "[height<=4320]"
                case _:         qfilter = ""

            match fmt:
                case "av1":

                    video_format = f"bestvideo[vcodec*=av01]{qfilter}+bestaudio/bestvideo+bestaudio/best"

                    print("\n------- Downloading AV1 video file format (max quality if exists, either fallback) -------")

                case "vp9":

                    video_format = f"bestvideo[vcodec*=vp9]{qfilter}+bestaudio/bestvideo+bestaudio/best"
                    
                    print("\n------- Downloading VP9 video file format (max quality if exists, either fallback) -------")

                case "mp4":

                    video_format = f"bestvideo[vcodec^=avc1]{qfilter}+bestaudio[ext=m4a]/best[ext=mp4]/best"

                    print("\n------- Downloading H.264 (mp4) video file format -------\n")
            
            cmd = [
                    YT_DLP_BIN,
                    "--yes-playlist",
                    "-f", video_format,
                    "--merge-output-format", "mkv",  
                    "-o", out_tmpl,
                    url,
            ]

        elif format_type == "audio":
            cmd = [
                YT_DLP_BIN,
                "--yes-playlist",
                "-f", "bestaudio",
                "-x",
                "--audio-format", fmt,
                "-o", out_tmpl,
                url,
            ]
            print("\n------- Downloading " + fmt.lower() + format_type + " -------\n")
        
        else:
            print(f"[{PROG_NAME}] Error {ErrorCodes.FORMAT_NOT_VALID}: Unknown format type.")
            sys.exit(ErrorCodes.FORMAT_NOT_VALID)

        Utils.run_cmd(cmd)

    @staticmethod
    def download_subtitles(url: str, lang: str, dir: str):

        Utils.mkdir(dir)

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

        print(f"\n------- Downloading subtitles ({lang}) -------")

        Utils.run_cmd(cmd)


