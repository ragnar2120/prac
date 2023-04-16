opcodes = {
    "DS": "000",
    "INP": "001",
    "LOD": "010",
    "ADD": "011",
    "STO": "100",
    "OUT": "101",
    "RST": "111"
}

def perform_operation(instruction, registers):
    parts = instruction.split()
    op, *operands = parts
    if op not in opcodes:
        return None
    if op == "DS":
        registers[operands[0]] = None
    elif op == "INP":
        registers[operands[0]] = int(input(f"Enter {operands[0]}: "))
    elif op == "LOD":
        registers["ACC"] = registers[operands[0]]
    elif op == "ADD":
        registers["ACC"] += registers[operands[0]]
    elif op == "STO":
        registers[operands[0]] = registers["ACC"]
    elif op == "OUT":
        print("Total :",registers[operands[0]])
    elif op == "RST":
        registers["ACC"] = 0
    return registers

registers = {"ACC": 0}
instructions = [
    "DS A",
    "DS B",
    "INP A",
    "INP B",
    "LOD A",
    "ADD B",
    "STO C",
    "OUT C",
    "DS C",
    "RST"
]

for instruction in instructions:
    result = perform_operation(instruction, registers)
    if result:
        registers = result
    else:
        print("Invalid instruction:", instruction)
