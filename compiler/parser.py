import ply.yacc as yacc
from compiler.lexer import tokens

def p_function(p):
    'function : TYPE ID LPAREN params RPAREN LBRACE statements RBRACE'
    p[0] = ('function', p[1], p[2], p[4], p[7])

def p_params(p):
    '''params : TYPE ID
              | TYPE ID COMMA params
              | empty'''
    if len(p) == 3:
        p[0] = [('param', p[1], p[2])]
    elif len(p) == 5:
        p[0] = [('param', p[1], p[2])] + p[4]
    else:
        p[0] = []

def p_statements(p):
    '''statements : statement
                  | statement statements'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_statement_assign(p):
    'statement : TYPE ID ASSIGN expression SEMICOLON'
    p[0] = ('assign', p[1], p[2], p[4])

def p_statement_return(p):
    'statement : RETURN expression SEMICOLON'
    p[0] = ('return', p[2])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('num', p[1])

def p_expression_id(p):
    'expression : ID'
    p[0] = ('id', p[1])

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()
