import ply.yacc as yacc
from compiler.lexer import tokens

def p_statement_assign(p):
    'statement : TYPE ID ASSIGN expression SEMICOLON'
    p[0] = ('assign', p[1], p[2], p[4])

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

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()
