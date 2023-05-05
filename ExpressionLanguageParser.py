# Rascunho da gramatica
# program → funcdecl | funcdecl program
# funcdecl → signature body
# signature → id id ( sigParams)
# sigparams → ID ID | ID ID COMMA sigparams
# body → { stms }
# stms → stm  | stm  stms
# stm → exp ;  | 
#while ( exp ) body | 
#return exp ; |
#IF "(" exp ")" body ELSE body |
#FOR "(" ID "in" exp ")" body |
#REPEAT body UNTIL "(" exp ")" ";" |
#break ";" |
#next ";"
#stm → SWITCH "(" exp "," cases ")"
#cases  → "(" exp ")" "=" "{" stms "}"
#       | "(" exp ")" "=" "{" stms "}" "(" cases ")"
#       | "(" exp ")" "=" "{" stms "}"
#       | "(" exp ")" "=" "{" stms "}" "(" cases ")"
#
# call → id ( params )
# exp → exp + exp |exp - exp | exp * exp |exp / exp | exp ^ exp | call | assign | num | id
# call → id (params) | id ( )
# params → exp, params | exp
# assign → id = exp


import ply.yacc as yacc
import ply.lex as lex
from ExpressionLanguageLex import *


def p_program(p):
    '''program : funcdecl
                | funcdecl program
                '''
    pass

def p_funcdecl(p):
    '''funcdecl : signature body'''
    pass

def p_signature(p):
    '''signature : DEF ID LPAREN sigparams RPAREN
                 | DEF ID LPAREN RPAREN
                 | DEF ID LPAREN sigparams RPAREN SEQUENCIAL
                 | DEF ID LPAREN RPAREN SEQUENCIAL'''
    pass

def p_sigparams(p):
    '''sigparams : ID ID
                  | ID ID COMMA sigparams
    '''
    pass

def p_body(p):
    ''' body : LCHAV stms RCHAV
             | LCHAV RCHAV
             | stms'''
    pass

def p_stms(p):
    ''' stms : stm
            | stm stms'''
    pass
def p_bodyORstm(p):
    '''bodyORstm : body 
                |  stm'''

def p_stm_exp(p):
    ''' stm :  exp PV ''' 
    pass
    
def p_stm_while(p):
    ''' stm : WHILE LPAREN exp RPAREN body ''' 
    pass

def p_stm_return(p):
    ''' stm : RETURN exp PV ''' 
    pass

def p_stm_for(p):
    ''' stm : FOR LPAREN ID IN exp RPAREN body ''' 
    pass

def p_stm_repeat(p):
    ''' stm : REPEAT body WHILE LPAREN exp RPAREN PV ''' 
    pass

def p_stm_break(p):
    ''' stm : BREAK PV ''' 
    pass

def p_stm_next(p):
    ''' stm : NEXT PV ''' 
    pass

def p_stm_witch(p):
    ''' stm :  SWITCH LPAREN exp COMMA  cases RPAREN 
            |  SWITCH LPAREN exp COMMA  casesnum RPAREN '''
    pass

def p_cases(p):
    '''cases : exp IGUALAT exp
            | exp IGUALAT exp COMMA cases'''
    pass

def p_cases_num(p):
    '''casesnum : exp
            | exp COMMA cases'''
    pass

def p_stm_if(p):
    ''' stm : IF LPAREN exp RPAREN bodyORstm ''' 
    pass

def p_stm_if_seq(p):
    ''' stm : IF LPAREN exp RPAREN SEQUENCIAL bodyORstm ''' 
    pass

def p_stm_if_else(p):
    ''' stm : IF LPAREN exp RPAREN bodyORstm ELSE bodyORstm''' 
    pass

def p_stm_if_else_seq1(p):
    ''' stm : IF LPAREN exp RPAREN SEQUENCIAL bodyORstm ELSE bodyORstm''' 
    pass

def p_stm_if_else_seq2(p):
    ''' stm : IF LPAREN exp RPAREN SEQUENCIAL bodyORstm ELSE SEQUENCIAL bodyORstm''' 
    pass

def p_stm_if_else_seq3(p):
    ''' stm : IF LPAREN exp RPAREN bodyORstm ELSE SEQUENCIAL bodyORstm''' 
    pass

def p_exp_assign(p):
    ''' exp :    exp IGUAL exp1
              | exp1'''
    pass

def p_exp1_soma(p):
    '''exp1 : exp1 SOMA exp2
         | exp2'''
    pass

def p_exp1_menos(p):
    '''exp1 : exp1 SUBTRAIR exp2'''
    pass

def p_exp2_vezes(p):
   '''exp2 : exp2 VEZES exp3
           | exp3'''
   pass

def p_exp2_dividir(p):
   '''exp2 : exp2 DIVIDIR exp3 '''
   pass

def p_exp3_pot(p):
    '''exp3 : exp4 POT exp3
            | exp4'''
    pass

def p_exp4_maior(p):
    '''exp4 : exp4 MAIOR exp5
        | exp5'''
    pass

def p_exp5_menor(p):
    '''exp5 : exp5 MENOR exp6
        | exp6'''
    pass

def p_exp6_maiorigual(p):
    '''exp6 : exp6 MAIORIGUAL exp7
        | exp7'''
    pass

def p_exp7_menorigual(p):
    '''exp7 : exp7 MENORIGUAL exp8
        | exp8'''
    pass

def p_exp8_diferente(p):
    '''exp8 : exp8 DIFERENTE exp9
        | exp9'''
    pass

# t_ANDVETOR = r'\&'
def p_exp9_andvetor(p):
    '''exp9 : exp9 ANDVETOR exp10
        | exp10'''
    pass

# t_AND = r'\&\&'
def p_exp10_and(p):
    '''exp10 : exp10 AND exp11
        | exp11'''
    pass

# t_ORVETOR = r'\|\|'
def p_exp11_orvetor(p):
    '''exp11 : exp11 ORVETOR exp12
        | exp12'''
    pass

# t_OR = r'\|'
def p_exp12_or(p):
    '''exp12 : exp12 OR exp13
        | exp13'''
    pass

# t_NOTLOGICO = r'!'
def p_exp13_notlogico(p):
    '''exp13 : exp13 NOTLOGICO exp14
        | exp14'''
    pass

# t_XOR = r'XOR'
def p_exp14_xor(p):
    '''exp14 : exp14 XOR exp15
        | exp15'''
    pass

def p_exp15_call(p):
    '''exp15 : call
            | NUMBER_INT
            | NUMBER_FLOAT
            | ID
            | TRUE
            | FALSE'''
    pass

def p_call_id_params(p):
    '''call : ID LPAREN params RPAREN
            | ID LPAREN RPAREN'''
    pass

def p_params_ids(p):
    '''params : exp COMMA params
            | exp '''
    pass

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc() 
print(parser.parse(debug = False))

