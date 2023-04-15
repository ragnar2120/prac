import re
import pandas as pd 

def compiler(input_string):
  # Tokenize the input string
  tokens = re.split(r'(\W)', input_string)

  # Initialize the symbol table and address counter
  symbol_table = {}
  address_counter = 0

  # Initialize the current scope
  current_scope = "global"

  # Iterate through the tokens
  for token in tokens:
    # Check if the token is a variable or constant
    if token.isalpha():
      # Check if the token is already in the symbol table
      if token in symbol_table:
        # If it is, retrieve its information from the symbol table
        symbol_info = symbol_table[token]
        symbol_info["USED"] = True
        address = symbol_info["ADDRESS"]
        datatype = symbol_info["DATATYPE"]
        value = symbol_info["VALUE"]
      else:
        # If it is not, assign it a new address and add it to the symbol table with default values
        address = address_counter
        symbol_table[token] = {"DATATYPE": "undefined", "ADDRESS": address, "USED": True, "DEFINED": False, "scope": current_scope, "VALUE": None}
        address_counter += 1
        datatype = "undefined"
        value = None
      print(f"{token} is a variable or constant with address {address}, datatype {datatype}, value {value}, and scope {current_scope}")
    # Check if the token is a number
    elif token.isdigit():
      # Assign it a new address and add it to the symbol table with default values
      address = address_counter
      symbol_table[token] = {"DATATYPE": "number", "ADDRESS": address, "USED": True, "DEFINED": True, "SCOPE": current_scope, "VALUE": token}
      address_counter += 1
      print(f"{token} is a number with address {address}, datatype number, value {token}, and scope {current_scope}")
    # Check if the token is an operator
    elif token in ['+', '-', '*', '/']:
      # Check if the operator is already in the symbol table
      if token in symbol_table:
        # If it is, update its "used" field in the symbol table
        symbol_table[token]["used"] = True
      else:
        # If it is not, add it to the symbol table with default values
        symbol_table[token] = {"DATATYPE": "operator", "ADDRESS": None, "USED": True, "DEFINED": True, "SCOPE": "global", "VALUE": token}
      print(f"{token} is an operator with scope global")
    # Check if the token is a separator
    elif token in [';', '{', '}']:
      # Update the current scope if the token is a curly brace
      if token == '{':
        current_scope = "local"
      elif token == '}':
        current_scope = "global"
    # Otherwise, the token is a whitespace, so we ignore it
    else:
      continue

  # Format the symbol table as a table using pandas
  df = pd.DataFrame(symbol_table).T
  df.index.name = "Variable"
  print("\nSymbol table:")
  print(df)

# Test the compiler
input_string = input("Enter String : ")
compiler(input_string)

# Sample input
a=b; print(hello)
