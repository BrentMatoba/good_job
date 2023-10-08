import pygame
import random
from datetime import datetime
import time

pygame.init()
pygame.mixer.init()

def countDown():
    #counter variable is in seconds, currently set to 25 minutes, a standard pomodoro time.
    counter = 10
    while counter > 0:
        minutes, seconds = divmod(counter, 60)
        if minutes > 0:
            print(minutes, "minute(s),", seconds, "seconds")
        else:
            print(seconds, "seconds")
        #pauses once per second, technically imprecise because it doesn't account for computing time,
        #but its sufficient for now as a working protoype, I can change to a more precise counter
        #Once I have the program running.
        time.sleep(1)
        counter -=1
    print("Pomodoro Complete!")
    goodJobSound()

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

def writeLog(log, datetime, type, description):
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

def goodJobSound():
    good_job = pygame.mixer.Sound("ST_Fanfare_WinBattle.wav")
    good_job.play()
    pygame.time.wait(int(good_job.get_length() * 1000))

#Randomly prints inspirational quote
def printQuote():
    print(quotes[random.randint(0, len(quotes)-1)])
    print("You did it! Good job!")
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()

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

def logPomodoro():
    #log management
    with open('log.csv', 'a+') as log:
        #gathers data for log entry
        current_datetime = str(datetime.now())
        num = input("What type of pomodoro? (1/2/3/4?)\n1:School\n2:Odin\n3:Extracurricular programming\n4:School Programming\n")
        type = numToType(int(num))
        description = input("What did you do during the pomodoro? ")

        #Adds new line to log.csv
        writeLog(log, current_datetime, type, description)


    #print inspirational quote
    printQuote()
    #plays sound
    goodJobSound()


logPomodoro()
#countDown()

