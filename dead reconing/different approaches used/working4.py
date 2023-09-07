from evdev import InputDevice, categorize, ecodes
import math
import time
device2 = InputDevice('/dev/input/event0')
device1 = InputDevice('/dev/input/event3')


#Always put the marked mouse at position 1
dpcy1 = 3850.40
dpcy2 = 4050.0
dpcx1 = 4000.4
dpcx2 = 4100.4
X, Y , Theta = 0,0,0
D = 11.0
count = 0
max_mov = 0
time_mean = 0
try:
    while True:
        s = time.time()
        count += 1
        
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
                    
        max_mov = max(x1_d, y1_d, x2_d, y2_d,max_mov)
        #Converting to centimeters for First mouse
        x1_c = x1_d/dpcx1
        y1_c = y1_d/dpcy1
        
        #Converting to centimeters for Second mouse
        x2_c = x2_d/dpcx2
        y2_c = y2_d/dpcy2
        
        delta_x = (x1_c+x2_c)/2
        delta_y = (y1_c+y2_c)/2
        prev_theta = Theta
        delta_theta = math.atan2(y1_c - y2_c, x1_c - x2_c + D)
        
		
        if count == 1:
            Theta = delta_theta
        else:
            # Check for jumps in the angle due to discontinuities
            if delta_theta - prev_theta > math.pi:
                delta_theta -= 2 * math.pi
            elif delta_theta - prev_theta < -math.pi:
                delta_theta += 2 * math.pi
            Theta += delta_theta
        
        #delta_theta = math.atan2(y1_c - y2_c, x1_c - x2_c + D)
        #Theta += delta_theta
        
        delta_x_global = math.cos(Theta)*delta_x + math.sin(Theta)*delta_y
        delta_y_global = -math.sin(Theta)*delta_x + math.cos(Theta)*delta_y
        
        X += delta_x_global
        Y += delta_y_global
        e = time.time()
        time_mean += (e-s)
        
        if count%50000==0:
            print("C:%d, X:%f, Y:%f, Theta:%f\n"%(count/50000 ,X, Y,math.degrees(Theta)))
            #print("Maximum Movement:",max_mov)
            #print("Average time:",time_mean/count)
            

except KeyboardInterrupt:     
    device1.close()
    device2.close()
