# main_uvd.py

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 *  ▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
 *                                                                      
 *  Universal Video Downloader (UVD)                                                
 *  Download Videos in High Quality                                 
 *                                                                  
 *  Version:         7.0.0                                                    
 *  Data:            2026/02/01                                               
 *  Author:          Alessio Occulto (Aloc08)                                         
 *  
 * ----------------------------------------------------------------------------
 *  DESCRIPTION:
 *  This software can download online multimedia in high quality 
 *  through its URL and from the major websites. 
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

from cli_uvd import get_cli_args
from utils_uvd import Utils
from config_uvd import PROG_NAME, HELP_MESSAGE
import sys
from error_codes_uvd import ErrorCodes
from downloader_uvd import Downloader
import subprocess

def main():
    # Checking for arguments
    if len(sys.argv) == 1:
        print("[" + PROG_NAME + "] Error " + str(ErrorCodes.MISSING_ARGUMENTS) + ": Missing or bad arguments.\n["+ PROG_NAME + "] " + HELP_MESSAGE + "\n");
        sys.exit(1)
    else: # If there are arguments, create the parser and the args
        args = get_cli_args()
        want_media = args.format != "none"
        want_subs  = args.subs != "none"



    # URL check
    isValid = Utils.url_check(args.url)

    # If URL is not valid, exit
    if isValid == False:
        sys.exit(2)


    # Summary

    print("\n-------   SUMMARY   -------\n")

    print(f"URL: {args.url}")
    print(f"Format: {args.format}")
    print(f"Quality: {args.quality}")
    print(f"Download directory: {args.directory}")
    print(f"Subtitles: {args.subs}")

    print("\n---------------------------\n")


    error = False

    # If neither format or subs are selected
    if args.format == "none" and args.subs == "none":
        print("[" + PROG_NAME + "] Error " + str(ErrorCodes.MISSING_ARGUMENTS) + ": Select a video format (and quality).\n[" + PROG_NAME + "] " + HELP_MESSAGE + "\n");
        sys.exit(1)

    if want_media:
        # Download video or audio
        if args.format != "none" or args.quality != "none":
            try:
                Downloader.download_video_or_audio(args.url, args.format, args.quality, args.directory)
            except subprocess.CalledProcessError as e:
                print("\n[" + PROG_NAME + "] Error " + str(ErrorCodes.MEDIA_NOT_AVAIABLE) + ": Media is not not available or a generic error occurred while downloading: ",e)
                error = True

    if want_subs:
        # Download subtitles
        if args.subs != "none":
            try:
                Downloader.download_subtitles(args.url, args.subs, args.directory)
            except subprocess.CalledProcessError as e:
                print("\n[" + PROG_NAME + "] Error " + str(ErrorCodes.MEDIA_NOT_AVAIABLE) + ": Subtitles are not available or a generic error occurred while downloading: ",e)
                error = True


    if error == False:
        print("\n[" + PROG_NAME + "] Done! Check: " + str(args.directory))


    sys.exit(0)


if __name__ == "__main__":
    main()