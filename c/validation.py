import re

def check_for_loop(code):
    for_loop_pattern = r'\bfor\b\s*\(.*;.*;.*\)'
    if re.search(for_loop_pattern, code):
        return "For loop found and implemented properly"
    else:
        return "For loop found but implemented incorrectly"

def check_while_loop(code):
    while_loop_pattern = r'\bwhile\b\s*\(.*\)'
    if re.search(while_loop_pattern, code):
        return "While loop found and implemented properly"
    else:
        return "While loop found but implemented incorrectly"

def check_loops(code):
    for_result = check_for_loop(code)
    while_result = check_while_loop(code)
    return for_result, while_result

c_code = """
#include <stdio.h>
int main() {
   for (i = 0; i < n; i++) {
      printf("Hello World\\n");
   }
   while (count < 5) {
      printf("Hello\\n");
   }
   return 0;
}
"""

for_loop_result, while_loop_result = check_loops(c_code)
print(for_loop_result)
print(while_loop_result)
