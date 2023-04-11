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
    ''' stm :  SWITCH LPAREN exp COMMA  cases RPAREN '''
    pass

def p_cases(p):
    '''cases : exp IGUAL body
            | exp IGUAL body cases
            | exp IGUAL stm
            | exp IGUAL stm cases'''
    pass


def p_stm_if_else(p):
    ''' stm : IF LPAREN exp RPAREN body ELSE body ''' 
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

parser = yacc.yacc() 

