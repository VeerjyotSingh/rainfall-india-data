import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.__version__ 
data = pd.read_csv("/Users/veerjyotsingh/Veerjyot Singh/Computer/Python/rainfall_data/rainfall-indiia-data/rainfall in india 1901-2015.csv",sep=",")
y={}
for i in range(1947,2016,1):
    temp = data[["SUBDIVISION","JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]].loc[data["YEAR"]==i]
    data_2010 = np.asarray(temp[["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]].loc[temp["SUBDIVISION"]=="PUNJAB"])
    z=0
    for a in data_2010[0]:
        y[i] = a
        i+=0.083

sns.lineplot(y)
plt.show()
