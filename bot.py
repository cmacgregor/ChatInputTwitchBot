from dotenv import load_dotenv
import os
from twitchio.ext import commands
from virtualcontroller import VirtualController
import vgamepad as vg

class Bot(commands.Bot):
    def __init__(self, virtual_controller):
        super().__init__(token=os.getenv('ACCESS_TOKEN'), prefix=os.getenv('PREFIX'), initial_channels=[os.getenv('CHANNEL')])
        self.virtual_controller = virtual_controller

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        #ignore bot sent messages
        if message.echo:
            return

        input_name =  message.content.upper().strip()
        if input_name in self.virtual_controller.valid_inputs:
            print(f'{message.author.display_name}: {message.content}')
            self.virtual_controller.handle_input(input_name)

        await self.handle_commands(message)
        
    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')

load_dotenv()
virtual_controller = VirtualController(vg.VX360Gamepad())
bot = Bot(virtual_controller)
bot.run()