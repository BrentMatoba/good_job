#graphing software for log.csv

import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd

#import data from csv
log = pd.read_csv('log.csv')



def countPlot():
    #Creates countplot of total pomodoros
    #Alters initial size of countplot
    plt.figure(figsize=(10, 8))
    #countplot shows how many times something occurs
    sns.countplot(x="Type", data=log)


    #Makes graph appear
    plt.show()



countPlot()