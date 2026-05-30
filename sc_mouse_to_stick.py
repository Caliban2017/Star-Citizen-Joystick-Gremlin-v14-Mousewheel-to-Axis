###############################################################################
# Creator:     Caliban86
# GitHub:      https://github.com/Caliban2017/Star-Citizen-Joystick-Gremlin-v14-Mousewheel-to-Axis
# Description: Joystick-to-Mouse movement script for Joystick Gremlin
###############################################################################

import time
import ctypes
import gremlin
from gremlin.user_script import *

axis_x = PhysicalInputVariable(
    "X Axis",
    "Select X Axis",
    False,
    [gremlin.common.InputType.JoystickAxis]
)

axis_y = PhysicalInputVariable(
    "Y Axis",
    "Select Y Axis",
    False,
    [gremlin.common.InputType.JoystickAxis]
)

mode = ModeVariable("Mode", "Mode", False)

speed = FloatVariable("Speed", "Mouse Speed", False, 8.0, 0.1, 50.0)
deadzone = FloatVariable("Deadzone", "Ignore center", False, 0.1, 0.0, 1.0)

current_x = 0.0
current_y = 0.0

decorator_x = axis_x.create_decorator(mode.value)
decorator_y = axis_y.create_decorator(mode.value)

@decorator_x.axis(axis_x.input_id)
def handle_x(event, vjoy):
    global current_x
    current_x = event.value

@decorator_y.axis(axis_y.input_id)
def handle_y(event, vjoy):
    global current_y
    current_y = event.value

@periodic(0.01)
def process_mouse():
    val_x = current_x if abs(current_x) >= deadzone.value else 0.0
    val_y = current_y if abs(current_y) >= deadzone.value else 0.0

    if val_x == 0.0 and val_y == 0.0:
        return

    move_x = int(val_x * speed.value)
    move_y = int(val_y * speed.value)

    if move_x != 0 or move_y != 0:
        ctypes.windll.user32.mouse_event(0x0001, move_x, move_y, 0, 0)