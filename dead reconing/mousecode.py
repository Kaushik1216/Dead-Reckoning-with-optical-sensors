from evdev import InputDevice,categorize,ecodes
#evtest ka upper
device2 = InputDevice('/dev/input/event0')  # device one is rightmouse whose usb in down to
#usb cable and written U on usb
device1 = InputDevice('/dev/input/event3') #left mouse

X1,Y1=0,0
X2,Y2=0,0

count=0;
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
        if count%50000==0:
            print("C:%d,X1:%d,Y1:%d X2:%d,Y2:%d\n"%(count/50000,X1,Y1,X2,Y2))

    except KeyboardInterrupt:
        device1.close()
        device2.close()
        break

