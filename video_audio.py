from stringcolor import *
from pafy import get_playlist 

class Video :
    """
    This class based on pafy and youtube-dl
    this class is the main part of the project plyalist_OOP to download video
    """
    def video(self,path,playlist) :
        number = len(playlist["items"])
        cte = 0
        for video in range(len(playlist["items"])) :
            cte += 1
            down = playlist["items"][video]["pafy"].getbest()
            down.download(path)
            cte1  = str(video+1) + f" is downloaded: ---->({cte}/{number})"
            print(f"Video:{cs(cte1, 'orchid').bold()}")


class Audio :
    """
    This class based on pafy and youtube-dl
    this class is the main part of the project plyalist_OOP to download audio
    """
    def audio(self,path,playlist) :
        number = len(playlist["items"])
        cte = 0
        for video in range(len(playlist["items"])) :
            cte += 1
            down = playlist["items"][video]["pafy"].getbestaudio()
            down.download(path)
            cte1  = str(video+1)+f" is downloaded: ---->({cte}/{number})"
            print(f"Video:{cs(cte1, 'orchid').bold()}")

            
