import vgamepad as vg
from texttoinputcontroller import TextToInputController
from timedtexttoinputcontroller import TimedTextToInputController

gamepad = vg.VX360Gamepad()
virtual_controller = TextToInputController(gamepad)

while True:
    command = input().upper()
    
    if command == "Exit":
        break
    elif command == "Queue Mode":
        virtual_controller = TextToInputController(gamepad)
    elif command == "Timed Mode":
        virtual_controller = TimedTextToInputController(gamepad, 5)
    virtual_controller.text_to_input(command)
