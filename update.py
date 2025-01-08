import ply as ply
import ply.lex as lex
import ply.yacc as yacc

reserved={
'UPDATE': 'UPDATE',
'SET' : 'SET',
'WHERE' : 'WHERE',
'AND' : 'AND'
}

tokens = list(reserved.values()) + ['ID','SEMICOLON','EQUAL','COMMA']

def t_ID(t):
    r'[_a-zA-Z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'ID')
    return t


t_SEMICOLON = r';'
t_COMMA = r','
t_EQUAL = r'='
t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" %t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def p_update(p):
    's : UPDATE ID c'
    
def p_val1(p):
    'c : SET v'
    
def p_val2(p):
    'v : ID EQUAL ID d'
    
def p_val3(p):
    'd : COMMA v'
    
def p_dest(p):
    'd : WHERE v'
    
def p_dest2(p):
    'd : AND v'
    
def p_end(p):
    'd : se'
    
def p_semi(p):
    'se : SEMICOLON'

def p_error(t):
    if(t):
        print("Syntax error at %s" %t.value)
    else:
        print("Syntax error: missing token")

parser = yacc.yacc()

while True:
    try:
        s = input('\nCommand > ')
        if s=='exit':
            print("\n")
            break
    except EOFError:
        break
    parser.parse(s)