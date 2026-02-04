# error_codes_uvd.py

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
 *  error_codes_uvd.py:
 *  List of error codes that the software could throw
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

from enum import IntEnum

class ErrorCodes(IntEnum):
    # Generic
    ERR_UNKNOWN = 9001
    INVALID_OS = 9002

    # Arguments
    MISSING_ARGUMENTS = 1001
    URL_NOT_VALID = 1002
    
    # Media
    MEDIA_NOT_AVAILABLE = 2001
    FORMAT_NOT_VALID = 2002
    QUALITY_NOT_VALID = 2003


  
