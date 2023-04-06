import pygame
pygame.init()
pygame.mixer.init()

#things to do
#game window
#load star
#make text boxes in window
#Change font/size
#One textbox optional, can user prompt to say what they did
#is this fun or sad lmfao
#I have a supportive network I swear
#little animation maybve? star comes in on a swirly pattern?
#Make desktop shortcut
#reduce volume
#improve sound loop code


start = True
good_job = pygame.mixer.Sound("ST_Fanfare_WinBattle.wav")
length = pygame.mixer.Sound.get_length(good_job)

while start == True:
    good_job = pygame.mixer.Sound("ST_Fanfare_WinBattle.wav")
    good_job.play(0, 0, 0)
    print("You did it!")
    input("")
    start = False






