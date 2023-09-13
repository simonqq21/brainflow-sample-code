import numpy as np 
import pandas as pd 
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets
from brainflow.data_filter import DataFilter 

data = DataFilter.read_file('test.csv')
data_df = pd.DataFrame(np.transpose(data))
print(data_df)
print(data_df.iloc[:,31].unique())
for i in range(1,10):
    print(data_df.loc[data_df.iloc[:,31] == i])