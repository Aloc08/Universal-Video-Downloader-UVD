# config_uvd.py

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 *  ▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
 *                                                                      
 *  Universal Video Downloader (UVD)                                                
 *  Download Videos in High Quality                                 
 *                                                                  
 *  Version:         6.1.0                                                    
 *  Data:            2026/01/24                                               
 *  Author:          Alessio Occulto (Aloc08)                                         
 *  
 * ----------------------------------------------------------------------------
 *  DESCRIPTION:
 *  This software can download online multimedia in high quality 
 *  through its URL and from the major websites. 
 *
 * ----------------------------------------------------------------------------
 *  config_uvd.py:
 *  Stores some standard configurations and definitions
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


import sys
import os
import platform
from error_codes_uvd import ErrorCodes

def resource_path(relative_path: str) -> str:
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

SYSTEM = platform.system().lower()

if SYSTEM == "windows":
    BIN_DIR = "bin/windows"
    EXT = ".exe"
elif SYSTEM == "linux":
    BIN_DIR = "bin/linux"
    EXT = ""
elif SYSTEM == "darwin":
    BIN_DIR = "bin/mac"
    EXT = ""
else:
    raise RuntimeError(f"[{PROG_NAME}] Error {ErrorCodes.INVALID_OS}: O.S. not supported: {SYSTEM}")


YT_DLP_BIN   = resource_path(f"{BIN_DIR}/yt-dlp{EXT}")
FFMPEG_BIN  = resource_path(f"{BIN_DIR}/ffmpeg{EXT}")
FFPROBE_BIN = resource_path(f"{BIN_DIR}/ffprobe{EXT}")
FFPLAY_BIN  = resource_path(f"{BIN_DIR}/ffplay{EXT}")

PROG_NAME = "UVD"
PROG_VER = "6.0.0"

DEFAULT_OUTPUT_DIR = "./downloaded_videos"
UVD_FOLDER_NAME = "UVD"

BASE_TEMPLATE = "%(title)s_%(id)s"

COMMON_ARGS = [
    "--yes-playlist"
]

VIDEO_FORMATS = ["av1", "vp9", "mp4"]
AUDIO_FORMATS = ["opus", "mp3", "flac"]
QUALITIES = ["360p", "480p", "720p", "1080p", "1440p", "4k", "8k", "best"]





