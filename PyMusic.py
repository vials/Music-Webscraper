import time, sys, os, shutil
import subprocess as sp
from pytube import YouTube
import moviepy.editor as mp
from colorama import init
from colorama import Fore, Back, Style
init()

def main():
    cls()
    print(Fore.WHITE+'*'*37)
    print('+  '+Fore.CYAN+'Interval.inc\'s Music Downloader'+Fore.WHITE+'  +')
    print('*'*37)
    print('*[1.] YouTube                       *')
    print('*[2.] SoundCloud                    *')
    print('*[0.] Exit                          *')
    print('*'*37)
    print('+   '+Fore.YELLOW+'Sub>www.YouTube.com/CallMeCOM'+Fore.WHITE+'   +')
    print('*'*37)

    menu = True

    choice = raw_input(Fore.RED+'Please Select Your Choice: '+Fore.GREEN)

    if choice == '1':
        YouTubeDownload()
        menu = False
    elif choice == '2':
        #SoundCloudDownload()
        #menu = False
        print('Not Implemented Yet...')
    elif choice == '0':
        Exit()
        menu = False
    elif choice == '' or choice >= 2:
        print('Please Only Select Choices <0-2>')

def Exit():
        cls()
        print('Script Is Shutting Down In 3 Seconds')
        time.sleep(3)
        sys.exit("Thanks For Using My Script!\n~Inc")

def cls():
        sp.call('cls', shell=True)

def YouTubeDownload():
    cls()
    print(Fore.WHITE+'*'*37)
    print('+  '+Fore.CYAN+'Interval.inc\'s Music Downloader'+Fore.WHITE+'  +')
    print('*'*37)

    YouTubeURL = raw_input(Fore.RED+'Enter YouTube URL To Download: '+Fore.GREEN)

    yt = YouTube(str(YouTubeURL))
    print(Fore.YELLOW+yt.title)

    YTDownload = True
    
    while YTDownload:
            YTCheck = raw_input(Fore.RED+'Is This The Correct Video? (Y/N): '+Fore.GREEN)
            if YTCheck == 'Y' or YTCheck == 'y':
                print(Fore.YELLOW+'Proceeding To Download...')
                '''stream = yt.streams.filter(only_audio=True).first()
                stream.download()
                shutil.move(yt.title+'.mp4', './Downloads/'+yt.title+'.mp3')
                '''
                stream = yt.streams.filter(file_extension='mp4').first()
                stream.download()
                print('Download Is Complete!')
                Changed = yt.title.replace('.', '').replace('\'', '')
                clip = mp.VideoFileClip(Changed+'.mp4')
                clip.audio.write_audiofile('./Downloads/'+Changed+'.mp3')
                tryAgain = raw_input(Fore.RED+'Would You Like To Download Another? (Y/N): '+Fore.GREEN)

                if tryAgain == 'Y' or tryAgain == 'y':
                    main()
                    YTDownload = False
                elif tryAgain == 'N' or tryAgain == 'n':
                    Exit()
                elif tryAgain == '':
                    print(Fore.WHITE+'Please Only Type (Y/N)!')
                    
            elif YTCheck == 'N' or YTCheck == 'n':
                print(Fore.WHITE+'Please Enter The Correct URL!')
                time.sleep(3)
                YouTubeDownload()
                YTDownload = False
            elif YTCheck == '':
                print(Fore.WHITE+'Please Enter A Proper URL')
                time.sleep(3)
                YouTubeDownload()
                YTDownload = False
    

if __name__ == '__main__':
    main()
