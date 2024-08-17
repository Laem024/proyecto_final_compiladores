import ply.lex as lex

tokens = (
    'ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON',
    'ASSIGN', 'TYPE', 'RETURN', 'COMMA'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_ASSIGN = r'='
t_COMMA = r','

t_ignore = ' \t'  # Ignorar espacios en blanco y tabulaciones

# Manejar los saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer_errors = []

def t_TYPE(t):
    r'int|float|double|void'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    error_message = f"Illegal character '{t.value[0]}' at line {t.lineno}"
    lexer_errors.append(error_message)
    t.lexer.skip(1)

lexer = lex.lex()
