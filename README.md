# MIDI_to_FreePIE_to_vJoy
#A small project so I can use a Korg NanoKontrol2 as a joystick input for games like Artemis Starship Bridge Simulator, Space-Nerds-In-Space or anything that would benefit from a bunch of slider or dial controls

# This is a work in progress and to hell with your warranty!
# I wanted to use a Korg nanoKontrol2 as a joystick. Why? 'Cause buttons, dials & sliders for cheaper ($80 CDN).
# This: http://www.korg.com/caen/products/computergear/nanokontrol2/
# To make this work we need to monitor the midi from the nanoKontrol2 and convert them in real time to a joystick output.
# We can do that with FreePIE (Programmable Input Emulator): http://andersmalmgren.github.io/FreePIE/
# FreePIE converts that to an output for a virtual joystick.
# For this we're using vJoy: http://vjoystick.sourceforge.net/site/
# vJoy only supports a limited number of axis which we want to use as sliders/dials and other inputs to games.
# To make this all work, we're going to have to split layout of the nanoKontrol2 into multiple virtual joysticks.
# To make this all work, we're going to have to split layout of the nanoKontrol2 into multiple virtual joysticks.
# 4 dials and 4 sliders on the left as a joystick (with some buttons?), 4 dials and 4 sliders on the right as a second joystick (with some buttons?).
# A 3rd joystick could be used for all the "transport" buttons (forward, back, play, record, next track, etc).
# All of this was coded in a brute force way because I am a noob at this.

# Install vJoy.
# Install FreePIE.
# Copy and past this code into FreePIE. Save it as a script, then press run. If it all works, you should be able to monitor the joystick outuput with vJoy's monitor program.
# So far this only a 3rd of the input buttons on the nanoKontrol2. Its late, and I should not be doing this.
