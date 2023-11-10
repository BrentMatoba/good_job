#graphing software for log.csv

import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
from datetime import datetime

#import data from csv
log = pd.read_csv('log.csv')



def countPlot():
    #Creates countplot of total pomodoros
    log = pd.read_csv('log.csv')

    #Alters initial size of countplot
    plt.figure(figsize=(10, 8))
    #countplot shows how many times something occurs
    sns.countplot(x="Type", data=log)
    print("Total pomodoros:",  len(log)-1)

    #Makes graph appear
    plt.show()

def histPlotLastThirty():
    plt.figure(figsize=(10, 8))
    current_datetime = str(datetime.now())
    #want to sort log.csv rows by month

    #try DateOffset, then iterate backwards through csv until csv date is less than 1 month ago.

    print("current: " + current_datetime)


    lastThirtyRows = log.tail(30)
    sns.histplot(x="Type", data=lastThirtyRows)
    plt.show()
if __name__ == '__main__':
    histPlotLastThirty()
    countPlot(log)
