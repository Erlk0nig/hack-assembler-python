# Hack Assembler in Python

## Overview
This project is a Hack assembler written in Python, developed as part of the *Nand2Tetris* course.  
It translates Hack assembly language (`.asm`) programs into Hack machine code (`.hack`), which can be executed on the Hack CPU Emulator.

## Features
- Implements a **two-pass assembler**:
  - **First pass**: resolves labels and symbols.  
  - **Second pass**: generates binary machine code.  
- Supports both **A-instructions** (`@value`) and **C-instructions** (`dest=comp;jump`).  
- Provides built-in support for all predefined Hack symbols (`SP`, `LCL`, `ARG`, `THIS`, `THAT`, `R0–R15`, `SCREEN`, `KBD`).  
- Produces `.hack` files compatible with the official Nand2Tetris tools.  

## Requirements
- Python 3.8 or higher  
- No external dependencies  

## Usage
1. Clone the repository:
   ```bash
   git clone git@github.com:yourusername/hack-assembler-python.git
   cd hack-assembler-python
   ```
2. Run the assembler on an `.asm` file:
   ```bash
   python assembler.py Program.asm
   ```
3. The assembler will generate:
   ```
   Program.hack
   ```

## Project Structure
```
hack-assembler-python/
│── assembler.py     # Entry point of the assembler
│── parser.py        # Parses Hack assembly instructions
│── code.py          # Translates mnemonics into binary
│── symbol_table.py  # Manages symbols and labels
│── README.md
```

## Example
**Input (Add.asm):**
```asm
@2
D=A
@3
D=D+A
@0
M=D
```

**Output (Add.hack):**
```
0000000000000010
1110110000010000
0000000000000011
1110000010010000
0000000000000000
1110001100001000
```

## Acknowledgments
This project is based on the *Elements of Computing Systems* textbook and the [Nand2Tetris course](https://www.nand2tetris.org/) by Noam Nisan and Shimon Schocken.  
