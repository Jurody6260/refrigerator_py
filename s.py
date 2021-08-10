from datetime import datetime
import pandas as pd
from pandas.core.frame import DataFrame

data = pd.read_excel(r'C:\Projects\refrigerator_py\assets\tash_ref.xlsx', usecols='B:O', header=5, nrows=22)
print(data)


# for row_id, row_data in nuk.iterrows():
#     print(row_id)
#     print("_____")
#     print(row_data)