#graphing software for log.csv

import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd

#import data from csv
log = pd.read_csv('log.csv')
#make bar graph
print(log)

