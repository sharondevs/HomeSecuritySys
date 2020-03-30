import RPi.GPIO as gpio
import picamera
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText 
from email.MIMEBase import MIMEBase
from email import encoders
from email.mime.image import MIMEImage
import os

#We specify the email address to whom the email is send
fromaddr = "Email_for_the_device"
toaddr = "The_Owners_Email"

#Invoke the multipart function for email
mail = MIMEMultipart()

mail['From'] = fromaddr
mail['To'] = toaddr
mail['Subject'] = "Home Security system Alert"
body = "Their has been a breach in security , Please find the attachment"
led=22 
pir=17 #For taking PIR input for sensing 
motor=26    #For taking the motor accessing input from the primary 
laser=27 #Taking the laser breach signal from the primary
access=25 #For disabling the security in case of access by the owner.
breach=8 #In case of breach, this is high, coming from the primary board
HIGH=1 
LOW=0
test=20   #Initializing pins
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(led, gpio.OUT)
gpio.setup(pir, gpio.IN)
gpio.setup(laser,gpio.IN)
gpio.setup(access,gpio.IN)
gpio.setup(breach,gpio.OUT)
gpio.setup(test,gpio.OUT)
gpio.setup(motor,gpio.IN)
gpio.setup(5,gpio.OUT)
gpio.setup(6,gpio.OUT)
gpio.setup(13,gpio.OUT)
gpio.setup(19,gpio.OUT)
gpio.output(test,0)
data=""

#Method for sending mail
def sendMail(data):
    mail.attach(MIMEText(body, 'plain'))
    print (data)
    dat='%s.jpg'%data
    print (data)
    attachment = open(dat, 'rb')
    image=MIMEImage(attachment.read())   # For attaching the photo with the email
    attachment.close()
    mail.attach(image)
    dat='%s.jpg'%data
    print(data)
    attachment=open(dat,'rb')
    image=MIMEImage(attachment.read())
    attachment.close()
    mail.attach(image)
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Initializing the SMTP protocol server for port 587 
    server.starttls()
    server.login(fromaddr, "belugvgnkciisoef")  # The google server login for the specified from address and its application password(Not the same as the real passcode for the account)  
    text = mail.as_string()                     # The passcode for the login can be obtained by the method given. 
    
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


def capture_image():
    data= time.strftime("%d_%b_%Y|%H:%M:%S")  # For getting the time of snap
    #camera.start_preview()
    time.sleep(5)
    print (data)
    camera.capture('%s.jpg'%data)  # Capturing the photo
    camera.capture('%s.jpg'%data)  # Another one 
    #camera.stop_preview()
    time.sleep(1)
    camera.close() #Closing the camera application
    sendMail(data)  # Sending the iamge to the sendMail method for mailing

gpio.output(led , 0) 
gpio.output(breach,0)  #  The breach signal from the Raspi for the PIR 
camera = picamera.PiCamera() #Configure the Pi Camera
camera.rotation=180
camera.awb_mode= 'auto'
camera.brightness=55
num=0

# Underlying logic 
while 1:
    if gpio.input(access)==1 and num==0:   # Cheching for the access signal from the Primary, if low indicates the presence of the user 
        if gpio.input(pir)==1 or gpio.input(laser)==1:  # If the PIR or the Laser external circuit send a high, indicating the break-in
            gpio.output(test,0)  # For test
            num+=1
            gpio.output(led, 1) # For indicating the action
            capture_image() # Method for capturing photo involved
            camera.close()
            gpio.output(breach,1) # The signal given out from the raspi to the primary circuit
            while(gpio.input(pir)==1 or gpio.input(laser)==1 ): # Waiting for the detected signals from the PIR and the laser to be low
                time.sleep(1)
            time.sleep(30) # Gives a 30 second alarm time 
            gpio.output(breach,0) #turns the breach signal to the primary off 
            os.system('sudo shutdown -r now') # The RasPi system restarts 
        
        else:
            gpio.output(led, 0) # Indicating no break-in 
            time.sleep(0.01)

    elif gpio.input(access)==0: # If the user is inside 
        num=0  
        if gpio.input(motor)== 1:  # If the user wants to open the door, high is send from the primary 
            control_pins = [5,6,13,19] # For the motor at the entrance  
            for pin in control_pins:  # All the control pins are initialized 
                gpio.setup(pin,gpio.OUT)
                gpio.output(pin,0)
    
            halfstep_seq = [
                [1,0,0,0],
                [1,1,0,0],
                [0,1,0,0],
                [0,1,1,0],
                [0,0,1,0],
                [0,0,1,1],
                [0,0,0,1],
                [1,0,0,1]
                ]

            for i in range(128): # For half step
                for halfstep in range(8):
                    for pin in range(4):
                        gpio.output(control_pins[pin],
                        halfstep_seq[halfstep][pin])
                        time.sleep(0.001)
 
            time.sleep(7)            
            halfstep_seq = [
                [1,0,0,1],
                [0,0,0,1],
                [0,0,1,1],
                [0,0,1,0],
                [0,1,1,0],
                [0,1,0,0],
                [1,1,0,0],
                [1,0,0,0]
            ]
                                   # For the reverse rotation(locking)
            for i in range(128):
                for halfstep in range(8):
                    for pin in range(4):
                        gpio.output(control_pins[pin],
                        halfstep_seq[halfstep][pin])
                        time.sleep(0.001)
