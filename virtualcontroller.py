import vgamepad as vg
import time

class VirtualController():
    button_hold_time = 0.1
    trigger_hold_time = 0.1
    analog_hold_time = 0.5

    xbox360_button_mapping = {
        'A': vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
        'B': vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
        'X': vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
        'Y': vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,
        'UP': vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
        'DOWN': vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
        'LEFT': vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
        'RIGHT': vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
        'START': vg.XUSB_BUTTON.XUSB_GAMEPAD_START,
        'BACK': vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK,
        'L3': vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB,
        'R3': vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB,
        'LB': vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
        'RB': vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,
        #'HOME': vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE,
    }

    xbox360_trigger_mapping = {
        'LT': 255,
        'RT': 255,
    }

    xbox360_left_analog_mapping = {
        'ANALOG L 1': 1,
        'ANALOG L 2': 2,
        'ANALOG L 3': 3,
        'ANALOG L 4': 4,
        'ANALOG L 5': 5,
        'ANALOG L 6': 6,
        'ANALOG L 7': 7,
        'ANALOG L 8': 8,
        'ANALOG L 9': 9,    
    }

    xbox360_righ_analog_mapping = {
        'ANALOG R 1': 1,
        'ANALOG R 2': 2,
        'ANALOG R 3': 3,
        'ANALOG R 4': 4,
        'ANALOG R 5': 5,
        'ANALOG R 6': 6,
        'ANALOG R 7': 7,
        'ANALOG R 8': 8,
        'ANALOG R 9': 9,    
    }

    def __init__(self, virtualGamepad):
        self.virtual_gamepad = virtualGamepad

        #xbox360 is 0 ds4 is 2 
        if self.virtual_gamepad.get_type() == 0: 
            self.buttons = self.xbox360_button_mapping
            self.triggers = self.xbox360_trigger_mapping
            self.left_analog = self.xbox360_left_analog_mapping
            self.right_analog = self.xbox360_righ_analog_mapping
        
        self.valid_inputs = list(self.buttons.keys()) + list(self.triggers.keys()) + list(self.left_analog.keys()) + list(self.right_analog.keys())

    def handle_input(self, input_name:str) -> None:
        if input_name in self.right_analog.keys() or input_name in self.left_analog.keys():
            self.input_analog(input_name)
        elif input_name in self.triggers.keys() : 
            self.input_trigger(input_name)
        elif input_name in self.buttons.keys() :
            self.input_button(input_name)

    def input_analog(self, analog_command) -> None:
        split_command = analog_command.split()
        stick = split_command[1]
        direction = int(split_command[-1])
        x_axis = 0
        y_axis = 0
        match direction:
            case 1:
                x_axis = -1.0
                y_axis = -1.0
            case 2:
                x_axis = 0
                y_axis = -1.0
            case 3:
                x_axis = 1.0
                y_axis = -1.0
            case 4:
                x_axis = -1.0
                y_axis = 0
            case 5: 
                x_axis = 0
                y_axis = 0
            case 6: 
                x_axis = 1.0
                y_axis = 0
            case 7:     
                x_axis = -1.0
                y_axis = 1.0
            case 8:
                x_axis = 0
                y_axis = 1.0
            case 9:
                x_axis = 1.0
                y_axis = 1.0
            case _:
                x_axis = 0
                y_axis = 0 
        if stick == 'R':
            self.virtual_gamepad.right_joystick_float(x_value_float=x_axis, y_value_float=y_axis)
            self.virtual_gamepad.update()
            time.sleep(self.analog_hold_time)
            self.virtual_gamepad.right_joystick_float(x_value_float=0, y_value_float=0)
            self.virtual_gamepad.update()
        elif stick == 'L':
            self.virtual_gamepad.left_joystick_float(x_value_float=x_axis, y_value_float=y_axis)
            self.virtual_gamepad.update()
            time.sleep(self.analog_hold_time)
            self.virtual_gamepad.left_joystick_float(x_value_float=0, y_value_float=0)
            self.virtual_gamepad.update()

    def input_trigger(self, trigger_name) -> None:
        if trigger_name == 'RT':
            self.virtual_gamepad.right_trigger(self.triggers[trigger_name])    
            time.sleep(self.trigger_hold_time) 
            self.virtual_gamepad.right_trigger(0)
            self.virtual_gamepad.update()
        else:
            self.virtual_gamepad.left_trigger(self.triggers[trigger_name])
            self.virtual_gamepad.update()
            self.virtual_gamepad.left_trigger(0)
            self.virtual_gamepad.update()

    def input_button(self, button_name) -> None:
        self.virtual_gamepad.press_button(button=self.buttons[button_name])
        self.virtual_gamepad.update()
        time.sleep(self.button_hold_time)
        self.virtual_gamepad.release_button(button=self.buttons[button_name])
        self.virtual_gamepad.update()