# parser.py

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

