from sys import argv
from pathlib import Path

class Parser:
    def __init__(self,path):
        self.path = path

    def initializer(self):
        try:
            with self.path.open(mode="r", encoding="utf-8") as file:
                instructions = []
                # Remove newlines and comments
                for line in file.readlines():
                    if line != "\n":
                        line = line.strip()
                        if line[0] + line [1] != "//":
                            instructions.append(line)
        except FileNotFoundError:
            print("Usage : [command] [assembly file] [hack file]")
        return instructions
        
    def symbol(self,instruction):
            # Return the symbol part of the A-instruction
            return instruction.replace('@','')
    
    def label(self,instruction):
        # Return the lable from the L-instruction
        return instruction.replace('(','').replace(')','')
    
    # Split instructions into A-instructions and C-instructions
    def instruction_type(self,instruction):
        if instruction[0] == '@':
            return "A-instruction"
        elif instruction[0] + instruction[-1] == "()":
            return "L-instruction"
        else:
            return "C-instruction"
        
    def dest(self,instruction):
        # Get the destination field of the instruction
        if len(instruction.split("=")) < 2:
            return ""
        return instruction.split("=")[0]

    def comp(self,instruction):
        # Get the computation field of the instruction
        if len(instruction.split("=")) < 2:
            return instruction.split(";")[0]
        return instruction.split("=")[1].split(";")[0]
    
    def jump(self,instruction):
        # Get the jump field of the instruction
        if len(instruction.split(";")) < 2:
            return ""
        return instruction.split(";")[1]


class Code:
    def __init__(self,dest_field,comp_field,jump_field):
        self.dest_field = dest_field
        self.comp_field = comp_field
        self.jump_field = jump_field
    def dest(self):
        # Translate the destination field of the instruction
        match self.dest_field:
            case "":
                return "000"
            case "M":
                return "001"
            case "D":
                return "010"
            case "MD":
                return "011"
            case "A":
                return "100"
            case "AM":
                return "101"
            case "AD":
                return "110"
            case "ADM":
                return "111"
    
    def comp(self):
            # Translate the computation field of the instruction 
            match self.comp_field:
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
                
    def jump(self):
        match self.jump_field:
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


class SymbolTable:
    def __init__(self):
        self.table = {}
    
    def initializer(self):
        # Initialize the predefined symbols for the symbol table
        predefined_symbols = {
                               "R0": 0,
                               "R1": 1,
                               "R2": 2,
                               "R3": 3, 
                               "R4": 4, 
                               "R5": 5, 
                               "R6": 6, 
                               "R7": 7, 
                               "R8": 8,
                               "R9": 9,
                               "R10": 10,
                               "R11": 11,
                               "R12": 12,
                               "R13": 13,
                               "R14": 14,
                               "R15": 15,
                               "SP": 0,
                               "LCL": 1,
                               "ARG": 2,
                               "THIS": 3,
                               "THAT": 4,
                               "SCREEN": 16384,
                               "KBD": 24576
                              }
        self.table.update(predefined_symbols)
        
    
    def contains(self,symbol):
        # Check if the symbol table contains the specified symbol
        return symbol in self.table
    
    def add_entry(self,address,symbol):
        # Adds entry to the symbol table
        self.table[symbol] = address
        

    def get_address(self,symbol):
        # Get symbol address from the symbol table
        return self.table[symbol]

        
# Select file to translate and store instructions
path = Path(argv[1])
parser = Parser(path)
instructions = parser.initializer()
# First pass
# iterate over instructions
instruction_count = -1
symbol_table = SymbolTable()
symbol_table.initializer()
for instruction in instructions:
    if instruction_count < len(instructions):
        if parser.instruction_type(instruction) != "L-instruction":
            instruction_count += 1
    if parser.instruction_type(instruction) == "L-instruction":
        label = parser.label(instruction)
        contains = symbol_table.contains(label)
        if contains == False:
            symbol_table.add_entry(instruction_count+1,label)
# Second pass
ram = 16 # Initialize ram
translated_instructions = [] # intialize list to store translated instructions
for instruction in instructions:
    if parser.instruction_type(instruction) == "L-instruction":
        continue
     # Split C-instruction into subfields and translate each subfield
    if parser.instruction_type(instruction) == "C-instruction":
        dest = parser.dest(instruction)
        comp = parser.comp(instruction)
        jump = parser.jump(instruction)
        code = Code(dest,comp,jump)
        translated_dest = code.dest()
        translated_comp = code.comp()
        translated_jump = code.jump()
        # Assemble translated subfields
        translated_instruction = f"111{translated_comp}{translated_dest}{translated_jump}"
    if parser.instruction_type(instruction) == "A-instruction":
        # Translate each A-instruction into its binary value
        symbol = parser.symbol(instruction)
        # tranlate the value directly or get the symbols address
        try:
            integer = int(symbol)
        except ValueError:
            contains = symbol_table.contains(symbol)
            if contains == False:
                if ram < 255:
                    # Add variable symbol to symbol table
                    symbol_table.add_entry(ram,symbol)
                    ram += 1
                else:
                    print("Variable space exceeded")
                    exit()
            # Get variable address
            integer = symbol_table.get_address(symbol)
        binary_representation = f'{integer:015b}'
        translated_instruction = f"0{binary_representation}"

    translated_instructions.append(f"{translated_instruction}\n")

# Remove trailing newline
translated_instructions[-1] = translated_instruction
# Select file to store binary output
try:
    with Path(argv[1]).open(mode="w", encoding="utf-8") as file:
        file.writelines(translated_instructions)
except FileNotFoundError:
    print("Usage : [command] [assembly file] [hack file]")

    







