from dotenv import load_dotenv
from texttoinputcontroller import TextToInputController
import vgamepad as vg
from bot import Bot


def main():
    load_dotenv()
    virtual_controller = TextToInputController(vg.VX360Gamepad())
    bot = Bot(virtual_controller)
    bot.run()
    

if __name__ == "__main__":
    main()