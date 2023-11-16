import os
import twitchio
from twitchio.ext import commands
from texttoinputcontroller import TextToInputController

class Bot(commands.Bot):
    def __init__(self, text_to_input_controller:TextToInputController):
        super().__init__(token = os.getenv('ACCESS_TOKEN'), prefix = os.getenv('PREFIX'), initial_channels = [os.getenv('CHANNEL')])
        self.text_to_input_controller = text_to_input_controller
        self.register_inputs = True

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message: twitchio.Message):
        #ignore bot sent messages 
        if message.echo:
            return
        
        await self.handle_commands(message)
    
        if self.register_inputs:
            await self.parse_inputs(message)
    
    async def parse_inputs(self, message):
        print(f'{message.author.display_name}: {message.content}')
        self.text_to_input_controller.text_to_input(message.content)
    
    @commands.command(name="TurnOnController")
    async def turn_on_input_handling(self, ctx: commands.Context) -> None:
        self.register_inputs = True
        response = "Input handling turned on"
        print(f"{ctx.author}: " + response)
        await ctx.send(response)
    
    @commands.command(name="TurnOffController")
    async def turn_off_input_handling(self, ctx: commands.Context) -> None:
        self.register_inputs = False
        response = "Input handling turned off"
        print(f"{ctx.author}: " + response)
        await ctx.send(response)
    
    # TODO - make this a setter instead of a toggle
    @commands.command(name="ToggleSelectionMode")
    async def toggle_selection_mode(self, ctx: commands.Context) -> None:

        response = f"Toggled command selection mode to {self.text_to_input_controller.get_command_selection_mode().name}"
        print(f"{ctx.author}: " + response)
        await ctx.send(response)