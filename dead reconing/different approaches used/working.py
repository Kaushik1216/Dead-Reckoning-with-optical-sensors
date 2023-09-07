from evdev import InputDevice,categorize,ecodes
import math
import numpy as np
device1 = InputDevice('/dev/input/event1')
device2 = InputDevice('/dev/input/event3')


#coordinates of right mouse

#coordinates of left mouse


#Distnace Between Left and Right mouse
d=8.7

#coordinate of midpont of mouse global 
Xmid,Ymid=0,0
count=0

dpileft = 12594
dpiright = 13300#10345.2676 
#angle value at which mouse previosly  moved
angle=0
while True:
    try:
        count+=1
        X2,X1,Y1,Y2=0,0,0,0
        
        event1= device1.read_one()
        event2= device2.read_one()
        
        if event1 is not None:
            if event1.type==ecodes.EV_REL:
                if event1.code==ecodes.REL_X:
                    X1=(event1.value)/dpiright
                elif event1.code==ecodes.REL_Y:
                    Y1=-(event1.value)/dpiright
        if event2 is not None:
            if event2.type==ecodes.EV_REL:
                if event2.code==ecodes.REL_X:
                    X2=(event2.value)/dpileft
                elif event2.code == ecodes.REL_Y:
                    Y2=-(event2.value)/dpileft
        
        
        #Net change in x and y coordinates
        X=d+X1-X2
        Y=Y1-Y2
        
        #Angle channge due to rotation o 
        
        angletemp = math.atan2(Y,X)
      	
        #Calculation of global coordinates
         
        Xu=(X1+X2)/2
        Yu=(Y1+Y2)/2
        
        angle = angle+angletemp
        

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
        
        # print("tempmatrix : "+str(tempmatrix[0])+"      "+str(tempmatrix[1]))
        #print(X1,T1)
        if count%5000==0:
            #print("count : "+str((count/5000))+"  X1 : "+str(X1) +"  Y1 : "+str(Y1)+"  X2 : "+str(X2)+"  Y2 : "+str(Y2)+"  angle :"+str(math.degrees(angle)%360))
            print("tempmatrix : "+str(tempmatrix[0])+"      "+str(tempmatrix[1]) + "    "+"angle" + str(math.degrees(angle)%360))
           # print(angletemp);

    except KeyboardInterrupt:
        device1.close()
        device2.close()
        break

