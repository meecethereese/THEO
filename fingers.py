#Import the necessary Packages and scritps for this software to run (Added speak in
#there too as an easer egg)
import cv2
from collections import Counter
from module import findnameoflandmark,findpostion,speak
import os
import math

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
import time




# Code for controlling servos
def init_arm():
    shoulder = 179
    base = 179
    elbow = 90 
    wrist = 179
    increment = 1
    while(True):
        a = kit.servo[0].angle
        b = kit.servo[2].angle
        c = kit.servo[3].angle
        d = kit.servo[4].angle
        foo = True

        if (shoulder > int(a)):
            a+=increment
            foo = False
        elif (shoulder < int(a)):
            a-=increment
            foo = False

        if (base > int(b)):
            b+=increment
            foo = False
        elif (base < int(b)):
            b-=increment
            foo = False

        if(elbow > int(c)):
            c+=increment
            foo = False
        elif(elbow < int(c)):
            c-=increment
            foo = False

        if(wrist > int(d)):
            d+=increment
            foo = False
        elif (wrist < int(d)):
            d-=increment
            foo = False

        if(foo):
            break
        
        
        print(a,b,c,d)

        kit.servo[0].angle = a
        kit.servo[1].angle = a
        kit.servo[2].angle = b
        kit.servo[3].angle = c 
        kit.servo[4].angle = d
        #time.sleep(.0001)

    print("finished")
        
def prep_high_five():
    # kit.servo[0].angle = 180
    # kit.servo[1].angle = 180
    # kit.servo[2].angle = 180
    # kit.servo[3].angle = 40 
    # kit.servo[4].angle = 0
    shoulder = 179
    base = 179
    elbow = 40 
    wrist = 1
    increment = 1
    while(True):
        a = kit.servo[0].angle
        b = kit.servo[2].angle
        c = kit.servo[3].angle
        d = kit.servo[4].angle
        foo = True

        if (shoulder > int(a)):
            a+=increment
            foo = False
        elif (shoulder < int(a)):
            a-=increment
            foo = False

        if (base > int(b)):
            b+=increment
            foo = False
        elif (base < int(b)):
            b-=increment
            foo = False

        if(elbow > int(c)):
            c+=increment
            foo = False
        elif(elbow < int(c)):
            c-=increment
            foo = False

        if(wrist > int(d)):
            d+=increment
            foo = False
        elif (wrist < int(d)):
            d-=increment
            foo = False

        if(foo):
            break
        
        
        print(a,b,c,d)

        kit.servo[0].angle = a
        kit.servo[1].angle = a
        kit.servo[2].angle = b
        kit.servo[3].angle = c 
        kit.servo[4].angle = d
        time.sleep(.01)

    print("finished")

def perform_high_five():
    shoulder = 75
    base = 179
    elbow = 40 
    wrist = 1
    increment = 1
    while(True):
        a = kit.servo[0].angle
        b = kit.servo[2].angle
        c = kit.servo[3].angle
        d = kit.servo[4].angle
        foo = True

        if (shoulder > int(a)):
            a+=increment
            foo = False
        elif (shoulder < int(a)):
            a-=increment
            foo = False

        if (base > int(b)):
            b+=increment
            foo = False
        elif (base < int(b)):
            b-=increment
            foo = False

        if(elbow > int(c)):
            c+=increment
            foo = False
        elif(elbow < int(c)):
            c-=increment
            foo = False

        if(wrist > int(d)):
            d+=increment
            foo = False
        elif (wrist < int(d)):
            d-=increment
            foo = False

        if(foo):
            break
        
        
        print(a,b,c,d)

        kit.servo[0].angle = a
        kit.servo[1].angle = a
        kit.servo[2].angle = b
        kit.servo[3].angle = c 
        kit.servo[4].angle = d
        #time.sleep(.0001)

    time.sleep(.5)
    print("finished")

# call this to high five someone :)
def high():
    init_arm()
    prep_high_five()
    perform_high_five()
    init_arm()


# Computer vision code
async def play_sound():
   os.system("mpg321 high_five.mp3")

    #Use CV2 Functionality to create a Video stream and add some values + variables
cap = cv2.VideoCapture(0)
tip=[8,12,16,20]
tipname=[8,12,16,20]
fingers=[]
finger=[]

#Create an infinite loop which will produce the live feed to our desktop and that will search for hands
while True:
     ret, frame = cap.read() 
     #Unedit the below line if your live feed is produced upsidedown
     #flipped = cv2.flip(frame, flipCode = -1)
     
     #Determines the frame size, 640 x 480 offers a nice balance between speed and accurate identification
     frame1 = cv2.resize(frame, (640, 480))
    
    #Below is used to determine location of the joints of the fingers 
     a=findpostion(frame1)
     b=findnameoflandmark(frame1)
     
     #Below is a series of If statement that will determine if a finger is up or down and hii
     #then will print the details to the console
     if len(b and a)!=0:
        finger=[]
        if a[0][1:] < a[4][1:]: 
           finger.append(1)
           print (b[4])
          
        else:
           finger.append(0)   
        
        fingers=[] 
        for id in range(0,4):
            if a[tip[id]][2:] < a[tip[id]-2][2:]:
               print(b[tipname[id]])

               fingers.append(1)
    
            else:
               fingers.append(0)
     #Below will print to the terminal the number of fingers that are up or down          
     x=fingers + finger
     c=Counter(x)
     up=c[1]
     down=c[0]
     print('This many fingers are up - ', up)
     print('This many fingers are down - ', down)
     
     #Below shows the current frame to the desktop 
     cv2.imshow("Frame", frame1);
     key = cv2.waitKey(1) & 0xFF
     
     if up == 5:
        #play_sound()
        os.system("mpg321 high_five.mp3")
        high()
        break


     #Below will speak out load when |s| is pressed on the keyboard about what fingers are up or down
     #if key == ord("q"):
     #   speak("you have"+str(up)+"fingers up  and"+str(down)+"fingers down") 
     
     #Below states that if the |s| is press on the keyboard it will stop the system
     if key == ord("s"):
       break