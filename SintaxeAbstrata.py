from abc import abstractmethod
from abc import ABCMeta
from Visitor import Visitor

class Program(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SimpleProgram(Program):
    def __init__(self, funcdecl):
        self.funcdecl = funcdecl
    def accept(self, visitor):
        return visitor.visit_simple_program(self)

class CompositeProgram(Program):
    def __init__(self, funcdecl, program):
        self.funcdecl = funcdecl
        self.program = program
    def accept(self, visitor):
        return visitor.visit_composite_program(self)
    

class FuncDecl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class FuncDeclConcrete(FuncDecl):
    def __init__(self, signature, body):
        self.signature = signature
        self.body = body
    def accept(self, visitor):
        return visitor.visitFuncDeclConcrete(self)

'''
Assinatura de função
Signature
'''
class Signature(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class SignatureConcrete(Signature):
    def __init__(self, id, sigParams, is_sequential):
        self.id = id
        self.sigParams = sigParams
        self.is_sequential = is_sequential
        
    def accept(self, visitor):
        return visitor.visitSignatureConcrete(self)
    
'''
Parâmetros de assinatura de função
SigParams
'''

class SigParams(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SingleSigParams(SigParams):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitSingleSigParams(self)


class CompoundSigParams(SigParams):
    def __init__(self, id, sigParams):
        self.id = id
        self.sigParams = sigParams
    def accept(self, visitor):
        return visitor.visitCompoundSigParams(self)

'''
Corpo de uma função
Body
'''

class Body(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class BodyConcrete(Body):
    def __init__(self, stms):
        self.stms = stms
    def accept(self, visitor):
        return visitor.visitBodyConcrete(self)


class Stm(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class StmExp(Stm):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitStmExp(self)

class StmWhile(Stm):
    def __init__(self, exp, bodyORstm):
        self.exp = exp
        self.bodyORstm = bodyORstm
    def accept(self, visitor):
        return visitor.visitStmWhile(self)

class StmReturn(Stm):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitStmReturn(self)

class StmFor(Stm):
    def __init__(self, id, exp, bodyORstm):
        self.id = id
        self.exp = exp
        self.bodyORstm = bodyORstm
    def accept(self, visitor):
        return visitor.visitStmFor(self)

class StmRepeat(Stm):
    def __init__(self, bodyORstm, exp):
        self.bodyORstm = bodyORstm
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitStmRepeat(self)

# def p_stm_break(p):
#     ''' stm : BREAK PV ''' 
#     pass
class StmBreak(Stm):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitStmReturn(self)

# def p_stm_next(p):
#     ''' stm : NEXT PV ''' 
#     pass
class StmNext(Stm):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitStmReturn(self)
# def p_stm_witch(p):
#     ''' stm :  SWITCH LPAREN exp COMMA  cases RPAREN 
#             |  SWITCH LPAREN exp COMMA  casesnum RPAREN '''
#     pass
class StmSwitch(Stm):
    def __init__(self, exp, cases):
        self.exp = exp
        self.cases = cases
    def accept(self, visitor):
        return visitor.visitStmSwitch(self)

class StmSwitchNum(Stm):
    def __init__(self, exp, casesnum):
        self.exp = exp
        self.casesnum = casesnum
    def accept(self, visitor):
        return visitor.visitStmSwitchNum(self)

class Case():
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

class CaseNum():
    def __init__(self, exp):
        self.exp = exp


class StmIf(Stm):
    def __init__(self, exp, bodyORstm):
        self.exp = exp
        self.bodyORstm = bodyORstm
    def accept(self, visitor):
        return visitor.visitStmIf(self)

class StmIfSeq(Stm):
    def __init__(self, exp, bodyORstm):
        self.exp = exp
        self.bodyORstm = bodyORstm
    def accept(self, visitor):
        return visitor.visitStmIfSeq(self)

class StmIfElse(Stm):
    def __init__(self, exp, ifBody, elseBody):
        self.exp = exp
        self.ifBody = ifBody
        self.elseBody = elseBody
    def accept(self, visitor):
        return visitor.visitStmIfElse(self)

class StmIfElseSeq1(Stm):
    def __init__(self, exp, ifBody, elseBody):
        self.exp = exp
        self.ifBody = ifBody
        self.elseBody = elseBody
    def accept(self, visitor):
        return visitor.visitStmIfElseSeq1(self)

class StmIfElseSeq2(Stm):
    def __init__(self, exp, ifBody, elseBody):
        self.exp = exp
        self.ifBody = ifBody
        self.elseBody = elseBody
    def accept(self, visitor):
        return visitor.visitStmIfElseSeq2(self)

class StmIfElseSeq3(Stm):
    def __init__(self, exp, ifBody, elseBody):
        self.exp = exp
        self.ifBody = ifBody
        self.elseBody = elseBody
    def accept(self, visitor):
        return visitor.visitStmIfElseSeq3(self)
'''
Expressoes
Exp
'''

class Exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

# def p_exp_assign(p):
#     ''' exp :    exp IGUAL exp1
#               | exp1'''
#     pass
class AssignExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitAssignExp(self)


# def p_exp1_soma(p):
#     '''exp1 : exp1 SOMA exp2
#          | exp2'''
#     pass
#

class SomaExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitSomaExp(self)
# def p_exp1_menos(p):
#     '''exp1 : exp1 SUBTRAIR exp2'''
#     pass
class MenosExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitMenosExp(self)

# def p_exp2_vezes(p):
#    '''exp2 : exp2 VEZES exp3
#            | exp3'''
#    pass
class VezesExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitVezesExp(self)

# def p_exp2_dividir(p):
#    '''exp2 : exp2 DIVIDIR exp3 '''
#    pass
class DividirExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitDividirExp(self)
# def p_exp3_pot(p):
#     '''exp3 : exp4 POT exp3
#             | exp4'''
#     pass
class PotExp(Exp):
    def __init__(self, exp3, exp4):
        self.exp4 = exp4
        self.exp3 = exp3
    def accept(self, visitor):
        return visitor.visitPotExp(self)


# def p_exp4_maior(p):
#     '''exp4 : exp4 MAIOR exp5
#         | exp5'''
#     pass
class MaiorExp(Exp):
    def __init__(self, exp4, exp5):
        self.exp4 = exp4
        self.exp5 = exp5
    def accept(self, visitor):
        return visitor.visitMaiorExp(self)

# def p_exp5_menor(p):
#     '''exp5 : exp5 MENOR exp6
#         | exp6'''
#     pass
class MenorExp(Exp):
    def __init__(self, exp5, exp6):
        self.exp5 = exp5
        self.exp6 = exp6
    def accept(self, visitor):
        return visitor.visitMenorExp(self)

# def p_exp6_maiorigual(p):
#     '''exp6 : exp6 MAIORIGUAL exp7
#         | exp7'''
#     pass
class MaiorIgualExp(Exp):
    def __init__(self, exp6, exp7):
        self.exp6 = exp6
        self.exp7 = exp7
    def accept(self, visitor):
        return visitor.visitMaiorIgualExp(self)

# def p_exp7_menorigual(p):
#     '''exp7 : exp7 MENORIGUAL exp8
#         | exp8'''
#     pass
class MenorIgualExp(Exp):
    def __init__(self, exp7, exp8):
        self.exp7 = exp7
        self.exp8 = exp8
    def accept(self, visitor):
        return visitor.visitMenorIgualExp(self)

# def p_exp8_diferente(p):
#     '''exp8 : exp8 DIFERENTE exp9
#         | exp9'''
#     pass
class DiferenteExp(Exp):
    def __init__(self, exp8, exp9):
        self.exp8 = exp8
        self.exp9 = exp9
    def accept(self, visitor):
        return visitor.visitDiferenteExp(self)


# # t_ANDVETOR = r'\&'
# def p_exp9_andvetor(p):
#     '''exp9 : exp9 ANDVETOR exp10
#         | exp10'''
#     pass
class AndVetorExp(Exp):
    def __init__(self, exp9, exp10):
        self.exp9 = exp9
        self.exp10 = exp10
    def accept(self, visitor):
        return visitor.visitAndVetorExp(self)
    
# # t_AND = r'\&\&'
# def p_exp10_and(p):
#     '''exp10 : exp10 AND exp11
#         | exp11'''
#     pass

class AndExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitAndExp(self)

# # t_ORVETOR = r'\|\|'
# def p_exp11_orvetor(p):
#     '''exp11 : exp11 ORVETOR exp12
#         | exp12'''
#     pass

class OrVetorExp(Exp):
    def __init__(self, exp11, exp12):
        self.exp11 = exp11
        self.exp12 = exp12
    def accept(self, visitor):
        return visitor.visitOrVetorExp(self)

# # t_OR = r'\|'
# def p_exp12_or(p):
#     '''exp12 : exp12 OR exp13
#         | exp13'''
#     pass
class OrExp(Exp):
    def __init__(self, exp12, exp13):
        self.exp12 = exp12
        self.exp13 = exp13
    def accept(self, visitor):
        return visitor.visitOrExp(self)

# # t_NOTLOGICO = r'!'
# def p_exp13_notlogico(p):
#     '''exp13 : exp13 NOTLOGICO exp14
#         | exp14'''
#     pass

class NotExp(Exp):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitNotExp(self)

# # t_XOR = r'XOR'
# def p_exp14_xor(p):
#     '''exp14 : exp14 XOR exp15
#         | exp15'''
#     pass

class XorExp(Exp):
    def init(self, exp14, exp15):
        self.exp14 = exp14
        self.exp15 = exp15
    def accept(self, visitor):
        return visitor.visitXorExp(self)




# def p_exp15_call(p):
#     '''exp15 : call
#             | NUMBER_INT
#             | NUMBER_FLOAT
#             | ID
#             | TRUE
#             | FALSE'''
#     pass


class CallExp(Exp, Stm):
    def __init__(self, call):
        self.call = call

    def accept(self, visitor):
        return visitor.visitCallExp(self)

class NumIntExp(Exp):
    def __init__(self, numInt):
        self.numInt = numInt
    def accept(self, visitor):
        return visitor.visitNumIntExp(self)

class NumFloatExp(Exp):
    def __init__(self, numFloat):
        self.numFloat = numFloat
    def accept(self, visitor):
        return visitor.visitNumFloatExp(self)


class IdExp(Exp):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitIdExp(self)

class BooleanExp(Exp):
    def __init__(self, boolValue):
        self.boolValue = boolValue
    def accept(self, visitor):
        return visitor.visitBooleanExp(self)

'''
Chamada de funcao
Call
'''
class Call(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ParamsCall(Call):
    def __init__ (self, id, params):
        self.id = id
        self.params = params
    def accept(self, visitor):
        return visitor.visitParamsCall(self)

class NoParamsCall(Call):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitNoParamsCall(self)


'''
Parametros de uma chamada de funcao
Params
'''
class Params(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CompoundParams(Params):
    def __init__(self, exp, params):
        self.exp = exp
        self.params = params
    def accept(self, visitor):
        return visitor.visitCompoundParams(self)

class SingleParam(Params):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitSingleParam(self)