#!/usr/bin/env python
import youtube_dl
def main():
    print("[PH] Pornhub Simple Downloader | github.com/im-bb") #XD
    print("[!] Auto Loop Script, Use Control + C to Stop")
    directory = input("[*] Folder Directory for Saving : ")
    while True:
        url = input("[*] Pornhub Videos Url : ")
        dire = directory+'/handpicked/%(title)s.%(ext)s'
        ydl_opts = {
            'format': 'best',
            'outtmpl': dire,
            'nooverwrites': True,
            'no_warnings': False,
            'ignoreerrors': True,
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])


if __name__ == '__main__':
    main()
