import re

def check_syntax(file_path):
    if_else_regex = r"if\s*\((?:[^)(]|\((?:[^)(]+|\([^)(]*\))*\))*\)\s*\{(?:[^{}]+|\{(?:[^{}]+|\{[^{}]*\})*\})*\}(?:\s*else\s*\{(?:[^{}]+|\{(?:[^{}]+|\{[^{}]*\})*\})*\})?"
    switch_case_regex = r"switch\s*\([^\)]*\)\s*{(\s*case\s*[^\n]*:\s*[^\n]*\s*break;\s*)+\s*(\s*default:\s*[^\n]*\s*break;\s*)?}"
    with open(file_path, 'r') as file:
        code = file.read()
    if_else_search = re.search(if_else_regex, code)
    switch_case_search = re.search(switch_case_regex, code)
    if not if_else_search:
        print("Invalid syntax: if-else statement is not valid")
    else:
        print("Valid syntax: if-else statement is valid")

    if not switch_case_search:
        print("Invalid syntax: switch-case statement is not valid")
    else:
        print("Valid syntax: switch-case statement is valid")

file_path = "Downloads\example.c"
check_syntax(file_path)

# Sample input
if (x > 10) 
{
    printf("x is greater than 10");
} else {
    printf("x is less than or equal to 10");
}
    switch(x) {
        case 1:
            printf("x is 1");
            break;
        case 2:
            printf("x is 2");
            break;
        default:
            printf("x is neither 1 nor 2");
            break;
    }
}
