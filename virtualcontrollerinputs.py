class VirtualControllerInputs: 
    def __init__(self) -> None:
        self.inputs = list()

    def add_valid_inputs(self, command_list) -> None:
        #TODO - Create tests and guards around this
        self.inputs = self.inputs + list(command_list)

    def remove_valid_inputs(self, command_list) -> None:
        #TODO - Create tests around this
        new_inputs = [i for i in self.inputs if i not in command_list]
        self.inputs = new_inputs
