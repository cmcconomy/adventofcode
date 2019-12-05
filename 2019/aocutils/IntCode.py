from enum import Enum

class ParamMode(Enum):
    POSITION=0
    IMMEDIATE=1

# Day 5 variant
class OpCode:
    def __init__(self,compound_opcode):
        # print("Parsing opcode of %d" % compound_opcode)
        self.param_modes = [ParamMode.POSITION,ParamMode.POSITION,ParamMode.POSITION]
        if( compound_opcode < 100 ):
            self.code = compound_opcode
        else:
            opcode_str = str(compound_opcode)
            self.code = int(opcode_str[-2:])
            # Assuming max 3 param codes
            for i in range(0,3):
                if len(opcode_str) > i+2:
                    opstr_pos = -3 - i;
                    self.param_modes[i] = ParamMode(int(opcode_str[opstr_pos]))
                    # print("i=%d, strpos=%d, val=%s"%(i,opstr_pos,self.param_modes[i]))

        # print( "Converted %d --> %s" % (compound_opcode, self))
    
    def __str__(self):
        return "%d%s" % (self.code,self.param_modes)


class IntCode5:
    class State(Enum):
        RUNNING = 1
        TERMINATED = 2

    def __init__(self, memory, pointer=0, prog_input=None, prog_output=None):
        self.memory_init = memory.copy()
        self.pointer_init = pointer
        self.input = prog_input # Added on Day 5
        self.output = prog_output # Added on Day 5
        self.reset()
        
    def reset(self):
        self.memory = self.memory_init.copy()
        self.pointer = self.pointer_init
        self.state = self.State.RUNNING

    def get_value(self,param,param_mode):
        if( param_mode == ParamMode.POSITION ):
            return self.memory[param]
        elif( param_mode == ParamMode.IMMEDIATE ):
            return param

    def run_single_instruction(self):
        if self.state == self.State.TERMINATED:
            raise Exception("Attempting to run a TERMINATED IntCode process")
        if self.pointer < 0 or self.pointer >= len(self.memory):
            raise Exception("Pointer out of bounds (%d) for memory of length %d" % (self.pointer,len(self.memory)))
        
        opcode = OpCode(self.memory[self.pointer])
        # print( "Pointer %d, opcode %s" % (self.pointer,opcode))

        params = []
        if( opcode.code == 1 ):
            # Add
            params.append(self.memory[self.pointer+1])
            params.append(self.memory[self.pointer+2])
            params.append(self.memory[self.pointer+3])
            # print("> Set pos %d to value of %d + %d" % (params[2],self.get_value(params[0],opcode.param_modes[0]),self.get_value(params[1],opcode.param_modes[1])))
            self.memory[params[2]] = self.get_value(params[0],opcode.param_modes[0]) + \
                                     self.get_value(params[1],opcode.param_modes[1])
        elif( opcode.code == 2 ):
            # Mult
            params.append(self.memory[self.pointer+1])
            params.append(self.memory[self.pointer+2])
            params.append(self.memory[self.pointer+3])
            self.memory[params[2]] = self.get_value(params[0],opcode.param_modes[0]) * \
                                     self.get_value(params[1],opcode.param_modes[1])
        elif( opcode.code == 3 ):
            # input
            program_input = int(input("Please enter the ID of the system to test: "))
            params.append(self.memory[self.pointer+1])
            self.memory[params[0]] = program_input
        elif( opcode.code == 4 ):
            # output
            params.append(self.memory[self.pointer+1])
            program_output = self.memory[params[0]]
            print("Diagnostic test output: %d" % program_output)
        elif( opcode.code == 99 ):
            # End
            self.state = self.State.TERMINATED
        else:
            raise Exception("Illegal opcode %d" % opcode)
            
        self.pointer += 1 + len(params) # 1 for the opcode and n for the params if applicable.
        
    def run(self):
        while self.state == self.State.RUNNING:
            self.run_single_instruction()


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
