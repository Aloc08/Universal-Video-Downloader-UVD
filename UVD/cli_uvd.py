# cli_uvd.py

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
 *  cli_uvd.py:
 *  Manages CLI arguments and parsing
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

import argparse
from config_uvd import PROG_NAME, PROG_VER
from utils_uvd import Utils


def get_cli_args() -> argparse.Namespace:

    parser = argparse.ArgumentParser(
        prog=PROG_NAME,
        description=f"{PROG_NAME} is a lightweight command-line multimedia downloader built on top of yt-dlp.",
        epilog=f"[{PROG_NAME}] Version {PROG_VER}. 2026.",
        formatter_class=argparse.RawTextHelpFormatter
    )


    # URL (positional and mandatory)
    parser.add_argument(
        "url", 
        help="Multimedia URL to download"
    )


    # Format flag
    parser.add_argument(
        "-f", "--format",
        default="none",
        choices=["av1", "vp9", "mp4", "opus", "mp3", "flac"],
        help="Format to download [av1, vp9, mp4, opus, mp3, flac | default: none]"
    )


    # Quality flag
    parser.add_argument(
        "-q", "--quality",
        default="best",
        choices=["360p", "480p", "720p", "1080p", "1440p", "4k", "8k"],
        help="Quality to download [360p, 480p, 720p, 1080p, 1440p, 4k, 8k | default: best]"
    )


    # Download directory flag
    parser.add_argument(
        "-dir", "--directory",
        default=Utils.create_default_video_directory(),
        help="Directory where the file will be saved (default: pc videos dir)"
    )

    # Subtitles flag
    parser.add_argument(
        "-s", "--subs",
        nargs="?",
        default="none",
        help="Subtitles languages to download (comma separated, e.g. en,it,en-US or 'all')"
    )

    # Version
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"[{PROG_NAME}] {PROG_VER}"
    )

    args = parser.parse_args()

    return args
