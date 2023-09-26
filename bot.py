from dotenv import load_dotenv
import os
import time
from twitchio.ext import commands
import vgamepad as vg
from inputmap import InputMap

class Bot(commands.Bot):
    def __init__(self, gamepad, inputmap):
        super().__init__(token=os.getenv('ACCESS_TOKEN'), prefix=os.getenv('PREFIX'), initial_channels=[os.getenv('CHANNEL')])
        self.virtualgamepad = gamepad
        self.inputmap = inputmap

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        #ignore bot sent messages
        if message.echo:
            return

        if message.content.upper().trim() in self.inputmap.valid_inputs:
            print(f'{message.author.display_name}: {message.content}')

            if message.content.upper() in self.inputmap.right_analog_map.keys() or message.content.upper() in self.inputmap.left_analog_map.keys():
                self.input_analog(message.content.upper())
            elif message.content.uppper() in self.inputmap.trigger_map.keys() : 
                self.input_trigger(message.content.upper())
            elif message.content.upper() in self.inputmap.button_map.keys() :
                self.input_button(message.content.upper())

        await self.handle_commands(message)

    #input handling should be split into another class that combines concerns with controller type and inputing to the virtual controller
    #this will allow the bot to only worry about if a command is valid for the controller
    def input_analog(self, analog_command) -> None:
        stick = analog_command[1]
        direction = analog_command[-1]
        x_axis = 0
        y_axes = 0
        match direction:
            case 1:
                x_axis = -32768
                y_axes = -32768
            case 2:
                x_axis = 0
                y_axes = -32768
            case 3:
                x_axis = 32768
                y_axes = -32768
            case 4:
                x_axis = -32768
                y_axes = 0
            case 5: 
                x_axis = 0
                y_axes = 0
            case 6: 
                
            case _:
                x_axis = 0
                y_axes = 0 

    def input_trigger(self, trigger_name) -> None:
        if trigger_name == 'RT':
            self.virtualgamepad.right_trigger(value=255)     
        else:
            self.virtualgamepad.left_trigger(value=255)
        self.virtualgamepad.update()
        time.sleep(0.5)
        if trigger_name == 'RT':
            self.virtualgamepad.right_trigger(0)
        else:
            self.virtualgamepad.left_trigger(0)
        self.virtualgamepad.update()

    def input_button(self, button_name) -> None:
        self.virtualgamepad.press_button(button=self.input_mapping[button_name])
        self.virtualgamepad.update()
        time.sleep(0.5)
        self.virtualgamepad.release_button(button=self.input_mapping[button_name])
        self.virtualgamepad.update()
        
    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')

load_dotenv()
input_map = InputMap(True)
bot = Bot(vg.VX360Gamepad(), input_map)
bot.run()