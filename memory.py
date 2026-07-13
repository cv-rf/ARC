# memory.py

class Memory:
    def __init__(self, size=100):
        self._ram = [0] * size

    def read(self, address):
        return self._ram[address]
    
    def write(self, address, value):
        self._ram[address] = value

    def load_program(self, program_code):
        for address, instruction in enumerate(program_code):
            self.write(address, instruction)