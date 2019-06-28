import pandas as pd
from string import ascii_lowercase
import numpy as np

df = pd.DataFrame(np.random.randn(50, 4), columns=list('ABCD'))

def abc_df(data):
    df = pd.DataFrame(data=data,    # values
                      index=list(ascii_lowercase[:data.shape[0]]),    # 1st column as index
                      columns=list(ascii_lowercase[:data.shape[1]]))
    return df

def last_col_median(df):
    if np.issubdtype(df.iloc[:,-1].dtype, np.number):
        return df.iloc[:,-1].median(axis=0)
    else:
        return None

# def last_col_median(df):
#     last_col = df.iloc[:,-1]
#     try:
#         answer = last_col.median()
#     except TypeError:
#         answer = None
#     return answer

# last_col_median(df)
# https://docs.python.org/2/tutorial/errors.html

def most_common_index(df):
    return max(df.index.value_counts())

# most_common_index(df)
