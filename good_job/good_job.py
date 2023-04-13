import pygame
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
#Make desktop shortcut
#Add inspirational quote dictionary

import random
start = True
good_job = pygame.mixer.Sound("ST_Fanfare_WinBattle.wav")
print("You did it! Good job!")
quotes = ["The pain you feel today is the strength you feel tomorrow. For every challenge encountered there is an opportunity for growth",
          "It's hard to beat a person who never gives up. Our greatest glory is not in never failing, but in rising every time we fail.",
          "With or without you, there will be champions. You want your name there? Work hard."]

print("\n")

print(quotes[random.randint(0, len(quotes)-1)])



while start == True:
    good_job.play(0, 0, 0)
    input("")
    start = False






