from scipy.signal import butter, filtfilt
import numpy as np
from evdev import InputDevice, categorize, ecodes
import math
import time


device2 = InputDevice('/dev/input/event0')
device1 = InputDevice('/dev/input/event3')
# Define the low-pass filter function
def butter_lowpass(cutoff, fs, order=2):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

# Set the parameters for the low-pass filter
cutoff_freq = 5# Hz
sampling_freq = 100  # Hz
filter_order = 3
# Create the filter coefficients
b, a = butter_lowpass(cutoff_freq, sampling_freq, filter_order)

# Initialize an array to store the filtered data
filtered_data = np.zeros((2, 2))



#Always put the marked mouse at position 1
dpcy1 = 4000.40
dpcy2 = 4050.0
dpcx1 = 4150.4
dpcx2 = 4360.4
X, Y , Theta = 0,0,0
D = 11.0
count = 0
max_mov = 0
time_mean = 0

try:
    while True:
        s = time.time()
        count += 1
        
        # Read the raw data from the mice
        event1 = device1.read_one()
        event2 = device2.read_one()
        x1_d, y1_d = 0, 0
        x2_d, y2_d = 0, 0
        if event1 is not None:
            if event1.type == ecodes.EV_REL:
                if event1.code == ecodes.REL_X:
                    x1_d = event1.value
                elif event1.code == ecodes.REL_Y:
                    y1_d = -event1.value
        if event2 is not None:
            if event2.type == ecodes.EV_REL:
                if event2.code == ecodes.REL_X:
                    x2_d = event2.value
                elif event2.code == ecodes.REL_Y:
                    y2_d = -event2.value
                    
        max_mov = max(x1_d, y1_d, x2_d, y2_d, max_mov)
        
        # Convert the raw data to centimeters
        x1_c = x1_d / dpcx1
        y1_c = y1_d / dpcy1
        x2_c = x2_d / dpcx2
        y2_c = y2_d / dpcy2
        
        # Combine the data from the two mice
        delta_x = (x1_c + x2_c) / 2
        delta_y = (y1_c + y2_c) / 2
        
        # Calculate the change in angle
        delta_theta = math.atan2(y1_c - y2_c, x1_c - x2_c + D)
        Theta += delta_theta
        
        # Convert the data to global coordinates
        delta_x_global = math.cos(Theta) * delta_x + math.sin(Theta) * delta_y
        delta_y_global = -math.sin(Theta) * delta_x + math.cos(Theta) * delta_y
        
        # Apply the low-pass filter to the data
        input_data = np.array([[delta_x_global, delta_y_global]])
        filtered_data = filtfilt(b, a, input_data, axis=0, padtype=None)
        
        # Update the position
        X += filtered_data[0, 0]
        Y += filtered_data[0, 1]
        
        e = time.time()
        time_mean += (e - s)
        
        if count % 500 == 0:
            print("C:%d, X:%f, Y:%f, Theta:%f\n" % (count / 500, X, Y, math.degrees(Theta)))
            
except KeyboardInterrupt:
        device1.close()
        device2.close()
        
