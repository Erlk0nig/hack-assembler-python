from sys import argv
from pathlib import Path

class Parser:
    innstruction_count = 0

    def __init__(self,path):
        self.path = path

    def initializer(self):
        with self.path.open(mode="r", encoding="utf-8") as file:
            instructions = []
            # Remove newlines and comments
            for line in file.readlines():
                if line != "\n":
                    if line[0] + line [1] != "//":
                        line = line.rstrip()
                        instructions.append(line)
            return instructions
    
    def has_more_lines(instructions,instruction_count):
        # Check if there are more instructions in the file
        if instruction_count < len(instructions):
            return True
        
    def advance(self,instruction_count):
        # Fetch the next instruction
        if self.has_more_lines() is True:
            instruction_count += 1
    
    # Split instructions into A-instructions and C-instructions
    def instruction_type(self,instruction):
        if instruction[0] == '@':
            return "A-instruction"
        else:
            return "C-instruction"
        
    def dest(self,instruction):
        # Get the destination field of the instruction
        return instruction.split("=")[0]

    def comp(self,instruction):
        # Get the computation field of the instruction
        return instruction.split("=")[1].split(";")[0]
    
    def jump(self,instruction):
        # Get the jump field of the instruction
        return instruction.split(";")[1]

    

path = Path(argv[1])
parser = Parser(path)
instructions = parser.initializer()
print(instructions)

for instruction in instructions:
    if parser.instruction_type(instruction) == "C-instruction":
        print(parser.comp(instruction))





