from enum import Enum

class IntCode:
    class State(Enum):
        RUNNING = 1
        TERMINATED = 2

    def __init__(self, memory, pointer=0):
        self.memory_init = memory.copy()
        self.pointer_init = pointer
        self.reset()
        
    def reset(self):
        self.memory = self.memory_init.copy()
        self.pointer = self.pointer_init
        self.state = self.State.RUNNING
        
    def run_single_instruction(self):
        if self.state == self.State.TERMINATED:
            raise Exception("Attempting to run a TERMINATED IntCode process")
        if self.pointer < 0 or self.pointer >= len(self.memory):
            raise Exception("Pointer out of bounds (%d) for memory of length %d" % (self.pointer,len(self.memory)))
        
        opcode = self.memory[self.pointer]
        params = []
        if( opcode == 1 ):
            # Add
            params.append(self.memory[self.pointer+1])
            params.append(self.memory[self.pointer+2])
            params.append(self.memory[self.pointer+3])
            self.memory[params[2]] = self.memory[params[0]] + self.memory[params[1]]
        elif( opcode == 2 ):
            # Mult
            params.append(self.memory[self.pointer+1])
            params.append(self.memory[self.pointer+2])
            params.append(self.memory[self.pointer+3])
            self.memory[params[2]] = self.memory[params[0]] * self.memory[params[1]]
        elif( opcode == 99 ):
            # End
            self.state = self.State.TERMINATED
        else:
            raise Exception("Illegal opcode %d" % opcode)
            
        self.pointer += 1 + len(params) # 1 for the opcode and n for the params if applicable.
        
    def run(self):
        while self.state == self.State.RUNNING:
            self.run_single_instruction()
