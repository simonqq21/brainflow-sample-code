import time
import numpy as np
import pandas as pd
from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardIds
from brainflow.data_filter import DataFilter, FilterTypes
from datetime import datetime, timedelta
from pprint import pprint 
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, lfilter_zi, filtfilt, sosfiltfilt, sosfilt, sosfilt_zi

def butter_bandpass(lowcut, highcut, fs, order):
    nyq = fs * 0.5 
    low = lowcut / nyq 
    high = highcut / nyq 
    return butter(order, [low, high], btype="bandpass", output='sos')

def butter_bandpass_filter(data, lowcut, highcut, fs, order):
    sos = butter_bandpass(lowcut, highcut, fs, order)
    filtered = sosfiltfilt(sos, data)
    return filtered

freq = 4
time_ = np.arange(0, 2, 0.01)
print(time_)
signal = np.sin(2* np.pi* freq * time_)

# filtered = butter_bandpass_filter(signal, 1, 2, 200, 3)
# filtered2 = butter_bandpass_filter(signal, 2, 4, 200, 3)
# filtered3 = butter_bandpass_filter(signal, 4, 16, 200, 3)

filtered = np.copy(signal)
filtered2 = np.copy(signal)
filtered3 = np.copy(signal)
DataFilter.perform_bandpass(filtered, sampling_rate=100, \
    start_freq=1, stop_freq=2, order=4, 
    filter_type=FilterTypes.BUTTERWORTH_ZERO_PHASE, ripple=0)
DataFilter.perform_bandpass(filtered2, sampling_rate=100, \
    start_freq=2, stop_freq=3, order=4, 
    filter_type=FilterTypes.BUTTERWORTH_ZERO_PHASE, ripple=0)
DataFilter.perform_bandpass(filtered3, sampling_rate=100, \
    start_freq=3, stop_freq=8, order=4, 
    filter_type=FilterTypes.BUTTERWORTH_ZERO_PHASE, ripple=0)

plt.plot(time_, signal, color="black")
plt.plot(time_, filtered, color="red")
plt.plot(time_, filtered2, color="green")
plt.plot(time_, filtered3, color="blue")
plt.savefig("test_filtering_bf_bw_zp.png") 
plt.show()
