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

The block diagram consists of two major parts.
Password protection door lock and
Home security controller
Chapter-3

Software
3.1 µVision IDE
		
	8051 is the root of the system for security.  The industry standard Keil C Compilers, Macro Assemblers, Debuggers, Real-time Kernels, Single-board Computers, and Emulators support all 8051 derivatives and help you get your projects completed on schedule. The Keil 8051 Development Tools are designed to solve the complex problems facing embedded software developers.
3.2 Raspberry Programming

Raspberry Pi Zero Wireless which has an onboard WiFi module. While these directions should work for most any version and form factor of the Raspberry Pi, it will revolve around the Pi Zero W.
3.3 Proteus

Proteus 8 Professional is software which can be used to draw schematics, PCB layout, and code and even simulate the schematic. The Proteus Design Suite is a proprietary software tool suite used primarily for electronic design automation. The software is used mainly by electronic design engineers and technicians to create schematics and electronic prints for manufacturing printed circuit boards.
Chapter-4

Major Components
4.1 8051 Microcontroller

FEATURES OF 8051
• 4096 bytes on-chip program memory.
• 128 bytes on-chip data memory.
• Four register banks.
• 128 User defined software flags.
• Two multiple mode, 16 bit timers/counters.
• Hardware Multiple and divide in 4µsec.
• 64Kb each program and external RAM addressability.

Pin description of 8051
• Pins 1 to 8 − these pins are known as Port 1. This port doesn’t serve any other functions. It is internally pulled up, bi-directional I/O port.
• Pin 9 − It is a RESET pin, which is used to reset the microcontroller to its initial values.
• Pins 10 to 17 − these pins are known as Port 3. This port serves some functions like interrupts, timer input, control signals, serial communication signals RxD and TxD, etc.
• Pins 18 & 19 − these pins are used for interfacing an external crystal to get the system clock.
• Pin 20 − this pin provides the power supply to the circuit.
• Pins 21 to 28 − these pins are known as Port 2. It serves as I/O port. Higher order address bus signals are also multiplexed using this port.
• Pin 29 − this is PSEN pin which stands for Program Store Enable. It is used to read a signal from the external program memory.
• Pin 30 − this is EA pin which stands for External Access input. It is used to enable/disable the external memory interfacing.
• Pin 31 − this is ALE pin which stands for Address Latch Enable. It is used to demultiplex the address-data signal of port.
• Pins 32 to 39 − these pins are known as Port 0. It serves as I/O port. Lower order address and data bus signals are multiplexed using this port.
• Pin 40 − this pin is used to provide power supply to the circuit.

4.2 Raspberry Pi Zero
The Raspberry Pi is a popular Single Board Computer (SBC) in that it is a full computer packed into a single board. Many may already familiar with the Raspberry Pi 3 and its predecessors, which comes in a form factor that has become as highly recognizable. The Raspberry Pi comes in an even smaller form factor. The introduction of the Raspberry Pi Zero allowed one to embed an entire computer in even smaller projects. This guide will cover the latest version of the Zero product line, the Raspberry Pi Zero - Wireless, which has an onboard Wi-Fi module. While these directions should work for most any version and form factor of the Raspberry Pi, it will revolve around the Pi Zero W.


• PWM (pulse-width modulation)
o Software PWM available on all pins
o Hardware PWM available on GPIO12, GPIO13, GPIO18, GPIO19
• SPI
o SPI0: MOSI (GPIO10); MISO (GPIO9); SCLK (GPIO11); CE0 (GPIO8), CE1 (GPIO7)
o SPI1: MOSI (GPIO20); MISO (GPIO19); SCLK (GPIO21); CE0 (GPIO18); CE1 (GPIO17); CE2 (GPIO16)
• I2C
o Data: (GPIO2); Clock (GPIO3)
o EEPROM Data: (GPIO0); EEPROM Clock (GPIO1)
• Serial
o TX (GPIO14); RX (GPIO15

4.3 PIR (Passive Infrared Sensor)

A passive infrared sensor (PIR sensor) is an electronic sensor that measures infrared (IR) light radiating from objects in its field of view. They are most often used in PIR-based motion detectors. PIR sensors are commonly used in security alarms and automatic lighting applications. PIR sensors detect general movement, but do not give information about the object moved. For that purpose, an active IR sensor is required.
     PIR sensors are commonly called simply "PIR", or sometimes "PID", for "passive infrared detector". The term passive refers to the fact that PIR devices do not radiate energy for detection purposes. They work entirely by detecting infrared radiation (radiant heat) emitted by or reflected from objects. Infrared radiation enters through the front of the sensor, known as the 'sensor face'. At the core of a PIR sensor is a solid state sensor or set of sensors, made from piezoelectric materials—materials which generate energy when exposed to heat. The PIR sensors are more complicated than the other sensors as they consist of two slots. These slots are made of a special material which is sensitive to IR. The Fresnel lens is used to see that the two slots of the PIR can see out past some distance. When the sensor is inactive, then the two slots sense the same amount of IR.The ambient amount radiates from the outdoors, walls or room, etc.
     
4.4 Laser (Light amplification by Stimulated Emission)


     Laser” is an acronym for light amplification by stimulated emission of radiation. A laser is created when the electrons in atoms in special glasses, crystals, or gases absorb energy from an electrical current or another laser and become “excited.” The excited electrons move from a lower-energy orbit to a higher-energy orbit around the atom’s nucleus. When they return to their normal or “ground” state, the electrons emit photons (particles of light).
     These photons are all at the same wavelength and are “coherent,” meaning the crests and troughs of the light waves are all in lockstep. In contrast, ordinary visible light comprises multiple wavelengths and is not coherent.
     Laser light is different from normal light in other ways as well. First, its light contains only one wavelength (one specific color). The particular wavelength of light is determined by the amount of energy released when the excited electron drops to a lower orbit. Second, laser light is directional. Whereas a laser generates a very tight beam, a flashlight produces light that is diffuse. Because laser light is coherent, it stays focused for vast distances, even to the moon and back.
     In NIF, as in most large lasers, intense flashes of white light from giant flash lamps “pump” electrons in large slabs of laser glass to a higher-energy state that lasts only about one-millionth of a second. A small pulse of laser light “tuned” to the excited electrons’ energy is directed through the glass slabs. This laser pulse stimulates the electrons to drop to their lower, or ground, energy states and emit a laser photon of exactly the same wavelength.
     An optical switch traps the low-energy laser pulse in the main amplifier for four passes through the laser glass slabs. Mirrors at both ends of the glass amplifier cause the photons to travel back and forth through the glass, stimulating more electrons to drop to their lower energy states and emit photons. This process produces huge numbers of photons of the same wavelength and direction—an extremely bright and straight beam of light. In this way the initial low-energy pulse is amplified by more than a quadrillion times to create 192 highly energetic, tightly focused laser beams that converge in the center of the Target Chamber.
     Lasers can be tiny constituents of microchips or as immense as NIF, which is ten stories high and as wide as three football fields. Lasers are found in a dazzling range of products and technologies, including CD and DVD players, metal-cutting machines, measuring systems, and eye and cosmetic surgery. Early lasers could produce peak powers of some 10,000 watts. Modern lasers can produce pulses that are billions of times more powerful. Scientists have demonstrated NIF’s ability to generate more than 500 trillion watts of power.
Some lasers, such as ruby lasers, emit short pulses of light. Others, like helium–neon gas lasers or liquid dye lasers, emit light that is continuous. NIF, like the ruby laser, emits pulses of light lasting only billionths of a second.
     Laser light does not need to be visible. NIF beams start out as invisible infrared light and then pass through special optics that convert them to visible green light and then to invisible, high-energy ultraviolet light for optimum interaction with the target.
     
     4.5 LCD ( Liquid Crystal Display )
     
     LCD modules are vey commonly used in most embedded projects, the reason being its cheap price, availability and programmer friendly. Most of us would have come across these displays in our day to day life, either at PCO’s or calculators. The appearance and the pinouts have already been visualized above now let us get a bit technical.
     16×2 LCD is named so because; it has 16 Columns and 2 Rows. There are a lot of combinations available like, 8×1, 8×2, 10×2, 16×1, etc. but the most used one is the 16×2 LCD. So, it will have (16×2=32) 32 characters in total and each character will be made of 5×8 Pixel Dots. 
     
     
     

Pin Configuration
Pin No:Pin Name:Description1Vss (Ground)Ground pin connected to system ground2Vdd (+5 Volt)Powers the LCD with +5V (4.7V – 5.3V)3VE (Contrast V)Decides the contrast level of display. Grounded to get maximum contrast.4Register SelectConnected to Microcontroller to shift between command/data register5Read/WriteUsed to read or write data. Normally grounded to write data to LCD6EnableConnected to Microcontroller Pin and toggled between 1 and 0 for data acknowledgement7Data Pin 0

Data pins 0 to 7 forms a 8-bit data line. They can be connected to Microcontroller to send 8-bit data.
These LCD’s can also operate on 4-bit mode in such case Data pin 4,5,6 and 7 will be left free.8Data Pin 19Data Pin 210Data Pin 311Data Pin 412Data Pin 513Data Pin 614Data Pin 715LED PositiveBacklight LED pin positive terminal16LED NegativeBacklight LED pin negative terminal
4.6 Keyboard 4*4

The 4*4 matrix keypad usually is used as input in a project. It has 16 keys in total, which means the same input values.
The SunFouner 4*4 Matrix Keypad Module is a matrix non- encoded keypad consisting of 16 keys in parallel. The keys of each row and column are connected through the pins outside – pin Y1-Y4 as labeled beside control the rows, when X1-X4, the columns.
Working: -	First test whether any key is pressed down. Connect power to rows, so they are High level. Then set all the rows Y1-Y4 as Low and then detect the status of the columns. Any column of Low indicates there is key pressing and that the key is among the 4 keys of the column. If all columns are high, it means no key is pressed down.
Next, locate the key. Since the column in which the pressed key lies is identified, knowing the line would finalize the testing. Thus, set the rows as Low in turns until any is unveiled accordingly – other rows will still be High.
Now the row can be identified. Detect the status of each column in turns. The column tested Low is the one intersecting with the line – their cross point is just the key pressed.



4.7 Pi  Camera


Enabling the camera
Open the raspi-config tool from the Terminal:
sudo raspi-config
Select Enable camera and hit Enter then go to finish and you'll be prompted to reboot.
Using the camera
Applications and libraries for using the camera are available in:
• Linux command line - Using the supplied command line applications (e.g. raspistill)
• Python
See detailed technical specs of the camera hardware and software.
Camera module is interfaced with raspberry Pi to capture the images of the intruder and send it to the owner via email.
	Camera captures the image when someone try to break in to the house or enter wrong password for more than the number of chances given.


4.8 Motor Driver

The ULN2003A is an array of seven NPN Darlington transistors capable of 500 mA, 50 V output. It features common-cathode flyback diodes for switching inductive loads. Typical usage of the ULN2003A is in driver circuits for relays, lamp and LED displays, stepper motors, logic buffers and line drivers.
Pin NumberPin NameDescription1 to 7Input 1 to Input 7Seven Input pins of Darlington pair, each pin is connected to the base of the transistor and can be triggered by using +5V8GroundGround Reference Voltage 0V9COMUsed as test pin or Voltage suppresser 
pin (optional to use)10 to 16Output 1 to Output 7Respective outputs of seven input pins. Each output pin will be connected to ground only when its respective input pin is high(+5V)
ULN2003 Features
• Contains 7 high-voltage and high current Darlington pairs
• Each pair is rated for 50V and 500mA
• Input pins can be triggered by +5V
• All seven Output pins can be connected to gather to drive loads up to (7×500mA) ~3.5A.
• Can be directly controlled by logic devices like Digital Gates, Arduino, PIC etc
• Available in 16-pin DIP, TSSOP, SOIC packages

4.9 Voltage Regulator IC- (78xx)
78xx is a family of self-contained fixed linear voltage regulator integrated circuits. The 78xx family is commonly used in electronic circuits requiring a regulated power supply due to their ease-of-use and low cost.

The xx is replaced with two digits, indicating the output voltage. 7805 has a 5-volt output, while the 7812 produces 12 volts.



We’ve used 7805 and 7812 for powering the circuit. 7805 is used to power the IC and Raspberry Pi zero, whereas 7812 is used for the motor driver. Both the IC’s can regulate their output voltage to a constant voltage, i.e.; for 7805 input greater than 5 v the max limit is regulated to 5v constant at the output and for 7812 input should be greater than 12v to the max input range. 
Chapter 5
Circuit Diagram

The basic circuit of our project is designed by using proteus simulation software. By using proteus one can determine the errors that can occur while doing the project and can rectify it before implementation. We’ve used Keil  µVision IDE software for programming 8051 and linked the hex file to proteus and debugged the program.
	We used the inbuilt PCB design suite by proteus for designing the PCB. By using the available libraries we designed our PCB and etched it using Ferric Chloride and Hydrogen Peroxide as catalyst.

Raspberry Pi 
The Raspberry Pi is a low cost, credit-card sized computer that plugs into a computer monitor or TV, and uses a standard keyboard and mouse. It is a capable little device that enables people of all ages to explore computing, and to learn how to program in languages like Scratch and Python. Here, the raspberry pi forms the secondary circuit for the security system. A portion of the power coming from the raspberry pi is directed to the raspberry pi. Raspberry pi handles for the intruder detection and alert features of the security system.  The system is designed such that whenever the user is currently present inside the home, the alert system is put on standby mode. When the user leaves the home, as the door is locked, the entire alert and the security system automatically gets back online. The access signal coming from the primary is concerned with this feature. The Raspberry Pi is equipped with a pi camera that takes 5 megapixel resolution images. They take the images of the intruder in an event of break-in. The raspberry pi is connected to the internet 24/7. When a break-in occurs , pi detects the intruder using the PIR sensor or the laser-based security provided at the entrance,  sends the images taken to the email of the user and the alert buzzer provided goes off. A signal also goes form the pi to the primary circuit, to indicate that there has been a break-in on the 16x2 LCD display.




                                                                      










Power delivery optimization 
		One of the major advantages of this system is its power saving characteristics. The security system uses custom-build power optimization technique..   It can save power by automatically turning off when PIR input stays constant for a period of time.


When PIR output is connected to IC 741 Opamp, Opamp works as a comparator. When output of PIR turns high, is send to comparator which compares it with reference and thus the output changes according to it. . Op-amp is used for selectively supplying the required power to the primary circuit. The output of the above circuit goes to the power i/p of the circuit.  







Chapter-6
Future scopes
Nothing concerns us more than the fear of someone breaking into our own home.
o In modern world security has an important role in daily life
o  21st century where IoT rules the market, we decided to make cost effective simple security system using cheap products.
o  By integrating the technologies available, we can make the system much efficient that other costly system.
o  Power supply system can be replaced by solar which make the system to use natural resources and can save energy to a great extend. 
o  Laser can be placed in such a way that it can used to protect the entire house/building.
o  Our system can be modified to work as a fire safety system and smoke detector. 
o We can use a GSM module to inform the use as well as neighbour/required authorities that security system has been compromised, to initialize quick response.

Chapter-7
Conclusions
	We hope that this project is helpful to those who aren’t able to implement high costly security systems to protect their personal belongings. 
	There are plenty of home/office security products to ensure total securities. Security is the most significant one for every owner but due to high cost implementation and maintenance becomes too hard for individuals. In many systems the owner won’t have complete accessibility over the hardware and these results in lack of knowledge about the working of the system.
	We give complete access control to the owner so that the hardware maintenance can be neglected which can save a lot of money. These results in complete user friendly device with lot of customizations. 
	We hope our project can help the common people to protect their properties without investing high amount of money in security solutions.

Chapter-8
References
1) www.firmcodes.com/microcontrollers/8051-3/password-based-door-locking-system-8051/ 
2) https://circuitdigest.com/microcontroller-projects/lcd-interfacing-with-8051-microcontroller-89s52 
3) https://circuitdigest.com/microcontroller-projects/keypad-interfacing-with-8051-microcontroller 
4) http://techknowlearn.blogspot.com/2013/07/reset-oscillator-circuit-of-8051-micro.html 
5) https://www.seeedstudio.com/blog/2019/03/04/driving-a-28byj-48-stepper-motor-with-a-uln2003-driver-board-and-arduino/ 
6) https://circuitdigest.com/microcontroller-projects/raspberry-pi-iot-intruder-alert-system 
7) https://en.m.wikipedia.org/wiki/Raspberry_Pi 

