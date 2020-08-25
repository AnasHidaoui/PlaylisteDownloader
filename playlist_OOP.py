from welcome import Welcome   # import the welcome methond
from stringcolor import *     # iport the stringcolor
from pafy import get_playlist # import pafy (pafy is based on youtube-dl)
from video_audio import Video,Audio # import Video and Audio from video_audio
class Download_playlist :
    """
    class about downloading from YouTube :
    1-Downloading playlist
    2-you can downloading video or audio
    This class is based on modul pafy and modul youtube-dl
    """
    def __init__(self) : # The vonstractor
        wel = Welcome.welcome(self)    # Activation the welcomr methode from modul welcome
        self.get_url()                 # Activation the methon get_url
        self.choces()                  # chose betwwene video or audio
        self.path()                    # grt the path here                   
        self.start()                  # start download
        Welcome.goodby(self)          # goodby to user
        

    def get_url(self) :   # get thre URL or ID from user
        while True :
            playlist_URL = input(cs("Enter the video ID or URL:", "#FFFF00").bold())
            
            try :
                print(cs("Please waite.....", "#FFFF00").bold())
                self.playlist = get_playlist(playlist_URL)
            except ValueError :
                print(cs("ValueError: Unrecognized playlist url!!!", "DeepPink3"))
            except TypeError :
                print(cs("TypeError: get_playlist() missing 1 required positional argument: 'playlist_url'", "DeepPink3"))
            except :
                print(cs("Ooops someting is wronge....try againe", "DeepPink3"))
            else :
                author = self.playlist["author"]
                title  = self.playlist["title"]
                number = len(self.playlist["items"])
                print(f"Playlist       :{cs(title, 'orchid').bold()}")
                print(f"Playlist_Author:{cs(author, 'orchid').bold()}")
                print(f"{cs(number, 'orchid').bold()} Videos")
                break
    def path(self) :   # get the path 
        while True :
            path = input(cs("Save as :", "#FFFF00").bold())
            try :
                self.path = str(path)
            except :
                print(cs("Ooops someting is wronge....try againe", "DeepPink3"))
            else :
                print("                                                ") 
                break
    def choces(self) :   # in this port thr user chose video or audio
        while True :
            chose = input(cs("[video/audio] :", "#FFFF00").bold())
            try :
                self.chose = str(chose)
                assert chose == "video" or chose == "audio"
            except AssertionError :
                print(cs("Please chose between audio/video....try againe", "DeepPink3"))
            except :
                print(cs("Ooops someting is wronge....try againe", "DeepPink3"))
            else :
                break
    def start(self) : 
        if self.chose == "video" :
            Video.video(self,self.path,self.playlist)   # start download video
        if self.chose == "audio" :
            Audio.audio(self,self.path,self.playlist)  # start download audio


# Run the all progecte

download = Download_playlist()