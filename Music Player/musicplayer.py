from random import randint

#path of music files
path_list =[
    r"/Users/ayush/Desktop/Code clause/song.mp3"
    r"/Users/ayush/Desktop/Code clause/song1.mp3"
    r"/Users/ayush/Desktop/Code clause/song2.mp3"
    r"/Users/ayush/Desktop/Code clause/song3.mp3"
]

import pygame
class Music:

    def play(self,path):
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
    
    def stop(self):
        pygame.mixer.music.stop()
    
    def __init__(self):
        print("Simple Music Player")
    
        while True:
            choice = input("\t1. Play\n\t2. Stop\n\t3. Change Song\nEnter (1-3) >>>> : ")
    
            if choice == "1":
                path = path_list[randint(0,len(path_list)-1)]
                self.play(path)
            elif choice == "2":
                self.stop()
            elif choice == "3":
                self.stop()
                path = path_list[randint(0,len(path_list)-1)]
                self.play(path)
            else:
                print("Invalid choice. Please try again.")
                break
Music()
