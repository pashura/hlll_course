import numpy as np
import pandas as pd

a = np.array([[1, 2, 3, 2, 1, 0], [4, 5, 6, 5, 4, 3], [7, 8, 9, 8, 7, 6]])

df = pd.DataFrame([[0, 2, 3], [5, 4, 1], [10, 20, 30]], index=[4, 5, 6], columns=['A', 'B', 'C'])

print(df.loc[df['A'] > 7])

# print(a)
# print(df)
