import pygame
import random
import csv
from datetime import datetime

pygame.init()
pygame.mixer.init()


def numToType(number):
    if number == 1:
        return "school"
    elif number == 2:
        return "odin"
    elif number == 3:
        return "extracurricular programming"
    elif number == 4:
        return "school programming"
    elif number == 0:
        return "testing"

def writeLog(datetime, type, description):
    log.write(datetime)
    log.write(", ")
    log.write(type)
    log.write(", ")
    log.write(description)
    log.write("\n")
    print()
    print()
    print()
    print()

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
#make calculating point types function
#make numbers for input, 1 = school, 2 = extracurricular etc, shoudl reduce capacity for user input error
#make desktop shortcut to good_job
#Wind rustling sound after good_job sound
#Write function that can search csv file and delete testing rows




#log management
with open('log.csv', 'a+') as log:
    #gathers data for log entry
    datetime = str(datetime.now())
    num = input("What type of pomodoro? (1/2/3?)\n1:School\n2:Odin\n3:Extracurricular programming\n4:School Programming\n")
    type = numToType(int(num))
    description = input("What did you do during the pomodoro? ")

    #Adds new line to log.csv
    writeLog(datetime, type, description)







#Stores quotes
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

#Randomly prints inspirational quote
print(quotes[random.randint(0, len(quotes)-1)])
print("You did it! Good job!")
print()
print()
print()
print()
print()


#plays sound
good_job = pygame.mixer.Sound("ST_Fanfare_WinBattle.wav")
good_job.play()
pygame.time.wait(int(good_job.get_length() * 1000))





