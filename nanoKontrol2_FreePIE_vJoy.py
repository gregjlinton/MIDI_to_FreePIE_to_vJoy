# This is a work in progress and to hell with your warranty!
# I wanted to use a Korg nanoKontrol2 as a joystick. Why? 'Cause buttons, dials & sliders for cheaper ($80 CDN).
# This: http://www.korg.com/caen/products/computergear/nanokontrol2/
# To make this work we need to monitor the midi from the nanoKontrol2 and convert them in real time to a joystick output.
# We can do that with FreePIE (Programmable Input Emulator): http://andersmalmgren.github.io/FreePIE/
# FreePIE converts that to an output for a virtual joystick.
# For this we're using vJoy: http://vjoystick.sourceforge.net/site/
# vJoy only supports a limited number of axis which we want to use as sliders/dials and other inputs to games.
# To make this all work, we're going to have to split layout of the nanoKontrol2 into multiple virtual joysticks.
# 4 dials and 4 sliders on the left as a joystick (with some buttons?), 4 dials and 4 sliders on the right as a second joystick (with some buttons?).
# A 3rd joystick could be used for all the "transport" buttons (forward, back, play, record, next track, etc).
# All of this was coded in a brute force way because I am a noob at this.

# Install vJoy.
# Install FreePIE.
# Install Korg Kontrol Editor. https://www.korg.com/us/support/download/software/0/159/1354/
# Starting with Korg Kontrol Editor. Run it and see if you can connect to the nanoKontrol2. This should bring up a "map" of the nanoKontrol2 and the Control Channels (CC#)'s.
# Open vJoyConf. Create 2 joysticks. 1 has all the axis enables with 36 buttons. 2 has all the exis enabled with any number of buttons since they won't be used.
# Open vJoy Monitor.
# Copy/paste or open this code in/into FreePIE. Save it as a script, then press run. If it all works, you should be able to monitor the joystick outuput with vJoy's monitor program.

def update():
   diagnostics.watch(midi[0].data.channel)
   diagnostics.watch(midi[0].data.status)
   diagnostics.watch(midi[0].data.buffer[0])
   diagnostics.watch(midi[0].data.buffer[1])


# Sliders and Dials and buttons on the left side of the nanoKontrol2
# Change the value after == to the Control Channel (CC#) you want as input from the nanoKontrol2
# Change the value after vJoy[0]. you want to be the button on your virtual joystick.
# Change the value after vJoy[ for the virtual joystick you want to use [0] or [1] for example.

#slider_1
if midi[0].data.buffer[0] == 0:#CC0
	slide_1 = midi[0].data.buffer[0] == 0 and filters.mapRange(midi[0].data.buffer[1], 0, 127, -17873, 17873)
	vJoy[0].x = slide_1;
#dial_1
if midi[0].data.buffer[0] == 16:#CC16
	dial_1 = midi[0].data.buffer[0] == 16 and filters.mapRange(midi[0].data.buffer[1], 0, 127, -17873, 17873)
	vJoy[0].rx = dial_1;

#Button S1 CC#32
if (midi[0].data.buffer[0] == 32) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(14,True)  

if (midi[0].data.buffer[0] == 32) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(14,False)

#Button M1 CC#45
if (midi[0].data.buffer[0] == 48) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(13,True)  

if (midi[0].data.buffer[0] == 48) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(13,False)

#Button R1 CC#64
if (midi[0].data.buffer[0] == 64) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(12,True)  

if (midi[0].data.buffer[0] == 64) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(12,False)


#slider_2
if midi[0].data.buffer[0] == 1:#CC1	
	slide_2 = midi[0].data.buffer[0] == 1 and filters.mapRange(midi[0].data.buffer[1], 0, 127, -17873, 17873)
	vJoy[0].y = slide_2;

#dial_2
if midi[0].data.buffer[0] == 17:#CC17
	dial_2 = midi[0].data.buffer[0] == 17 and filters.mapRange(midi[0].data.buffer[1], 0, 127, -17873, 17873)
	vJoy[0].ry = dial_2;

#Button S2 CC#33
if (midi[0].data.buffer[0] == 33) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(17,True)  

if (midi[0].data.buffer[0] == 33) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(17,False)

#Button M3 CC#49
if (midi[0].data.buffer[0] == 49) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(16,True)  

if (midi[0].data.buffer[0] == 49) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(16,False)

#Button R3 CC#65
if (midi[0].data.buffer[0] == 65) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(15,True)  

if (midi[0].data.buffer[0] == 65) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(15,False)

#slider_3
if midi[0].data.buffer[0] == 2:#CC2	
	slide_3 = midi[0].data.buffer[0] == 2 and filters.mapRange(midi[0].data.buffer[1], 0, 127, -17873, 17873)
	vJoy[0].z = slide_3;
#dial_3
if midi[0].data.buffer[0] == 18:#CC18
	dial_3 = midi[0].data.buffer[0] == 18 and filters.mapRange(midi[0].data.buffer[1], 0, 127, -17873, 17873)
	vJoy[0].rz = dial_3;

#Button S3 CC#34
if (midi[0].data.buffer[0] == 34) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(20,True)  

if (midi[0].data.buffer[0] == 34) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(20,False)

#Button M3 CC#50
if (midi[0].data.buffer[0] == 50) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(19,True)  

if (midi[0].data.buffer[0] == 50) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(19,False)

#Button R3 CC#66
if (midi[0].data.buffer[0] == 66) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(18,True)  

if (midi[0].data.buffer[0] == 66) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(18,False)


#slider_4
if midi[0].data.buffer[0] == 3:#CC3	
	slide_4 = midi[0].data.buffer[0] == 3 and filters.mapRange(midi[0].data.buffer[1], 0, 127, -17873, 17873)
	vJoy[0].slider = slide_4;
#dial_4
if midi[0].data.buffer[0] == 19:#CC19
	dial_4 = midi[0].data.buffer[0] == 19 and filters.mapRange(midi[0].data.buffer[1], 0, 127, -17873, 17873)
	vJoy[0].dial = dial_4;

#Button S4 CC#35
if (midi[0].data.buffer[0] == 35) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(23,True)  

if (midi[0].data.buffer[0] == 35) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(23,False)

#Button M4 CC#51
if (midi[0].data.buffer[0] == 51) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(22,True)  

if (midi[0].data.buffer[0] == 51) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(22,False)

#Button R4 CC#67
if (midi[0].data.buffer[0] == 67) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(21,True)  

if (midi[0].data.buffer[0] == 67) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(21,False)
	
	
# Because vJoy only supports a total of 8 axis per joystick, we have to split up the slider and dials section into two halves. The second half will be on the second virtual joystick vJoy[1]. 
# Sliders and Dials and buttons on the right side of the nanoKontrol2

#slider_5
if midi[0].data.buffer[0] == 4:#CC4
	slide_1 = midi[0].data.buffer[0] == 4 and filters.mapRange(midi[0].data.buffer[1], 0, 127, -17873, 17873)
	vJoy[1].x = slide_1;
#dial_5
if midi[0].data.buffer[0] == 20:#CC20
	dial_1 = midi[0].data.buffer[0] == 20 and filters.mapRange(midi[0].data.buffer[1], 0, 127, -17873, 17873)
	vJoy[1].rx = dial_1;

# Since vJoy can handle 128 buttons, we'll keep all the mashable buttons on the nanoKontrol2 to virtual joystick 1 vJoy[0]
#Button S5 CC#36
if (midi[0].data.buffer[0] == 36) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(26,True)  

if (midi[0].data.buffer[0] == 36) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(26,False)

#Button M5 CC#52
if (midi[0].data.buffer[0] == 52) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(25,True)  

if (midi[0].data.buffer[0] == 52) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(25,False)

#Button R5 CC#66
if (midi[0].data.buffer[0] == 68) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(24,True)  

if (midi[0].data.buffer[0] == 68) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(24,False)

#slider_6
if midi[0].data.buffer[0] == 5:#CC5	
	slide_2 = midi[0].data.buffer[0] == 5 and filters.mapRange(midi[0].data.buffer[1], 0, 127, -17873, 17873)
	vJoy[1].y = slide_2;
#dial_6
if midi[0].data.buffer[0] == 21:#CC21
	dial_2 = midi[0].data.buffer[0] == 21 and filters.mapRange(midi[0].data.buffer[1], 0, 127, -17873, 17873)
	vJoy[1].ry = dial_2;

#Button S6 CC#37
if (midi[0].data.buffer[0] == 37) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(29,True)  

if (midi[0].data.buffer[0] == 37) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(29,False)

#Button M6 CC#53
if (midi[0].data.buffer[0] == 53) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(28,True)  

if (midi[0].data.buffer[0] == 53) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(28,False)

#Button R6 CC#69
if (midi[0].data.buffer[0] == 69) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(27,True)  

if (midi[0].data.buffer[0] == 69) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(27,False)

#slider_7
if midi[0].data.buffer[0] == 6:#CC6	
	slide_3 = midi[0].data.buffer[0] == 6 and filters.mapRange(midi[0].data.buffer[1], 0, 127, -17873, 17873)
	vJoy[1].z = slide_3;
#dial_7
if midi[0].data.buffer[0] == 22:#CC22
	dial_3 = midi[0].data.buffer[0] == 22 and filters.mapRange(midi[0].data.buffer[1], 0, 127, -17873, 17873)
	vJoy[1].rz = dial_3;

#Button S7 CC#38
if (midi[0].data.buffer[0] == 38) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(32,True)  

if (midi[0].data.buffer[0] == 38) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(32,False)

#Button M7 CC#54
if (midi[0].data.buffer[0] == 54) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(31,True)  

if (midi[0].data.buffer[0] == 54) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(31,False)

#Button R7 CC#70
if (midi[0].data.buffer[0] == 70) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(30,True)  

if (midi[0].data.buffer[0] == 70) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(30,False)

#slider_8
if midi[0].data.buffer[0] == 7:#CC7	
	slide_4 = midi[0].data.buffer[0] == 7 and filters.mapRange(midi[0].data.buffer[1], 0, 127, -17873, 17873)
	vJoy[1].slider = slide_4;
#dial_8
if midi[0].data.buffer[0] == 23:#CC23
	dial_4 = midi[0].data.buffer[0] == 23 and filters.mapRange(midi[0].data.buffer[1], 0, 127, -17873, 17873)
	vJoy[1].dial = dial_4;

#Button S8 CC#39
if (midi[0].data.buffer[0] == 39) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(35,True)  

if (midi[0].data.buffer[0] == 39) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(35,False)

#Button M8 CC#55
if (midi[0].data.buffer[0] == 55) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(34,True)  

if (midi[0].data.buffer[0] == 55) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(34,False)

#Button R8 CC#71
if (midi[0].data.buffer[0] == 71) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(33,True)  

if (midi[0].data.buffer[0] == 71) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(33,False)

# the Korg nanoKontrol2 includes some transport buttons as well so we'll give them some allocations on virtual joystick 1 vJoy[0] as well
# We'll leave virtual joystick button 12 ( vJoy[0].11 ) as a gap to keep the deliniation between trasnport buttons and the slider area clear. In truth, I'm too lazy to fix it now.
# Button last Track CC#58
if (midi[0].data.buffer[0] == 58) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(0,True)  

if (midi[0].data.buffer[0] == 58) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(0,False)

# Button next Track CC#59
if (midi[0].data.buffer[0] == 59) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(1,True)  

if (midi[0].data.buffer[0] == 59) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(1,False)

# Button cycle CC#46
if (midi[0].data.buffer[0] == 46) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(2,True)  

if (midi[0].data.buffer[0] == 46) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(2,False)

# Button set CC#60
if (midi[0].data.buffer[0] == 60) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(3,True)  

if (midi[0].data.buffer[0] == 60) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(3,False)

# Button Left Marker CC#61
if (midi[0].data.buffer[0] == 61) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(4,True)  

if (midi[0].data.buffer[0] == 61) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(4,False)

# Button Right Marker CC#62
if (midi[0].data.buffer[0] == 62) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(5,True)  

if (midi[0].data.buffer[0] == 62) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(5,False)

# Button Rewind CC#43
if (midi[0].data.buffer[0] == 43) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(6,True)  

if (midi[0].data.buffer[0] == 43) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(6,False)

# Button Fast Forward CC#44
if (midi[0].data.buffer[0] == 44) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(7,True)  

if (midi[0].data.buffer[0] == 44) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(7,False)

# Button Stop CC#42
if (midi[0].data.buffer[0] == 42) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(8,True)  

if (midi[0].data.buffer[0] == 42) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(8,False)

# Button Play CC#41
if (midi[0].data.buffer[0] == 41) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(9,True)  

if (midi[0].data.buffer[0] == 41) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(9,False)

# Button Record CC#45
if (midi[0].data.buffer[0] == 45) and (midi[0].data.buffer[1] > 0): 
	vJoy[0].setButton(10,True)  

if (midi[0].data.buffer[0] == 45) and (midi[0].data.buffer[1] < 127):
	vJoy[0].setButton(10,False)



if starting:
	midi[0].update += update