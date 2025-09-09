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

class Code:
    def dest(field):
        # Translate the destination field of the instruction
        match field:
            case "":
                return "000"
            case "M":
                return "001"
            case "D":
                return "010"
            case "DM":
                return "011"
            case "A":
                return "100"
            case "AM":
                return "101"
            case "AD":
                return "110"
            case "ADM":
                return "111"
    
    def comp(field):
            # Translate the computation field of the instruction 
            match field:
                case "0":
                    return "0101010"
                case "1":
                    return "0111111"
                case "-1":
                    return "0111010"
                case "D":
                    return "0001100"
                case "A":
                    return "0110000"
                case "!D":
                    return "0001101"
                case "!A":
                    return "0110001"
                case "-D":
                    return "0001111"
                case "-A":
                    return "0110011"
                case "D+1":
                    return "0011111"
                case "A+1":
                    return "0110111"
                case "D-1":
                    return "0001110"
                case "A-1":
                    return "0110010"
                case "D+A":
                    return "0000010"
                case "D-A":
                    return "0010011"
                case "A-D":
                    return "0000111"
                case "D&A":
                    return "0000000"
                case "D|A":
                    return "0010101"
                case "M":
                    return "1110000"
                case "!M":
                    return "1110001"
                case "-M":
                    return "1110011"
                case "M+1":
                    return "1110111"
                case "M-1":
                    return "1110010"
                case "D+M":
                    return "1000010"
                case "D-M":
                    return "1010011"
                case "M-D":
                    return "1000111"
                case "D&M":
                    return "1000000"
                case "D|M":
                    return "1010101"    
                
    def jump(field):
        match field:
            # Translate the jump field of the instruction 
            case "":
                return "000"
            case "JGT":
                return "001"
            case "JEQ":
                return "010"
            case "JGE":
                return "011"
            case "JLT":
                return "100"
            case "JNE":
                return "101"
            case "JLE":
                return "110"
            case "JMP":
                return "111"


path = Path(argv[1])
parser = Parser(path)
instructions = parser.initializer()
print(instructions)
for instruction in instructions:
    if parser.instruction_type(instruction) == "C-instruction":
        dest = parser.dest(instruction)
        print (Code.dest(dest))





