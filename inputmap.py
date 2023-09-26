import vgamepad as vg

class InputMap():
    def __init__(self, isXbox360Controller):
        if isXbox360Controller: 
            self.button_map = self.xbox360_button_mapping
            self.trigger_map = self.xbox360_trigger_mapping
            self.left_analog_map = self.xbox360_left_analog_mapping
            self.right_analog_map = self.xbox360_righ_analog_mapping
        
        self.valid_inputs = self.button_map.keys() + self.trigger_map.keys() + self.left_analog_map.keys() + self.right_analog_map.keys() 

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
