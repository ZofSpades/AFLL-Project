import ply.lex as lex
import ply.yacc as yacc

reserved = {
    'INSERT': 'INSERT',
    'INTO': 'INTO',
    'SELECT': 'SELECT',
    'FROM': 'FROM',
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

def p_insert_into_select(p):
    '''s : INSERT INTO table_name LPAREN column_list RPAREN SELECT column_list FROM table_name SEMICOLON'''

def p_table_name(p):
    'table_name : ID'

def p_column_list(p):
    '''column_list : ID
                   | ID COMMA column_list'''

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
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