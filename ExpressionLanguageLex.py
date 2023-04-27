import ply.lex as lex

def space_counter(token):
    spaces = 0
    for c in token.value:
        if c == ' ':
            spaces += 1
        elif c == '\t':
            spaces += 8 - (spaces % 8)
    return spaces

reservadas = {
    'if' : 'IF',
    'else' : 'ELSE',
    'repeat' : 'REPEAT',
    'while' : 'WHILE',
    'function' : 'FUNCTION',
    'for' : 'FOR',
    'in' : 'IN',
    'next' : 'NEXT',
    'break' : 'BREAK',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'null' : 'NULL',
    'inf' : 'INF',
    'NaN' : 'NANA',
    'NA' : 'NA',
    'NA_integer_' : 'NA_INTEGER_',
    'NA_real_' : 'NA_REAL_',
    'NA_complex' : 'NA_COMPLEX',
    'NA_character_' : 'NA_CHARACTER_',
    'call' : 'CALL',
    'cat' : 'CAT',
    'switch' : 'SWITCH',
    'return' : 'RETURN',
    

}

tokens = ['PASS','ID', 'NUMBER_INT', 'NUMBER_FLOAT', 'SOMA', 'VEZES', 'IGUALAT', 'DIVIDIR', 'SUBTRAIR', 'LPAREN', 'RPAREN', 
          'LCHAV', 'RCHAV', 'POT', 'COMMA', 'IGUAL', 'DIFERENTE', 'MAIOR', 'MENOR', 'MAIORIGUAL', 'MENORIGUAL', 
          'ANDVETOR', 'AND', 'ORVETOR', 'OR', 'NOTLOGICO', 'XOR', 'SEQUENCIAL', 'MODULO', 'PV', 'LINHA', 'IDENT', 'DEDENT',
          ] + list(reservadas.values())

t_SOMA = r'\+'
t_VEZES = r'\*'
t_IGUALAT = r'<-'
t_DIVIDIR = r'/'
t_SUBTRAIR = r'-'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCHAV = r'{'
t_RCHAV = r'}'
t_POT = r'\^'
t_COMMA = r'\,'
t_PASS = r'\.\.\.'
t_DIFERENTE = r'!='
t_MAIOR =r'>'
t_MENOR =r'<'
t_MAIORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_IGUAL = r'=='
t_ANDVETOR = r'\&'
t_AND = r'\&\&'
t_ORVETOR = r'\|\|'
t_OR = r'\|'
t_NOTLOGICO = r'!'
t_XOR = r'XOR'
t_SEQUENCIAL = r'\:'
t_MODULO = r'%%'
t_PV =r';'

stack = [0]
states = (('idstate', 'exclusive'),
          ('dedstate', 'exclusive'),)

def t_ID(t):
    r'[a-zA-Z\t][a-zA-Z0-9_\. \t]*'
    t.type = reservadas.get(t.value, 'ID')
    return t

# t_LINHA = '[a-zA-Z][a-zA-Z \t]+'

def t_breakline(t):
    r'\n+'                                 #reconhece uma ou mais linhas de quebra
    t.lexer.lineno += len(t.value) 
    t.lexer.begin('idstate')

def t_idstate_blankline(t):
    r'([ \t]+)\n'                           #reconhece uma linha em branco
    # print('t_idstate_blankline')
    pass

def t_idstate_linewithcode(t):
    '([ \t]+) | ([a-zA-Z])'                 #reconhece espaços em branco e tabulações ou uma letra
    n_spaces = space_counter(t)
    t.lexer.begin('INITIAL')
    if n_spaces < stack[-1]:
        t.lexer.skip(-len(t.value))
        while n_spaces < stack[-1]:
            stack.pop()
            t.type='DEDENT'
            t.lexer.begin('dedstate')
        return t
    elif n_spaces > stack[-1]:
        stack.append(n_spaces)
        t.type='IDENT'
        return t
    elif n_spaces == 0:
        t.lexer.skip(-1)

def t_dedstate_linewithdedent(t):
    '([ \t]+) | ([a-zA-Z])'                 #recognizes white spaces and tabs or a letter
    n_spaces = space_counter(t)
    if n_spaces < stack[-1]:
        t.lexer.skip(-len(t.value))
        while n_spaces < stack[-1]:
            stack.pop()
            t.type='DEDENT'
        t.lexer.begin('dedstate')
        return t
    elif n_spaces > stack[-1]:  
        t.lexer.begin('INITIAL')
        if n_spaces > stack[-1]:
            print('Erro de dedentação --->', n_spaces)
        elif n_spaces == 0:                  # If the element starts with a letter
            t.lexer.skip(-1)

def t_error(t):
    print("ERROR in INITIAL state")
    print(t.value)
    t.lexer.skip(1)

def t_idstate_error(t):
    print("ERROR in idstate state")
    t.lexer.skip(1)

def t_dedstate_error(t):
    print("ERROR in dedstate state")
    t.lexer.skip(1)


# Expressão regular para identificar comentários
t_ignore_COMMENT = r'\#.*'



def t_NUMBER_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMBER_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# t_ignore = ' \t'

# def t_error(t):
#     print("Illegal character '%s'" % t.value[0])
#     t.lexer.skip(1)




# Build the lexer
lexer = lex.lex()
programa = """#Comentario

def soma():
    if True:
        print(soma)
return qualquer coisa
"""
lexer.input(programa)


# for token in lex.lexer:
#     print('[', token.type, ',', token.value)
#