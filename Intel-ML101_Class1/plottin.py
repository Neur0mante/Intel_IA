import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

filepath = 'data/Iris_Data.csv'
data = pd.read_csv(filepath)


# plt.plot(data.sepal_length,
# data.sepal_width,
# ls ='', marker='o')

# plt.show()
import seaborn as sns


data = data[0:10]
sequ = tuple(data.sepal_length),tuple(data.sepal_width)

sns.jointplot(x='sepal_length',
y='sepal_width',
data=sequ)