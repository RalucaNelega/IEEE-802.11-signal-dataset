import numpy as np
import pandas as pd

dataset = np.load('dataset.npy', allow_pickle=True)

with open('columns.txt', 'r') as f:
    column_names = [line.strip() for line in f]

df = pd.DataFrame(dataset, columns=column_names)
print(df.head())
