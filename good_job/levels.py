#I want to make an experience/leveling system even though I'm not completely done with the main functionality pogchamp
#xp equation:  XP threshold ==alogb(Level)+c
    #logarithmic, meaning fast start and gradually slower gains as you level up
    #where to place badges?
    #100 xp per level? why or why not?
import csv


###Assign an XP value to each Pomodoro session. For simplicity, let's say 1 Pomodoro = 1 XP.
        #Cumulative XP required for each JLPT level:
        #N5: 440 XP
        #N4: 1100 XP (440 from N5 + 660 additional)
        #N3: 1980 XP (1100 from N4 + 880 additional)
        #N2: 3080 XP (1980 from N3 + 1100 additional)
        #N1: 4400 XP (3080 from N2 + 1320 additional)

class Subject:
    name = None
    pomodoros =None;
    level = None
    def __init__(self, name):
        self.name = name
        self.pomodoros = 0;
        self.level = 1

def rankFinder():
    #find number of pomodoros,
    None
    #Feed them into level equation
    #Per x amount of levels, increase rank by one,
    #Assign badges to ranks
    #make display for gui
def scanLog(subject):
    counter = 0;
    with open("log.csv", "r") as log:
        reader = csv.reader(log)
        for line in reader:
            print(line[1])
            if line[1] == subject:
                counter+=1
    return counter


if __name__ == '__main__':
    print(scanLog(" odin") + scanLog(" extracurricular programming") + scanLog(" school programming") //2)