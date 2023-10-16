#graphing software for log.csv

import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
from datetime import datetime

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

def countPlotLastThirty():
    plt.figure(figsize=(10, 8))
    current_datetime = str(datetime.now())
    #want to sort log.csv rows by month
    print(len(log)-1)

countPlot()