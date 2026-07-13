# cpu.py

class CPU:
    def __init__(self, memory):
        self.memory = memory
        self.pc = 0
        self.acc = 0
        self.running = False

    def fetch(self):
        instruction = self.memory.read(self.pc)
        print(f"FETCH: PC=[{self.pc}] -> Instruction {instruction}")
        self.pc += 1
        return instruction
    
    def decode_and_execute(self, instruction):
        opcode = instruction // 100
        operand = instruction % 100

        if opcode == 1: # LOAD
            self.acc = self.memory.read(operand)
            print(f"EXEC:   LOAD value {self.acc} from address {operand} into ACC")
        
        elif opcode == 2: # ADD
            value = self.memory.read(operand)
            self.acc += value
            print(f"EXEC:   ADD value {value} from address {operand} to ACC (ACC is now {self.acc})")

        elif opcode == 3: # STORE
            self.memory.write(operand, self.acc)
            print(f"EXEC:   STORE ACC ({self.acc}) into address {operand}")

        elif opcode == 4: # SUBTRACT
            value = self.memory.read(operand)
            self.acc -= value
            print(f"EXEC:   SUBTRACT value {value} from address {operand} (ACC is now {self.acc})")
        
        elif opcode == 5: # JUMP_IF_ZERO
            if self.acc == 0:
                self.pc = operand
                print(f"EXEC:   JUMP_IF_ZERO triggered. Moving PC to address {operand}")
            else:
                print(f"EXEC:   JUMP_IF_ZERO ignored (ACC is {self.acc})")

        elif opcode == 6: # JUMP
            self.pc = operand
            print(f"EXEC:   JUMP unconditionally to address {operand}")

        elif opcode == 9: # HALT
            self.running = False
            print("EXEC:    HALT. Shutting down CPU.")

        else:
            print(f"ERROR: Unknown opcode: {opcode}! Halting.")
            self.running = False

    def run(self):
        self.running = True
        while self.running:
            instruction = self.fetch()
            self.decode_and_execute(instruction)
        print(f"Final Accumulator State: {self.acc}")