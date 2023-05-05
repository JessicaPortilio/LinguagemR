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
from SintaxeAbstrata import *

def p_program(p):
    '''program : funcdecl
                | funcdecl program
                '''
    pass

def p_funcdecl(p):
    '''funcdecl : signature body'''
    p[0] = FuncDeclConcrete(p[1], p[2])


def p_signature(p):
    '''signature : DEF ID LPAREN sigparams RPAREN
                 | DEF ID LPAREN RPAREN
                 | DEF ID LPAREN sigparams RPAREN SEQUENCIAL
                 | DEF ID LPAREN RPAREN SEQUENCIAL'''
    if len(p) == 6:
        p[0] = SignatureConcrete(p[2], p[4], p[5] == "sequencial")
    elif len(p) == 5:
        p[0] = SignatureConcrete(p[2], None, p[4] == "sequencial")
    else:
        p[0] = SignatureConcrete(p[2], None, False)


def p_sigparams(p):
    '''sigparams : ID ID
                  | ID ID COMMA sigparams
    '''
    if len(p) == 3:
        p[0] = SingleSigParams(p[1])
    else:
        p[0] = CompoundSigParams(p[1], p[3])


def p_body(p):
    ''' body : LCHAV stms RCHAV
             | LCHAV RCHAV
             | stms'''
    if len(p) == 4:
        p[0] = BodyConcrete(p[2])
    else:
        p[0] = BodyConcrete([])


def p_stms(p):
    ''' stms : stm
            | stm stms'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_bodyORstm(p):
    '''bodyORstm : body 
                |  stm'''
    p[0] = p[1]

def p_stm_exp(p):
    ''' stm :  exp PV ''' 
    p[0] = StmExp(p[1])
    
def p_stm_while(p):
    ''' stm : WHILE LPAREN exp RPAREN body ''' 
    p[0] = StmWhile(p[3], p[5])

def p_stm_return(p):
    ''' stm : RETURN exp PV ''' 
    p[0] = StmReturn(p[2])

def p_stm_for(p):
    ''' stm : FOR LPAREN ID IN exp RPAREN body ''' 
    p[0] = StmFor(p[5])

def p_stm_repeat(p):
    ''' stm : REPEAT body WHILE LPAREN exp RPAREN PV ''' 
    p[0] = StmRepeat(p[5])

def p_stm_break(p):
    ''' stm : BREAK PV ''' 
    p[0] = StmBreak()
    
def p_stm_next(p):
    ''' stm : NEXT PV ''' 
    p[0] = StmNext()

def p_stm_witch(p):
    ''' stm :  SWITCH LPAREN exp COMMA  cases RPAREN 
            |  SWITCH LPAREN exp COMMA  casesnum RPAREN '''
    if len(p) == 7:
        p[0] = StmSwitch(p[3], p[5])
    else:
        p[0] = StmSwitchNum(p[3], p[4])

def p_cases(p):
    '''cases : exp IGUALAT exp
            | exp IGUALAT exp COMMA cases'''
    if len(p) == 4:
        p[0] = [Case(p[1], p[3])]
    else:
        p[5].insert(0, Case(p[1], p[3]))
        p[0] = p[5]

def p_cases_num(p):
    '''casesnum : exp
            | exp COMMA cases'''
    if len(p) == 2:
        p[0] = [CaseNum(p[1])]
    else:
        p[3].insert(0, CaseNum(p[1]))
        p[0] = p[3]


def p_stm_if(p):
    ''' stm : IF LPAREN exp RPAREN bodyORstm ''' 
    p[0] = StmIf(p[3], p[5])

def p_stm_if_seq(p):
    ''' stm : IF LPAREN exp RPAREN SEQUENCIAL bodyORstm ''' 
    p[0] = StmIfSeq(p[3], p[6])

def p_stm_if_else(p):
    ''' stm : IF LPAREN exp RPAREN bodyORstm ELSE bodyORstm''' 
    p[0] = StmIfElse(p[3], p[5], p[7])

def p_stm_if_else_seq1(p):
    ''' stm : IF LPAREN exp RPAREN SEQUENCIAL bodyORstm ELSE bodyORstm''' 
    p[0] = StmIfElseSeq1(p[3], p[6], p[8])

def p_stm_if_else_seq2(p):
    ''' stm : IF LPAREN exp RPAREN SEQUENCIAL bodyORstm ELSE SEQUENCIAL bodyORstm''' 
    p[0] = StmIfElseSeq2(p[3], p[6], p[9])

def p_stm_if_else_seq3(p):
    ''' stm : IF LPAREN exp RPAREN bodyORstm ELSE SEQUENCIAL bodyORstm''' 
    p[0] = StmIfElseSeq3(p[3], p[5], p[8])

def p_exp_assign(p):
    ''' exp :    exp IGUAL exp1
              | exp1'''
    if len(p) == 4:
        p[0] = AssignExp(p[1], p[3])
    else:
        p[0] = p[1]

def p_exp1_soma(p):
    '''exp1 : exp1 SOMA exp2
         | exp2'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = SomaExp(p[1], p[3])

def p_exp1_menos(p):
    '''exp1 : exp1 SUBTRAIR exp2'''
    p[0] = MenosExp(p[1], p[3])

def p_exp2_vezes(p):
   '''exp2 : exp2 VEZES exp3
           | exp3'''
   if len(p) == 4:
       p[0] = VezesExp(p[1], p[3])
   else:
       p[0] = p[1]

def p_exp2_dividir(p):
   '''exp2 : exp2 DIVIDIR exp3 '''
   if len(p) == 4:
    p[0] = DividirExp(p[1], p[3])
   else: 
       p[0] = p[1]
   

def p_exp3_pot(p):
    '''exp3 : exp4 POT exp3
            | exp4'''
    if len(p) == 4:
        p[0] = PotExp(p[1], p[3])
    else:
        p[0] = p[1]

def p_exp4_maior(p):
    '''exp4 : exp4 MAIOR exp5
        | exp5'''
    if len(p) == 4:
        p[0] = MaiorExp(p[1], p[3])
    else:
        p[0] = p[1]

def p_exp5_menor(p):
    '''exp5 : exp5 MENOR exp6
        | exp6'''
    if len(p) == 4:
        p[0] = MenorExp(p[1], p[3])
    else:
        p[0] = p[1]

def p_exp6_maiorigual(p):
    '''exp6 : exp6 MAIORIGUAL exp7
        | exp7'''
    if len(p) == 4:
        p[0] = MaiorIgualExp(p[1], p[3])
    else:
        p[0] = p[1]

def p_exp7_menorigual(p):
    '''exp7 : exp7 MENORIGUAL exp8
        | exp8'''
    if len(p) == 4:
        p[0] = MenorIgualExp(p[1], p[3])
    else:
        p[0] = p[1]

def p_exp8_diferente(p):
    '''exp8 : exp8 DIFERENTE exp9
        | exp9'''
    if len(p) == 4:
        p[0] = DiferenteExp(p[1], p[3])
    else:
        p[0] = p[1]

# t_ANDVETOR = r'\&'
def p_exp9_andvetor(p):
    '''exp9 : exp9 ANDVETOR exp10
        | exp10'''
    if len(p) == 4:
        p[0] = AndVetorExp(p[1], p[3])
    else:
        p[0] = p[1]
        

# t_AND = r'\&\&'
def p_exp10_and(p):
    '''exp10 : exp10 AND exp11
        | exp11'''
    if len(p) == 4:
        p[0] = AndExp(p[1], p[3])
    else:
        p[0] = p[1]

# t_ORVETOR = r'\|\|'
def p_exp11_orvetor(p):
    '''exp11 : exp11 ORVETOR exp12
        | exp12'''
    if len(p) == 4:
        p[0] = OrVetorExp(p[1], p[3])
    else:
        p[0] = p[1]

# t_OR = r'\|'
def p_exp12_or(p):
    '''exp12 : exp12 OR exp13
        | exp13'''
    if len(p) == 4:
        p[0] = OrExp(p[1], p[3])

# t_NOTLOGICO = r'!'
def p_exp13_notlogico(p):
    '''exp13 : exp13 NOTLOGICO exp14
        | exp14'''
    if len(p) == 3:
        p[0] = NotExp(p[2])
    else:
        p[0] = p[1]

# t_XOR = r'XOR'
def p_exp14_xor(p):
    '''exp14 : exp14 XOR exp15
        | exp15'''
    if len(p) == 4:
        p[0] = XorExp(p[1], p[3])
    else:
        p[0] = p[1]


# Tem que colocar o de == porém toda vez que eu tento colocar está quebrando com tudo
# Lembrar de pedir para o professor nos ajudar com isso


def p_exp15_call(p):
    '''exp15 : call
            | NUMBER_INT
            | NUMBER_FLOAT
            | ID
            | TRUE
            | FALSE'''
    if len(p) == 2:
        if isinstance(p[1], CallExp):
            p[0] = p[1]
        elif isinstance(p[1], int):
            p[0] = NumIntExp(p[1])
        elif isinstance(p[1], float):
            p[0] = NumFloatExp(p[1])
        elif isinstance(p[1], str):
            if p[1] == 'true':
                p[0] = BooleanExp(True)
            elif p[1] == 'false':
                p[0] = BooleanExp(False)
            else:
                p[0] = IdExp(p[1])

def p_call_id_params(p):
    '''call : ID LPAREN params RPAREN
            | ID LPAREN RPAREN'''
    if len(p) == 4:
        p[0] = NoParamsCall(p[1])
    else:
        p[0] = ParamsCall(p[1], p[3])

def p_params_ids(p):
    '''params : exp COMMA params
            | exp '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[3].insert(0, p[1])
        p[0] = p[3]

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc() 
print(parser.parse(debug = False))

