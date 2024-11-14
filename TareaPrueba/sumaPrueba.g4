grammar sumaPrueba;

prog: statement* EOF; // Programa puede tener múltiples sentencias

functionDef: 'def' IDENTIFIER '(' parameters? ')' ':' block;
parameters: IDENTIFIER (',' IDENTIFIER)*;  // Lista de parámetros
block: '{' statement* '}'; // Un bloque puede tener múltiples sentencias dentro de corchetes

statement
    : functionDef
    | assignment
    | returnStatement
    | printStatement
    ;

assignment: IDENTIFIER '=' expression ';';  // Se añade ';' para finalizar la sentencia
returnStatement: 'return' expression ';';   // Se añade ';' para finalizar la sentencia
printStatement: 'print' '(' expression ')' ';'; // Se añade ';' para finalizar la sentencia

expression
    : expression ('+' | '-') expression   # AddSub
    | expression ('*' | '/') expression   # MulDiv
    | IDENTIFIER                          # Var
    | NUMBER                              # Number
    | '(' expression ')'                  # Parens
    | functionCall                        # FuncCall
    ;

functionCall: IDENTIFIER '(' (expression (',' expression)*)? ')'; // Llamada a función

// Definimos los tokens
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;    // Nombre de una variable
NUMBER: [0-9]+;                        // Números enteros
WS: [ \t\r\n]+ -> skip;                // Ignora los espacios en blanco
