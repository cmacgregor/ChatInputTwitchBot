import vgamepad as vg
from texttoinputcontroller import TextToInputController


class TimedTextToInputController(TextToInputController):
    def __init__(self, virtualGamepad:vg, input_interval:int, ):
        self.inputs_received = {}
        self.set_command_processing_time_window(input_interval)
        TextToInputController.__init__(virtualGamepad)

    def set_command_processing_time_window(input_interval:int) -> None:
        #update scheduled task to run at new interval
        return 