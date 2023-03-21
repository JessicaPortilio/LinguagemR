import ply.lex as lex

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
    

}

tokens = ['PASS','ID', 'NUMBER', 'SOMA', 'VEZES', 'IGUALAT', 'DIVIDIR', 'SUBTRAIR', 'LPAREN', 'RPAREN', 
          'LCHAV', 'RCHAV', 'POT', 'COMMA', 'IGUAL', 'DIFERENTE', 'MAIOR', 'MENOR', 'MAIORIGUAL', 'MENORIGUAL', 
          'ANDVETOR', 'AND', 'ORVETOR', 'OR', 'NOTLOGICO', 'XOR', 'SEQUENCIAL', 'MODULO', 'PV'
          ] + list(reservadas.values())

t_SOMA = r'\+'
t_VEZES = r'\*'
t_IGUALAT = r'='
t_DIVIDIR = r'/'
t_SUBTRAIR = r'-'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCHAV = r'{'
t_RCHAV = r'}'
t_POT = r'\^'
t_COMMA = r','
t_PASS = r'\.\.\.'
t_DIFERENTE = r'!='
t_MAIOR =r'>'
t_MENOR =r'<'
t_MAIORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_IGUAL = r'=='
t_ANDVETOR = r'&'
t_AND = r'&&'
t_ORVETOR = r'\|'
t_OR ='\|'
t_NOTLOGICO = '!'
t_XOR = r'XOR'
t_SEQUENCIAL = r':'
t_MODULO = r'%%'
t_PV =r';'

# Expressão regular para identificar comentários
t_ignore_COMMENT = r'\#.*'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.ype = reservadas.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()
 
lex.input("""# Uma funcao que realiza a soma de dois numeros
def soma(a,b): # a função espera receber dois argumentos
    return a + b # retorna a soma dos dois numeros""")

for token in lexer:
  print(token.type, token.value)

