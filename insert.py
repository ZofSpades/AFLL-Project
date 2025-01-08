import ply as ply
import ply.lex as lex
import ply.yacc as yacc

reserved = {
    'INSERT': 'INSERT',
    'INTO': 'INTO',
    'VALUES': 'VALUES'
}

tokens = list(reserved.values()) + ['ID', 'SEMICOLON', 'COMMA', 'LPAREN', 'RPAREN']

def t_ID(t):
    r'[_a-zA-Z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  
    return t

t_SEMICOLON = r';'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def p_insert_into(p):
    's : INSERT INTO table_name VALUES LPAREN values_list RPAREN SEMICOLON'

def p_table_name(p):
    'table_name : ID'

def p_values_list(p):
    '''values_list : ID
                   | ID COMMA values_list'''

def p_error(t):
    if t:
        print("Syntax error at '%s'" % t.value)
    else:
        print("Syntax error: missing token")

parser = yacc.yacc()

while True:
    try:
        s = input('\nCommand > ')
        if s == 'exit':
            print("\nExiting...")
            break
    except EOFError:
        break
    parser.parse(s)