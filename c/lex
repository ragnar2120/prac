Commadn to run :
nano filename.l
lex filename.l (sudo apt-get install flex)
gcc lex.yy.c -ll
./a/out
----------------------
# Accept all digits 0 to 9
%{
#include <stdio.h>
%}

DIGIT [0-9]

%%

{DIGIT}+ {
    printf("Found digit: %s\n", yytext);
}

.|\n {
    /* ignore everything else */
}

%%

int main() {
    yylex();
    return 0;
}
----------------------
# Accept all that start with 0 and end with 0
%{
#include <stdio.h>
%}

%%
0.*0 { printf("Valid string: %s\n", yytext); }
.|\n { /* ignore all other characters */ }
%%

int main(void) {
    yylex();
    return 0;
}
------------------
# keywords - if else for
%{
#include <stdio.h>
%}

%%

if { printf("Found keyword 'if'\n"); }
else { printf("Found keyword 'else'\n"); }
for { printf("Found keyword 'for'\n"); }

%%

int main(void) {
    yylex();
    return 0;
}
-------------------
# Accept 1 or 0
%{
#include <stdio.h>
%}

%%

[01] { printf("Valid character: %s\n", yytext); }
.|\n { printf("Invalid character: %s\n", yytext); }

%%

int main(void) {
    yylex();
    return 0;
}
------------------
# valid identifier
%{
#include <stdio.h>
%}

%%

[a-zA-Z0-9_]+ { printf("Valid identifier: %s\n", yytext); }
.|\n { /* ignore all other characters */ }

%%

int main(void) {
    yylex();
    return 0;
}
-------------------
# starts with vowel
%{
#include <stdio.h>
%}

%%

[aeiouAEIOU][a-zA-Z]* { printf("Valid word: %s\n", yytext); }
.|\n { /* ignore all other characters */ }

%%

int main(void) {
    yylex();
    return 0;
}
