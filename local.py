from dotenv import load_dotenv
from texttoinputcontroller import TextToInputController
import vgamepad as vg

virtual_controller = TextToInputController(vg.VX360Gamepad())

while True:
    command = input().upper()
    
    if command == "Exit":
        break

    virtual_controller.text_to_input(command)
