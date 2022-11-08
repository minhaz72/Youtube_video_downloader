# youtube video downloader: 
import sys 

from pytube  import YouTube 
def downloader(link):  # the link of the video : 
    yt= YouTube(link)
    video= yt.get('mp4', '720p')
    video.download('D:\python\project\youtube_Video_downloader')
if __name__== '__main__ ': 
    link =input('enter the video link: ')
    print(downloader(link))
    