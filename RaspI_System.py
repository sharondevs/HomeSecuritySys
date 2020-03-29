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


fromaddr = "Email_for_the_device"
toaddr = "The_Owners_Email"

mail = MIMEMultipart()

mail['From'] = fromaddr
mail['To'] = toaddr
mail['Subject'] = "Home Security system Alert"
body = "Their has been a breach in security , Please find the attachment"
led=22
pir=17
motor=26
laser=27
access=25
breach=8
HIGH=1
LOW=0
test=20
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

def sendMail(data):
    mail.attach(MIMEText(body, 'plain'))
    print (data)
    dat='%s.jpg'%data
    print (data)
    attachment = open(dat, 'rb')
    image=MIMEImage(attachment.read())
    attachment.close()
    mail.attach(image)
    dat='%s.jpg'%data
    print(data)
    attachment=open(dat,'rb')
    image=MIMEImage(attachment.read())
    attachment.close()
    mail.attach(image)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "belugvgnkciisoef")
    text = mail.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


def capture_image():
    data= time.strftime("%d_%b_%Y|%H:%M:%S")
    #camera.start_preview()
    time.sleep(5)
    print (data)
    camera.capture('%s.jpg'%data)
    camera.capture('%s.jpg'%data)
    #camera.stop_preview()
    time.sleep(1)
    camera.close()
    sendMail(data)

gpio.output(led , 0)
gpio.output(breach,0)
camera = picamera.PiCamera()
camera.rotation=180
camera.awb_mode= 'auto'
camera.brightness=55
num=0


while 1:
    if gpio.input(access)==1 and num==0:
        if gpio.input(pir)==1 or gpio.input(laser)==1:
            gpio.output(test,0)
            num+=1
            gpio.output(led, 1)
            capture_image()
            camera.close()
            gpio.output(breach,1)
            while(gpio.input(pir)==1 or gpio.input(laser)==1 ):
                time.sleep(1)
            time.sleep(30)
            gpio.output(breach,0)
            os.system('sudo shutdown -r now')
        
        else:
            gpio.output(led, 0)
            time.sleep(0.01)

    elif gpio.input(access)==0:
        num=0
        if gpio.input(motor)== 1:
            control_pins = [5,6,13,19]
            for pin in control_pins:
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

            for i in range(128):
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

            for i in range(128):
                for halfstep in range(8):
                    for pin in range(4):
                        gpio.output(control_pins[pin],
                        halfstep_seq[halfstep][pin])
                        time.sleep(0.001)
