import ply as ply
import ply.lex as lex
import ply.yacc as yacc

reserved={
'DELETE': 'DELETE',
'FROM' : 'FROM',
'WHERE' : 'WHERE',
'AND' : 'AND'
}

tokens = list(reserved.values()) + ['ID','SEMICOLON','EQUAL']

def t_ID(t):
    r'[_a-zA-Z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'ID')
    return t

t_SEMICOLON = r';'
t_EQUAL = r'='
t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" %t.value[0])
    t.lexer.skip(1)
lexer = lex.lex()

def p_delete(p):
    's : DELETE FROM c'
    
def p_dest(p):
    'c : ID WHERE d'
    
def p_source(p):
    'd : ID EQUAL ID f'
    
def p_source2(p):
    'f : AND d'
    
def p_end(p):
    'f : se'
    
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