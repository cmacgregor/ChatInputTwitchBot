import time
import vgamepad as vg
from virtualcontrollerinputs import VirtualControllerInputs
from xbox360controllerinputs import Xbox360ControllerInputs
from commandselectionmodes import CommnadSelectionModes
    
BUTTON_HOLD_TIME = 0.1
TRIGGER_HOLD_TIME = 0.1
ANALOG_HOLD_TIME = 0.5

class TextToInputController():

    def __init__(self, virtualGamepad:vg):
        self.virtual_gamepad = virtualGamepad

        #xbox360 is 0 ds4 is 2 
        if self.virtual_gamepad.get_type() == 0: 
            self.set_input_mapping(Xbox360ControllerInputs())
    
    def text_to_input(self, text:str) -> None:
        inputs = text.upper().split(", ")

        #process inputs but throw them all out if we encounter something we don't recognize
        for input in inputs:
            if input in self.controller_inputs.inputs:
                #set the controller state
                if input in self.controller_inputs.right_analog.keys() or input in self.controller_inputs.left_analog.keys():
                    self.set_analog(input)
                elif input in self.controller_inputs.triggers.keys() : 
                    self.set_trigger(input)
                elif input in self.controller_inputs.buttons.keys() :
                    self.set_button(input)
            else:
                self.virtual_gamepad.reset()
                self.virtual_gamepad.update()
                break
              
        #hold controller input for game to register inputs
        time.sleep(BUTTON_HOLD_TIME)

        #reset controller for next input
        self.virtual_gamepad.reset()
        self.virtual_gamepad.update()

    # TODO - rework this to not include a large switch statement
    def set_analog(self, analog_command) -> None:
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
        elif stick == 'L':
            self.virtual_gamepad.left_joystick_float(x_value_float=x_axis, y_value_float=y_axis)
            self.virtual_gamepad.update()

    def set_trigger(self, trigger_name) -> None:
        if trigger_name == 'RT':
            self.virtual_gamepad.right_trigger(self.controller_inputs.triggers[trigger_name])    
            self.virtual_gamepad.update()
        else:
            self.virtual_gamepad.left_trigger(self.controller_inputs.triggers[trigger_name])
            self.virtual_gamepad.update()

    def set_button(self, button_name) -> None:
        self.virtual_gamepad.press_button(button=self.controller_inputs.buttons[button_name])
        self.virtual_gamepad.update()
   
    def set_input_mapping(self, input_mapping:VirtualControllerInputs):
        self.controller_inputs = input_mapping