import pygame
import random
import csv
from datetime import datetime

pygame.init()
pygame.mixer.init()

#things to do
#reduce volume
#improve sound loop code
#game window
#load star
#make text boxes in window
#Change font/size
#One textbox optional, can user prompt to say what they did
#is this fun or sad lmfao
#I have a supportive network I swear
#little animation maybve? star comes in on a swirly pattern?
#Can make an in-app pomodoro. Create a timer somewhere that update each second. When it goes to zero have the rest of program automatically run.
#Make desktop shortcut
#Make pomodoro counter that persists between program runs by writing to file. Pseudo written
#write main function
#PyQT module is used to make gui with Python
#make desktop shortcut to good_job
#Wind rustling sound after good_job sound


start = True
good_job = pygame.mixer.Sound("ST_Fanfare_WinBattle.wav")

#persisting counter pseudo
#read file, put stored number into variable
#increase variable by one
#write variable back to file
#print #pomodoros completed

with open('log.csv', 'a+') as log:



    datetime = str(datetime.now())
    type = input("What type of pomodoro? Odin? School? Extracurricular? Misc? ")
    description = input("What did you do during the pomodoro? ")

    description = description.lower()
    log.write(datetime)
    log.write(", ")
    log.write(type)
    log.write(", ")
    log.write(description)
    log.write("\n")










quotes = ["The pain you feel today is the strength you feel tomorrow. For every challenge encountered there is an opportunity for growth",
          "It's hard to beat a person who never gives up. Our greatest glory is not in never failing, but in rising every time we fail.",
          "With or without you, there will be champions. You want your name there? Work hard. -Khabib Nurmagomedov",
          "You either experience the pain of discipline or the pain of regret. The choice is yours.” —Unknown",
          "People who wonder if the glass is half empty or full miss the point. The glass is refillable. —Unknown",
          "We are what we repeatedly do. Excellence, then, is not an act, but a habit. ―Aristotle",
          "If you hear a voice within you say, ‘You cannot paint,’ then by all means paint, and that voice will be silenced. ―Vincent Van Gogh",
          "“The hard days are what make you stronger.” ―Aly Raisman",
          "“Opportunity is missed by most people because it is dressed in overalls and looks like work.”"
          ]


print(quotes[random.randint(0, len(quotes)-1)])
print("\n")
print("You did it! Good job!")


#How to improve sound code
#https://stackoverflow.com/questions/17657103/how-to-play-wav-file-in-python

while start == True:
    good_job.play(0, 0, 0)
    input("")
    start = False






