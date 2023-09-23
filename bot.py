import time
from twitchio.ext import commands
import vgamepad as vg

class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token='ACCESS_TOKEN', prefix='?', initial_channels=['...'])
        self.virtualgamepad = vg.VX360Gamepad()

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        #ignore bot sent messages
        if message.echo:
            return

        if message.content == 'A':
            self.virtualgamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            self.virtualgamepad.update()
            time.sleep(0.5)
            self.virtualgamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            self.virtualgamepad.update()

        print(message.content)

        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')


bot = Bot()
bot.run()