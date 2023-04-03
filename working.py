from evdev import InputDevice,categorize,ecodes
import math
import numpy as np
device1 = InputDevice('/dev/input/event16')
device2 = InputDevice('/dev/input/event19')


#coordinates of right mouse
X1,Y1=0,0
#coordinates of left mouse
X2,Y2=0,0

#Distnace Between Left and Right mouse
d=10

#coordinate of midpont of mouse global 
Xmid,Ymid=0,0
count=0

#angle value at which mouse previosly  moved
angle=0
while True:
    try:
        count+=1

        event1= device1.read_one()
        event2= device2.read_one()
        if event1 is not None:
            if event1.type==ecodes.EV_REL:
                if event1.code==ecodes.REL_X:
                    X1+=event1.value
                elif event1.code==ecodes.REL_Y:
                    Y1-=event1.value
        if event2 is not None:
            if event2.type==ecodes.EV_REL:
                if event2.code==ecodes.REL_X:
                    X2+=event2.value
                elif event2.code == ecodes.REL_Y:
                    Y2-=event2.value
        
        #Net change in x and y coordinates
        X=d+X1-X2
        Y=Y1-Y2

        #Angle channge due to rotation o 
        if(X1-X2!=0 and  Y1-Y2!=0 and X!=0):
            temp=Y/X
            angletemp = math.atan(temp)
        else:
            angletemp = -angle
        #Calculation of global coordinates

        Xu=(X1+X2)/2
        Yu=(Y1+Y2)/2
        
        angle = math.radians(math.degrees(angle)+math.degrees(angletemp))

        #rotational matrix
        rmatrix = np.array([[math.cos(angle), math.sin(angle)], [-math.sin(angle), math.cos(angle)]])

        #tempary local coordinates matrix 
        localmatrix=np.array([Xu,Yu])
     
        #global cooredinates matrix ith movement

        tempmatrix=np.array([Xmid,Ymid])

        #New coordinate at (i+1)th movement
        tempmatrix = tempmatrix + (np.dot(rmatrix,localmatrix));

        Xmid=tempmatrix[0];
        Ymid=tempmatrix[1];
        
        print("tempmatrix : "+str(tempmatrix[0])+"      "+str(tempmatrix[1]))
        
        if count%50000==0:
            print("count : "+str((count/50000))+"  X1 : "+str(X1) +"  Y1 : "+str(Y1)+"  X2 : "+str(X2)+"  Y2 : "+str(Y2)+"  angle :"+str(angle))
            print("tempmatrix : "+str(tempmatrix[0])+"      "+str(tempmatrix[1]))

    except KeyboardInterrupt:
        device1.close()
        device2.close()
        break

