import ply.lex as lex
import ply.yacc as yacc

reserved={
'SELECT': 'SELECT',
'FROM' : 'FROM'
}

tokens = list(reserved.values()) + ['ID',
'COMMA', 'SEMICOLON', 'STAR']

def t_ID(t):
    r'[_a-zA-Z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'ID')
    return t

t_COMMA = r','
t_SEMICOLON = r';'
t_STAR = r'[*]'
t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" %t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def p_select(p):
    's : SELECT c'

def p_select2(p):
    's : SELECT st'

def p_column(p):
    'c : ID com'

def p_comma(p):
    'com : COMMA ID com'

def p_comma2(p):
    'com : f'

def p_star(p):
    'st : STAR f'

def p_from(p):
    'f : FROM t'

def p_table(p):
    't : ID se'

def p_semi(p):
    'se : SEMICOLON'

def p_error(t):
    if(t):
        print("Syntax error at %s" %

t.value)
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