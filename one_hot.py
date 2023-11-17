import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

columns_names = data['whoAmI'].unique()
one_hot_data = pd.DataFrame()
for name in columns_names:
    one_hot_data[name] = (data['whoAmI'] == name).astype(int)    
one_hot_data.head()