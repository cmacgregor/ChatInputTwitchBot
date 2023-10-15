from twitchio.ext import commands
from enum import Enum
class CommnadSelectionMode(Enum):
    Queue = 1
    Bucket = 2 

class Bot(commands.Bot):
    def __init__(self, token, prefix, initial_channels, virtual_controller, ):
        super().__init__(token, prefix, initial_channels)
        self.virtual_controller = virtual_controller
        self.command_selection_mode = CommnadSelectionMode.Queue
        self.register_inputs = False

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        #ignore bot sent messages
        if message.echo:
            return

        if(self.register_inputs):
            self.parse_input(message.content)

        await self.handle_commands(message)
    
    def parse_inputs(self, message):
        print(f'{message.author.display_name}: {message.content}')
        input_name =  message.content.upper().strip()

        if self.command_selection_mode == CommnadSelectionMode.Queue:
            self.handle_queue_command_node(input_name)
        if self.command_selection_mode == CommnadSelectionMode.Bucket:
            self.handle_bucket_command_mode(input_name)    
        
    def handle_queue_command_node(self, input_name):
        if input_name in self.virtual_controller.valid_inputs:
                self.virtual_controller.handle_input(input_name)

    def handle_bucket_command_mode(self, input_name):
        print(f"TODO - process input name: {input_name} ")
        
    async def toggle_command_selection_mode(self):
        self.command_selection_mode = CommnadSelectionMode.Bucket if self.command_selection_mode == CommnadSelectionMode.Queue else CommnadSelectionMode.Bucket

    async def get_command_selection_mode(self):
        return self.command_selection_mode
    
    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')
    
    async def turn_on_input_handling(self, ctx: commands.Context):
        self.register_inputs = True
        await ctx.send("Input handling is now on")
    
    async def turn_off_input_handling(self, ctx: commands.Context):
        self.register_inputs = False
        await ctx.send("Input handling has been turned off")
    
    async def toggle_command_selection_mode(self, ctx: commands.Context):
        #pass mode type here
        await self.toggle_command_selection_mode()
        await ctx.send(f'Toggled command selection mode to {self.get_command_selection_mode()}')