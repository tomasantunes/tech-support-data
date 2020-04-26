from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file = r'data.csv'
df = pd.read_csv(file)

df1 = df.sort_values(by='no_of_cases', ascending=False).head(10)
y_pos = np.arange(len(df1))

df1.plot.barh(x="PROBLEM_TYPE", y="no_of_cases", align='center', alpha=0.5, legend=None);
plt.xlabel('Nr. of cases')
plt.ylabel('Problem Type')
plt.gca().invert_yaxis()
plt.title("Most frequent problems")
plt.tight_layout()

plt.show(block=True);

df1 = df.sort_values(by='recurrence_freq', ascending=False).head(10)
y_pos = np.arange(len(df1))

df1.plot.barh(x="PROBLEM_TYPE", y="recurrence_freq", align='center', alpha=0.5, legend=None);
plt.xlabel('Recurrence')
plt.ylabel('Problem Type')
plt.gca().invert_yaxis()
plt.title("Most recurrent problems")
plt.tight_layout()

plt.show(block=True);