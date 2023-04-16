import re

def generate_intermediate_code(expression):
    expression = re.sub(r"\s+", "", expression)
    temp_counter = 1
    triples = []
    quadruples = []

    while "(" in expression:
        index_start = expression.index("(")
        index_end = expression.index(")")
        sub_expression = expression[index_start+1:index_end]
        sub_result = generate_expression(sub_expression, temp_counter, triples, quadruples)
        expression = expression[:index_start] + f"T{sub_result}" + expression[index_end+1:]
        temp_counter = sub_result + 1

    final_result = generate_expression(expression, temp_counter, triples, quadruples)
    
    print("Three-address code:")
    for tac in triples:
        print(tac)
        
    print("\nTriples:")
    for i, triple in enumerate(triples, start=1):
        print(f"{i}: {triple}")
        
    print("\nQuadruples:")
    for quad in quadruples:
        print(quad)

def generate_expression(expr, temp_counter, triples, quadruples):
    operators = re.findall(r"[+\-*/]", expr)
    operands = re.findall(r"\w+", expr)
    index = temp_counter

    for op, left, right in zip(operators, operands[:-1], operands[1:]):
        tac = f"T{index} = {left} {op} {right}"
        triple = f"({op}, {left}, {right}, T{index})"
        quad = f"({op}, {left}, {right}, T{index})"
        triples.append(tac)
        quadruples.append(quad)
        index += 1
        operands[operands.index(right)] = f"T{index-1}"

    return index - 1

# Test with a simple arithmetic expression
expression = "(a + b) * (c - d) / e"
generate_intermediate_code(expression)
