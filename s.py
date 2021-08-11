from datetime import datetime
import pandas as pd
from pandas.core.frame import DataFrame
import json

# data = pd.read_excel(r'C:\Projects\refrigerator_py\assets\tash_ref.xlsx', usecols='B:O', header=5, nrows=22)
data = pd.read_excel(r'C:\Projects\refrigerator_py\assets\tash_ref.xlsx', "Омборхона ва холодилник", 7, usecols='B:H', nrows=154)
completed_json = []
jsonf = {}
counter = 0
data = data.fillna("None")
for index, row_data in data.iterrows():

    ################ 1 bolim ################

    jsonf['district'] = row_data[0]
    jsonf['org_name'] = row_data[1]
    jsonf['name'] = row_data[2]
    jsonf['quantity'] = row_data[3]
    jsonf['capacity'] = row_data[4]
    jsonf['created_workplaces'] = row_data[5]
    # jsonf['date_of_registry'] = row_data[6]
    jsonf['type'] = 'storage'
    completed_json.append(jsonf)
    jsonf = {}

    # counter += 1
    # print(counter)
    # print(type(row_data[5]))
with open('data.json', 'w', encoding='utf-8') as outfile:
    outfile.write(json.dumps(completed_json, ensure_ascii=False, indent=4))
    outfile.close()
    
    ################ 2 bolim ################

    # jsonf['district'] = row_data[0]
    # jsonf['org_name'] = row_data[1]
    # jsonf['name'] = row_data[2]
    # jsonf['created_workplaces'] = row_data[7]
    # # jsonf['date_of_registry'] = row_data[6]
    # # jsonf['type'] = 
    # if row_data[3] and row_data[3] != 'None':
    #     jsonf['type'] = 'simple_refrig'
    #     jsonf['quantity'] = row_data[3]
    #     jsonf['capacity'] = row_data[4]
    # elif row_data[5] and row_data[5] != 'None':
    #     jsonf['type'] = 'shock_refrig'
    #     jsonf['quantity'] = row_data[5]
    #     jsonf['capacity'] = row_data[6]
    # else:
    #     jsonf['type'] = "None"
    #     jsonf['quantity'] = "None"
    #     jsonf['capacity'] = "None"
#     completed_json.append(jsonf)
#     jsonf = {}

#     # counter += 1
#     # print(counter)
#     # print(type(row_data[5]))
# with open('data_2.json', 'w', encoding='utf-8') as outfile:
#     outfile.write(json.dumps(completed_json, ensure_ascii=False, indent=4))
#     outfile.close()

