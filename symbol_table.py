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
