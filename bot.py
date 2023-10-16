from twitchio.ext import commands
import os
from enum import Enum

class CommnadSelectionMode(Enum):
    Queue = 1
    Bucket = 2 

class Bot(commands.Bot):
    def __init__(self, virtual_controller):
        super().__init__(token = os.getenv('ACCESS_TOKEN'), prefix = os.getenv('PREFIX'), initial_channels = [os.getenv('CHANNEL')])
        self.virtual_controller = virtual_controller
        self.command_selection_mode = CommnadSelectionMode.Queue
        self.register_inputs = True

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        #ignore bot sent messages 
        if message.echo:
            return
        
        await self.handle_commands(message)
    
        if self.register_inputs:
            self.parse_inputs(message)
    
    
    def parse_inputs(self, message):
        print(f'{message.author.display_name}: {message.content}')
        if self.command_selection_mode == CommnadSelectionMode.Queue:
            self.handle_queue_command_node(message.content)
        if self.command_selection_mode == CommnadSelectionMode.Bucket:
            self.handle_bucket_command_mode(message.content)    
        
    def handle_queue_command_node(self, text):
        self.virtual_controller.text_to_input(text)

    def handle_bucket_command_mode(self, input_name):
        print(f"TODO - process input name: {input_name} ")
        
    def toggle_command_selection_mode(self):
        self.command_selection_mode = CommnadSelectionMode.Bucket if self.command_selection_mode == CommnadSelectionMode.Queue else CommnadSelectionMode.Queue

    def get_command_selection_mode(self):
        return self.command_selection_mode
    
    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')
    
    @commands.command(name="TurnOnController")
    async def turn_on_input_handling(self, ctx: commands.Context) -> None:
        self.register_inputs = True
        print(f"Input handling turned on by {ctx.author}")
        await ctx.send("Input handling is now on")
    
    @commands.command(name="TurnOffController")
    async def turn_off_input_handling(self, ctx: commands.Context) -> None:
        self.register_inputs = False
        print(f"Input handling turned off by {ctx.author}")
        await ctx.send("Input handling has been turned off")
    
    @commands.command(name="ToggleSelectionMode")
    async def toggle_selection_mode(self, ctx: commands.Context) -> None:
        self.toggle_command_selection_mode()
        print(f"Selection mode toggled to {self.get_command_selection_mode().name}  by {ctx.author}")
        await ctx.send(f'Toggled command selection mode to {self.get_command_selection_mode().name}')