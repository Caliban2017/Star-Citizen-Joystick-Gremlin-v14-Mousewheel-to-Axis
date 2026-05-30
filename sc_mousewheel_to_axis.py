###############################################################################
# Creator:     Caliban86
# GitHub:      https://github.com/Caliban2017/Star-Citizen-Joystick-Gremlin-v14-Mousewheel-to-Axis
# Description: Joystick-to-Mouse movement script for Joystick Gremlin
###############################################################################

import time
import gremlin
from gremlin.user_script import *

axis = PhysicalInputVariable(
    "Axis",
    "Scroll Axis",
    False,
    [gremlin.common.InputType.JoystickAxis]
)

mode = ModeVariable("Mode", "Mode", False)

invert = BoolVariable("Invert", "Reverse", False, False)
scale = FloatVariable("Scale", "Speed Factor", False, 0.8, 0.1, 5.0)
deadzone = FloatVariable("Deadzone", "Ignore center", False, 0.1, 0.0, 1.0)

current_axis_value = 0.0
last_scroll_time = time.time()

decorator = axis.create_decorator(mode.value)

@decorator.axis(axis.input_id)
def axis_handler(event):
    global current_axis_value
    try:
        current_axis_value = event.value
    except AttributeError:
        current_axis_value = event.value


@periodic(0.01)
def process_scroll():
    global last_scroll_time
    
    if abs(current_axis_value) < deadzone.value:
        return

    intensity = (abs(current_axis_value) - deadzone.value) / (1.0 - deadzone.value)
    intensity = max(0.0, min(1.0, intensity))

    max_interval = 0.35 / scale.value
    min_interval = 0.03 / scale.value
    
    min_interval = max(0.025, min_interval)
    
    current_interval = max_interval - (intensity * (max_interval - min_interval))

    now = time.time()
    if now - last_scroll_time >= current_interval:
        direction = 1 if current_axis_value > 0 else -1
        if invert.value:
            direction *= -1
            
        gremlin.sendinput.mouse_wheel(direction)
        last_scroll_time = now