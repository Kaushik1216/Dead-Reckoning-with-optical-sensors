#This programe used to demonstare how to use Loch Antiphase with Hat-MDD10
#AN pin will act as sterring to control direction
#DIG pin will act to ON/OFF motor output.

import socket
import time;

HOST = '0.0.0.0'  # use the default IP address of the Raspberry Pi
PORT = 12345  # choose a free port number
import RPi.GPIO as GPIO			# using Rpi.GPIO module
from time import sleep			# import function sleep for delay
GPIO.setmode(GPIO.BCM)			# GPIO numbering
GPIO.setwarnings(False)			# enable warning from GPIO
AN2 = 25			# set pwm2 pin on MD10-Hat
AN1 = 24			# set pwm1 pin on MD10-hat
DIG2 = 23				# set dir2 pin on MD10-Hat
DIG1 = 18				# set dir1 pin on MD10-Hat
GPIO.setup(AN2, GPIO.OUT)		# set pin as output
GPIO.setup(AN1, GPIO.OUT)		# set pin as output
GPIO.setup(DIG2, GPIO.OUT)		# set pin as output
GPIO.setup(DIG1, GPIO.OUT)		# set pin as output
sleep(1)				# delay for 1 seconds
p1 = GPIO.PWM(AN1, 100)		# set pwm for M1
p2 = GPIO.PWM(AN2, 100)	
	# set pwm for M
def forward(t):
      print ("Forward")			# display "Forward" when programe run
      GPIO.output (DIG1, GPIO.LOW)		# set AN1 as HIGH, M1B will turn ON
      GPIO.output(DIG2, GPIO.LOW)		# set AN2 as HIGH, M2B will turn ON
      p1.start(49)	
   			# set Direction for M1
      p2.start(50)
      #sleep(t)

def backward(t):
      print ("Backward")
      GPIO.output(DIG1, GPIO.HIGH)       
      GPIO.output(DIG2, GPIO.HIGH)       
      p1.start(49)                     
      p2.start(50)                       
      #sleep(t) 

def left(t):
      print ("Left")
      GPIO.output(DIG1, GPIO.LOW)         
      GPIO.output(DIG2, GPIO.LOW)         
      p1.start(49)     #right wheel hai                  
      p2.start(30)   #left wheel hai                    
      #sleep(t)

def right(t):
      print ("Right")
      GPIO.output(DIG1, GPIO.LOW)       
      GPIO.output(DIG2, GPIO.LOW)       
      p1.start(30)                       
      p2.start(50)                     
      #sleep(t)
      #GPIO.cleanup()

def rotateleft(t):
      print("Rotate left")
      GPIO.output(DIG1, GPIO.LOW)         
      GPIO.output(DIG2, GPIO.HIGH)         
      p1.start(49)     #right wheel hai                  
      p2.start(50)   #left wheel hai                    
   #sleep(t)  
   #GPIO.cleanup()

def rotateright(t):
    
      print("rotate right")
      GPIO.output(DIG1, GPIO.HIGH)       
      GPIO.output(DIG2, GPIO.LOW)       
      p1.start(100)                       
      p2.start(100)                     
      sleep(3)
      #GPIO.cleanup()
   
def end(t):
      print ("STOP")
      GPIO.output(DIG1, GPIO.LOW)           # set AN1 as LOW, M1B will STOP
      GPIO.output(DIG2, GPIO.LOW)           # set AN2 as HIGH, M2B will STOP
      p1.start(0)                          # Direction can ignore
      p2.start(0)                          # Direction can ignore
      sleep(t)
   
      GPIO.cleanup()
def stop(t):
      print ("STOP")
      GPIO.output(DIG1, GPIO.LOW)           # set AN1 as LOW, M1B will STOP
      GPIO.output(DIG2, GPIO.LOW)           # set AN2 as HIGH, M2B will STOP
      p1.start(0)                          # Direction can ignore
      p2.start(0)                          # Direction can ignore
      sleep(t)
# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to a local address and port
server.bind((HOST, PORT))
    # Listen for incoming connections
server.listen()
  #  print('Waiting for connection...')
   # Accept a connection
 #   
#    with conn:
   #    
while True:
            conn, addr = server.accept()
            print('Connected by', addr)
            try:
               while True:
                  data = conn.recv(1024).decode('utf-8')
                  if(data=="a"):
                     s = time.time()
                     left(s)
                     conn.sendall("message recievde".encode('utf-8'))
                     continue
                  elif data=="d":
                     s = time.time()
                     right(s)
                     continue
                  elif data=="s":
                     s= time.time()
                     backward(s)
                     continue
                  elif data=="w":
                     s=time.time()
                     forward(s)
                     continue
                  elif data=="e":
                     s=time.time()
                     rotateright(s)
                     continue
                  elif data=="z":
                     s=time.time()
                     end(s)
                     continue
                  elif data=="q":
                     s=time.time()
                     stop(s)
                  
                    
                     
                     
                     #print('message received: {data}'.format(data=data))
            
            finally:
                  conn.close()
            #print("chal bhi raha hai")
            # Receive data from the client
            #data = conn.recv(1024).decode('utf-8')
            #print(data)
         
            #if not data:
            #    break
            # Print the received data
            
            
            



#try:					
   #while True:
 
  
   #GPIO.cleanup() 	#delay for 2 second
   
   
   
   
  

   
   
   
   
  
   

                            

    
   
  
                           
   
                            
	
  
   
   
                            #delay for 3 second
	

#except:					# exit programe when keyboard interupt
   #p1.start(0)				# set speed to 0
   #p2.start(0)	
   
   #GPIO.cleanup() 			# set speed to 0
					# Control+X to save and exit
   
						
