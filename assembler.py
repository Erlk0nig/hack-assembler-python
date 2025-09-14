from parser import Parser
from code import Code
from symbol_table import SymbolTable
from sys import argv
from pathlib import Path

if __name__ == "__main__":        
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
                    if ram < 256:
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
    try :
        output_file = f"{argv[1].split('/')[-1].split('.')[0]}.hack"
    except:
        output_file = f"{argv[1].split('.')[0]}.hack"
    with Path(output_file).open(mode="w", encoding="utf-8") as file:
        file.writelines(translated_instructions)


    







