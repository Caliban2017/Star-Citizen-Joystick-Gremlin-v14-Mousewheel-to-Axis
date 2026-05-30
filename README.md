# Star-Citizen-Joystick-Gremlin-v14-Mousewheel-to-Axis

# Description:
These two action scripts were created to use an axis on a joystick/HOTAS to control the distance of the tractor beam in Star Citizen. The sc_mousewheel_to_axis.py file allows you to bind an axis to the mouse wheel scroll. This enables you to perform both slow and fast movements for the tractor beam, depending on the axis input. The second file, sc_mouse_to_stick.py, can be used to map an analog stick, such as the mini-stick on the TWCS T.16000M Throttle. In combination with another rebinded button that holds down the "R" key on the keyboard, you can move the mouse with an analog stick and easily rotate boxes on the tractor beam with your finger stick.

It is recommended to create a separate profile for the tractor beam. You can use a free button of your choice to toggle through the profiles. Otherwise, this script may conflict with your other keybinds. To create a new profile, simply go to Tools -> Manage Modes -> Add Mode. For example, call it "Tractor". After creating it, you can select your default profile in the right drop-down box to inherit all keybinds from your default profile.

# Install:

1. Download sc_mousewheel_to_axis.py and/or sc_mouse_to_stick.py and put them into a folder of your choice.

2. Start Joystick Gremlin v14, go to Settings and choose Global. For the Plugin directory, choose the folder where your python scripts are located.

3. Click on "Scripts" in the top right of the main window. Click "Add Script" and choose one of the two .py files.

4. It should be listed as Instance 1. Click the Edit button (the middle of the three icons on the right side).

5. For sc_mousewheel_to_axis.py:
     Click on "No Input" next to Axis and then move the axis on your joystick that you want to use. 
   
6. For sc_mouse_to_stick.py:
     Same as the mouse script: set an X-Axis and a Y-Axis, and choose either your Tractor or Main profile.

7. Under Mode, you can select in which profile the script will be active. Choose your Tractor profile here.

![Readme Screenshot](https://github.com/Caliban2017/Star-Citizen-Joystick-Gremlin-v14-Mousewheel-to-Axis/blob/main/readme1.png?raw=true)

# Additional Settings:

With Invert, you can of course invert your axis.

Scale sets the speed of your mouse wheel scrolling. It only affects the minimum speed of the wheel scroll. The maximum amount is limited by Joystick Gremlin and cannot go faster; otherwise, the script will cause an overflow and stop scrolling.

Deadzone is, of course, used to prevent movement around the center point of the axis.

Speed is used to set the mouse movement speed.
