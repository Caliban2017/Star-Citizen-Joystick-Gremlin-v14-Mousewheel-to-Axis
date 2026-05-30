# Star-Citizen-Joystick-Gremlin-v14-Mousewheel-to-Axis

# Description:
This two Action-Scripts a created to use an Axis on a Joystick/Hotas for the Distance of the Tractor-Beam in Star Citizen. The sc_mousewheel_to_axis.py File is able to bind an Axis to the Mousewheel-Scroll. So you can use slow movements for the Tractor-Beam and fast movements, depending on the Axis Input. The Second File, the sc_mouse_to_stick.py can be used to bind an Analog-Stick, for example the Finger-Stick on the TWSC T.16000M Throttle. In combination with another rebinded Button, which holds the R-Button on the Keyboard, you can move the Mouse with an Analog-Stick and you are able to rotate the Boxes on the Tractor-Beam with your Finger-Stick.

It is recommended you create a separate Profile for the Tractor-Beam. You can use a free Button of your Choice to toggle trough the Profiles. Otherwise this Script may get in conflict with your other Keybinds. To create a new Profile, just go to Tools -> Manage Modes -> Add Mode. Call it for Example "Tractor" and after you created it, you can select your Default-Profile in the right Drop-Down box to inherit all Keybinds from your Default-Profile.

# Install:

1. Download the sc_mousewheel_to_axis.py and/or the sc_mouse_to_stick.py in put it in a Folder of your Choice.

2. start Joystick Gremlin v14, go to Settings and choose Global. Choose as Plugin directory, where your mousewheel.py is locatet.

3. Click on "Scripts" on the Top Right of the Main-Window. Click "Add Script" and choose one of the two .py Files.

4. It should be listet as Instance 1. Click the Edit Button (middle of the three Icons on the right side).

5. For the sc_mousewheel_to_axis.py:
     On Axis click on "No Input" and then press the Axis you want to use of your Joystick. 
   
6. For the sc_mouse_to_stick.py:
     Same for the Mouse.py, set a X-Axis and a Y Axis and choose your Tractor or Mainprofile.

7. On Mode you can select in which Profile it will be active. Choose your Tractor-Profile here.

# Additional Settings:

With Invert you can of course invert your Axis.

Scale sets the Speed of your Mousewheel. It is only usable for the minimum speed of the Wheelscroll. The Maximum Amount is limited by Joystick Gremlin and can not go faster, otherweise the Script will cause an Overflow and stop the Scrolling.

Deadzone is of course to prevent movings on the Zeropoint of the AXis.

Speed is to set the Mousemovement Speed.
