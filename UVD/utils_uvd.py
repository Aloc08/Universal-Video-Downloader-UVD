# utils_udv.py

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
 *  utils_uvd.py:
 *  -
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
import shlex
import subprocess
from config_uvd import PROG_NAME, PROG_VER, YT_DLP_BIN, VIDEO_FORMATS, AUDIO_FORMATS, QUALITIES, DEFAULT_OUTPUT_DIR
from error_codes_uvd import ErrorCodes
from pathlib import Path
import platform

class Utils:
    
    @staticmethod
    def run_cmd(cmd) -> None:

        env = os.environ.copy()
        bin_dir = os.path.dirname(YT_DLP_BIN)
        env["PATH"] = bin_dir + os.pathsep + env.get("PATH", "")

        print("[" + PROG_NAME + "] Executing: ", " ".join(shlex.quote(c) for c in cmd))

        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"[{PROG_NAME}] Error {ErrorCodes.ERR_UNKNOWN}: Download failed.")
            sys.exit(ErrorCodes.ERR_UNKNOWN)

        subprocess.run(cmd, check=True, env=env)


    @staticmethod
    def mkdir(path: str) -> None:
        os.makedirs(path, exist_ok=True)
    
    # URL checker
    @staticmethod
    def url_check(video_url: str) -> bool:
        
        isValid = True
        
        try:
            subprocess.run(
                [YT_DLP_BIN, "--simulate", "--no-playlist", video_url],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True
            )
        except subprocess.CalledProcessError:
            print("[" + PROG_NAME + "] Error " + str(ErrorCodes.URL_NOT_VALID) + ": Unsupported or invalid URL.\n[" + PROG_NAME + "] Type .\\" + PROG_NAME + " --help for help.\n")
            isValid = False
        
        return isValid
    

    # Check if a format is supported and specifies if is audio or video
    @staticmethod
    def check_format(fmt: str) -> str:
        
        fmt = fmt.lower()

        if fmt in VIDEO_FORMATS:
            return "video"
        elif fmt in AUDIO_FORMATS:
            return "audio"
        else:
            return "invalid"
        

    # Check if a quality is supported and specifies
    @staticmethod
    def check_quality(q: str) -> bool:
        
        q = q.lower()

        if q in QUALITIES:
            return True
        return False
    

    # Create video directory in fs at default location of the videos folder
    @staticmethod
    def create_default_video_directory():
        
        # Which OS?
        system = platform.system()

        # Definisci la directory di default dei video in base al sistema operativo
        if system == 'Windows':
           
            video_dir = Path(os.environ['USERPROFILE']) / 'Videos'

        elif system == 'Darwin':  # macOS
            
            video_dir = Path(os.environ['HOME']) / 'Movies'

        elif system == 'Linux':
           
            video_dir = Path(os.environ['HOME']) / 'Videos'

        else:

            print(f"[{PROG_NAME}] [Fallback]: Folder {DEFAULT_OUTPUT_DIR}")
            video_dir = DEFAULT_OUTPUT_DIR

        # Create 'UVD_downloads' dir inside the video directory
        uv_downloads_dir = video_dir / 'UVD_downloads'
        Utils.mkdir(uv_downloads_dir)

        return uv_downloads_dir
