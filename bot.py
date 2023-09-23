from dotenv import load_dotenv
import os
import time
from twitchio.ext import commands
import vgamepad as vg

from fetchtoken import fetch_oath_access_token

xbox360_button_mapping = {
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
    'A': vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
    'B': vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
    'X': vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
    'Y': vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,
}

class Bot(commands.Bot):
    def __init__(self, gamepad, input_map):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=os.getenv('ACCESS_TOKEN'), prefix=os.getenv('PREFIX'), initial_channels=[os.getenv('CHANNEL')])
        self.virtualgamepad = gamepad
        self.input_mapping = input_map

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        #ignore bot sent messages
        if message.echo:
            return

        if message.content.upper() in self.input_mapping.keys() :
            print(f'{message.author.display_name}: {message.content}')
            self.input_button(self.input_mapping[message.content.upper()])

        await self.handle_commands(message)

    def input_button(self, pressedButton) -> None:
        self.virtualgamepad.press_button(button=pressedButton)
        self.virtualgamepad.update()
        time.sleep(0.5)
        self.virtualgamepad.release_button(pressedButton)
        self.virtualgamepad.update()
        
    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')

load_dotenv()
bot = Bot(vg.VX360Gamepad(), xbox360_button_mapping)
bot.run()