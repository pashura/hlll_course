import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.width = 0
pd.options.display.max_columns = 500

data_test = pd.read_csv("data/test.csv")
data_train = pd.read_csv("data/train.csv")
gender_submission = pd.read_csv("data/gender_submission.csv")

#  Just to check how to concat
data_set_full = pd.concat([data_test, data_train])
print(data_set_full.head())


# 1. Find how many kids (<18 y.o) was on Titanic
print(len([i for i in data_train['Age'] if i < 18]))  # 113
print(len(data_train.loc[data_train['Age'] < 18]))  # 113


# 2. Compute average age for men and women separately
men = data_train.loc[data_train['Sex'] == 'male']
women = data_train.loc[data_train['Sex'] == 'female']

print(men['Age'].mean())  # 30.72664459161148
print(women['Age'].mean())  # 27.915708812260537

# Just a test, never mind
ages = [i for i in men['Age'].dropna()]
print(sum(ages) / len(ages))  # 30.72664459161148
ages = [i for i in women['Age'].dropna()]
print(sum(ages) / len(ages))  # 27.915708812260537


# Visualize average ages comparison with diagram using matplotlib
plt.style.use('_mpl-gallery')

x = [0, 1]
y = [men['Age'].mean(), women['Age'].mean()]

fig, ax = plt.subplots()

ax.set_title('Male and female ages')
ax.set_ylabel('Ages')
ax.set_xticks(np.arange(2), labels=['Male', 'Female'])  # matplotlib >= 3.5
ax.bar(x, y, width=0.4,)

plt.show()
