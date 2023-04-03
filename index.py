import evdev

# Get the mouse device
# devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
# print(devices)
# for device in devices:
#     if 'Mouse' in device.name:
#         mouse = device
#         break
# else:
#     print('No mouse found')

# # Set up the event types to listen for
# mouse.grab()
# mouse.evbits |= evdev.ecodes.EV_REL
# mouse.evbits |= evdev.ecodes.EV_KEY
# mouse.evbits |= evdev.ecodes.EV_SYN
# mouse.sync_evbits()

device1 = evdev.InputDevice('/dev/input/event4')
# Initialize the x and y coordinates
x = 0
y = 0

# Event loop
while True:
    event=device1.read_one()
    try:
# for event in device1.read_loop():
        if event.type == evdev.ecodes.EV_REL:
            if event.code == evdev.ecodes.REL_X:
                x += event.value
            elif event.code == evdev.ecodes.REL_Y:
                y += event.value
        elif event.type == evdev.ecodes.EV_KEY:
            # Check for shift key
            if event.code == evdev.ecodes.KEY_LEFTSHIFT or event.code == evdev.ecodes.KEY_RIGHTSHIFT:
                if event.value == 1:  # Shift key down
                    print("Shift key pressed")
                elif event.value == 0:  # Shift key up
                    print("Shift key released")
        elif event.type == evdev.ecodes.EV_SYN:
            # Calculate the shift angle
            angle = -1 * (y / 40)  # Adjust the divisor to change sensitivity
            print(f"X: {x}, Y: {y}, Angle: {angle}")
    
    except  KeyboardInterrupt:
        device1.close()
        break
