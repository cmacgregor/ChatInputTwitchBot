from dotenv import load_dotenv
import os
from virtualcontroller import VirtualController
import vgamepad as vg
from bot import Bot


def main():
    load_dotenv()
    virtual_controller = VirtualController(vg.VX360Gamepad())
    token = os.getenv('ACCESS_TOKEN')
    prefix = os.getenv('PREFIX')
    initial_channels = [os.getenv('CHANNEL')]
    bot = Bot(token, prefix, initial_channels, virtual_controller)
    bot.run()
    

if __name__ == "__main__":
    main()