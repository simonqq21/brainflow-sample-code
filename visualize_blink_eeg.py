import time
import sys 
import numpy as np 
import pandas as pd 
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets
from brainflow.data_filter import DataFilter 
import matplotlib.pyplot as plt 

def main():
    blink_data = DataFilter.read_file('Recordings/both_eyes_blink1/data.csv')
    blink_df = pd.DataFrame(np.transpose(blink_data))
    columns = ["index"]
    eeg_labels = []
    for i in range(8):
        columns.append(f"eeg{i}")
        eeg_labels.append(f"eeg{i}")
    columns.append("timestamp")
    print(blink_df.shape[0])
    blink_df = blink_df.iloc[:,np.r_[:9, -2]]
    blink_df.columns = columns
    # blink_df["index"] = blink_df["index"].astype(int)
    blink_df["timestamp"] = pd.to_datetime(blink_df["timestamp"], unit="s")
    print(blink_df.head(10))
    
    active_eeg = ["eeg2"]

    blink_df.iloc[:].plot(y=active_eeg)
    plt.show()

if __name__ == "__main__":
    main()


