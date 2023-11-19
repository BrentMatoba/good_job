#graphing software for log.csv

import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import csv
from datetime import datetime, timedelta

#import data from csv
log = pd.read_csv('log.csv')


def chatCount():
    # Step 2: Read the CSV file
    df = pd.read_csv('log.csv', parse_dates=['Date'])

    # Step 3: Calculate the date for one week ago
    one_week_ago = datetime.now() - timedelta(days=7)

    # Step 4: Filter the DataFrame
    last_week_data = df[df['Date'] >= one_week_ago]

    # Step 5: Access the filtered data
    return last_week_data

def countPlot():
    #Creates countplot of total pomodoros
    log = pd.read_csv('log.csv')

    #Alters initial size of countplot
    window = plt.figure(figsize=(10, 8))

    #Changes window title
    window.canvas.manager.set_window_title("CountPlot")

    #Gives the graph a title
    plt.title("Total Pomodoros")

    #countplot shows how many times something occurs
    sns.countplot(x="Type", data=log)

    #Displays total pomodoros on graph
    plt.text(-1, -10, "Total Pomodoros: " + str(len(log)-1))

    #Makes graph appear
    plt.show()

def histPlotLastThirty():
    window = plt.figure(figsize=(10, 8))
    #try DateOffset, then iterate backwards through csv until csv date is less than 1 month ago.

    #Changes window title
    window.canvas.manager.set_window_title("Histogram")



    lastThirtyRows = log.tail(30)
    sns.histplot(x="Type", data=lastThirtyRows)
    plt.show()


def chatPlotLastWeek():
    window = plt.figure(figsize=(10, 8))
    window.canvas.manager.set_window_title("Pomodoros over last week")
    #sns.histplot(x="x", data=chatCount())
    print(chatCount())


def histPlotLastWeek():
    with open("log.csv", "r") as log:
        reader = csv.reader(log)
        next(reader)
        rows = list(reader)
        now = datetime.now()
        oneWeekAgo = now - timedelta(weeks=1)
        for row in rows:
            date_string = row[0]
            modified_date_string = date_string.replace(".", ":")
            date_obj = datetime.strptime(modified_date_string, "%Y-%m-%d %H:%M:%S:%f") #this formatting is right but I need to pad an extra micro second onto every piece of data I have looooo

            result = date_obj-oneWeekAgo
            result = str(result)

        #ok so I figured out how to access the data, but you need to figure out how to access only the days with positive time. Also result and oneWeekAgo are not the same object type and thats causign issues
            negativeCheck = "-"
            if negativeCheck not in result:
                print(row)
        #You got this! After we figure this part out the rest should be pretty easy.
        #Its easy but thsi should have taken four lines and chatgpt figured itout......

if __name__ == '__main__':
    #histPlotLastThirty()
    #countPlot()
    histPlotLastWeek()
    #chatPlotLastWeek()