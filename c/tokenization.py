import re
import pandas as pd 

def compiler(input_string):
  tokens = re.split(r'(\W)', input_string)
  symbol_table = {}
  address_counter = 0
  current_scope = "global"
  for token in tokens:
    if token.isalpha():
      if token in symbol_table:
        symbol_info = symbol_table[token]
        symbol_info["USED"] = True
        address = symbol_info["ADDRESS"]
        datatype = symbol_info["DATATYPE"]
        value = symbol_info["VALUE"]
      else:
        address = address_counter
        symbol_table[token] = {"DATATYPE": "undefined", "ADDRESS": address, "USED": True, "DEFINED": False, "scope": current_scope, "VALUE": None}
        address_counter += 1
        datatype = "undefined"
        value = None
      print(f"{token} is a variable or constant with address {address}, datatype {datatype}, value {value}, and scope {current_scope}")
    elif token.isdigit():
      address = address_counter
      symbol_table[token] = {"DATATYPE": "number", "ADDRESS": address, "USED": True, "DEFINED": True, "SCOPE": current_scope, "VALUE": token}
      address_counter += 1
      print(f"{token} is a number with address {address}, datatype number, value {token}, and scope {current_scope}")
    elif token in ['+', '-', '*', '/']:
      if token in symbol_table:
        symbol_table[token]["used"] = True
      else:
        symbol_table[token] = {"DATATYPE": "operator", "ADDRESS": None, "USED": True, "DEFINED": True, "SCOPE": "global", "VALUE": token}
      print(f"{token} is an operator with scope global")
    elif token in [';', '{', '}']:
      if token == '{':
        current_scope = "local"
      elif token == '}':
        current_scope = "global"
    else:
      continue
      
  df = pd.DataFrame(symbol_table).T
  df.index.name = "Variable"
  print("\nSymbol table:")
  print(df)

input_string = input("Enter String : ")
compiler(input_string)

# Sample input
a=b; print(hello)
