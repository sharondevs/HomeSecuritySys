# Home Security System usign IoT with power optimization
This is my mini project on home security system, done using IoT devices. 


The need for security systems nowadays is a serious demand. As the number of crimes increasing abruptly, we seek help from the third eye- ‘security systems.’ Advancement in the field of security is improving day by day and as a result demands increases resulting in installation and maintenance cost increments. By understanding the need for security as well as to find an effective way to implement it by means of low cost and high efficiency resulted in our project. Investing our ideas and cascading them resulted in Security system using PIR and Laser.’ Simple technology but highly efficient one. ‘Basic password protected door lock system integrated with Laser and in addition to it we’ve introduced PIR (passive infrared sensor). By using PIR sensor we can detect the motion and human presence. By using this system we can save energy by almost more than half of the total energy required to run any other security systems.

    CONTENTS

1.	INTRODUCTION

1.1	OVERVIEW

2.	PRINCIPLE  OF OPERATION

2.1 BLOCK DIAGRAM

3.	SOFTWARE

3.1	 8051 PROGRAM
3.2	 RASPBERRY PI ZERO
3.3	 PROTEUS SIMULATION 

4.	MAJOR COMPONENTS

4.1	Microcontroller
4.2	 Raspberry Pi zero
4.3	 PIR
4.4	 Laser
4.5	 LCD
4.6	 Keyboard
4.7	 Pi Camera
4.8	 Motor Driver
4.9	 Voltage Regulator

5.	CIRCUIT

6.	FUTURE SCOPE
7.	CONCLUSION
8.	REFERANCE

The basic principle of operation is a password protected door lock controlled by a microcontroller. In addition to the basic door we’ve added  2xPIR sensors and a laser circuit for improving security. Raspberry pi zero act as the CPU for our system. PIR-1 act as a motion sensor while PIR-2 is designed for reducing pow-er usage which makes the system to use less power from the main supply.
When PIR-2 detects any motion in its working range it turns the system on and the user is required to enter the password to open the door. User has 3 chances to enter the password and if password entered is wrong for all the three chances system will be lockout for 30 seconds and again reset to main program. If someone try to break the door, system will capture the photo of the intruder and send it t the owners mail id and  if  laser connected to the door breaks buzzer will ring and the owner will be notified about the attempt of robbery or etc. PIR-1 is placed inside the house to detect any break-in t through other doors or win-dows. The system automatically turns off if the PIR-2’s output goes low.  But in this process the system will not remain on for the whole day which consumes more power but whenever PIR-2’s output varies immediately the system turn on.  


