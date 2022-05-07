import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
train_dataset = pd.DataFrame(np.array([[1, 2], [3, 4], [1, 2], [3, 4], [3, 4], [3, 4], [3, 4], [3, 4], [3, 4], [3, 4]]))

print(train_dataset)
num_folds = 5
hoge = [split for split in KFold(num_folds).split(range(len(train_dataset)))]
print(hoge)
print('end')