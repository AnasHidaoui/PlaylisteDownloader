from stringcolor import *
import emoji
from os import system
from sys import exit
from platform import system as getos

class Welcome :
    """
    this class is the first port of the project "playlist_OOP"
    It coutain welcome methode
    """
    def welcome(self) :
        if getos().lower()[0] is not "w":
            system("clear")
        else:
            system("cls")
        wel = """

                     ,------.   ,-----. ,--.   ,--.,--.  ,--. 
                     |  .-.  \ '  .-.  '|  |   |  ||  ,'.|  | 
                     |  |  \  :|  | |  ||  |.'.|  ||  |' '  | 
                     |  '--'  /'  '-'  '|   ,'.   ||  | `   | 
                     `-------'  `-----' '--'   '--'`--'  `--' 
                        By : HIDAOUI ANAS / Augaust 5 2020 /
                         https://github.com/rootAnashidaoui
        """
        print(cs(wel, "purple4").bold())
    def goodby(self) :
        
        gb = """
                        ==================================
                        |  Tanks you for using TopTube   |
                        +--------------------------------+
                        |      By : HIDAOUI ANAS         |
                        |        versio: 3.0.4           |        
                        +--------------------------------+
                        | www.rootAnashidaoui@githab.com |
                        |       Augaust 5 2020           |
                        ==================================
        """
        print(cs(gb,"purple4").bold())
        
