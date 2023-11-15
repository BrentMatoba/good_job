#I want to make an experience/leveling system even though I'm not completely done with the main functionality pogchamp
#xp equation:  XP threshold ==alogb(Level)+c
    #logarithmic, meaning fast start and gradually slower gains as you level up
    #where to place badges?
    #100 xp per level? why or why not?

    ###Assign an XP value to each Pomodoro session. For simplicity, let's say 1 Pomodoro = 1 XP.
        #Cumulative XP required for each JLPT level:
        #N5: 440 XP
        #N4: 1100 XP (440 from N5 + 660 additional)
        #N3: 1980 XP (1100 from N4 + 880 additional)
        #N2: 3080 XP (1980 from N3 + 1100 additional)
        #N1: 4400 XP (3080 from N2 + 1320 additional)

class Subject:
    name ="asdf"
    pomodoros =0;
    level = 1
    def __init__(self, name):
        self.name = name
        self.pomodoros = 0;
        self.level = 1


if __name__ == '__main__':
    test = Subject("boop")
    print(test.name)
    print(test.pomodoros)