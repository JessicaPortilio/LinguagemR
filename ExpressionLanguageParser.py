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
#cases  → ID "=" "{" stms "}" "," cases | ID "=" "{" stms "}" 

# call → id ( params )
# exp → exp + exp |exp - exp | exp * exp |exp / exp | exp ^ exp | call | assign | num | id
# call → id (params) | id ( )
# params → exp, params | exp
# assign → id = exp

import ply.yacc as yacc
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
    '''signature : ID ID LPAREN sigparams RPAREN
                 | ID ID LPAREN RPAREN'''
    pass

def p_sigparams(p):
    '''sigparams : ID ID
                  | ID ID COMMA sigparams
    '''
    pass

def p_body(p):
    ''' body : LCHAV stms RCHAV
             | LCHAV RCHAV'''
    pass

def p_stms(p):
    ''' stms : stm
            | stm stms'''
    pass

def p_stm(p):
    ''' stm :  exp PV
             | WHILE LPAREN exp RPAREN body
             | RETURN exp PV
             | IF LPAREN exp RPAREN body ELSE body
             | FOR LPAREN ID IN EXP RPAREN body
             | REPEAT body UNTIL LPAREN exp RPAREN PV
             | BREAK PV
             | NEXT PV ''' 
    
    ''' stm :  SWITCH LPAREN exp COMMA  CASES RPAREN
    CASES : ID IGUAL body IGUALAT LCHAV body RCHAV COMMA CASES
            | ID IGUALAT LCHAV body RCHAV'''
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
    '''exp1 : exp1 SUBTRAIR exp2
         | exp2'''
    pass

def p_exp2_vezes(p):
   '''exp2 : exp2 VEZES exp3
           | exp3'''
   pass

def p_exp2_dividir(p):
   '''exp2 : exp2 DIVIDIR exp3
           | exp3'''
   pass

def p_exp3_pot(p):
    '''exp3 : exp4 POT exp3
            | exp4'''
    pass

def p_exp4_call(p):
    '''exp4 : call
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