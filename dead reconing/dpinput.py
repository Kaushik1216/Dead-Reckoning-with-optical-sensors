import socket
import keyboard

HOST = '192.168.215.200'  # replace with the IP address or hostname of the Raspberry Pi
PORT = 12345  # the same port number used on the Raspberry Pi
count = 0
print("ravi")
# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((HOST, PORT))
    
    while True:
        count += 1
       
        #  a = input("write your input: ")
        if count%50000==0:
            
            if keyboard.is_pressed('a'):
                message = "a"
                print('Sending:', message)
                s.sendall(message.encode('utf-8'))
            elif keyboard.is_pressed('z'):
                message = "z"
                print("stop")
                s.sendall(message.encode('utf-8'))
            elif keyboard.is_pressed('w'):
                message = "w"
                s.sendall(message.encode('utf-8'))
            elif keyboard.is_pressed('d'):
                message = "d"
                s.sendall(message.encode('utf-8'))
            elif keyboard.is_pressed('s'):
                message = "s"
                s.sendall(message.encode('utf-8'))
            elif keyboard.is_pressed('e'):
                message = "e"
                s.sendall(message.encode('utf-8'))