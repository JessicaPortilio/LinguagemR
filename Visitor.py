from AbstractVisitor import AbstractVisitor
# global tab
tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p

class Visitor(AbstractVisitor):

    def visitFuncDeclConcrete(self, funcDeclConcrete):
        funcDeclConcrete.signature.accept(self)
        funcDeclConcrete.body.accept(self)
        

    def visitSignatureConcrete(self, signatureConcrete):
        print(signatureConcrete.id, '(', end = '', sep='')
        if (signatureConcrete.sigParams != None):
            signatureConcrete.sigParams.accept(self)
        print(')', end = '')

    def visitSingleSigParams(self, singleSigParams):
        print(singleSigParams.id, end='', sep='')

    def visitCompoundSigParams(self, compoundSigParams):
        print(compoundSigParams.id, ', ', end='', sep='')
        compoundSigParams.sigParams.accept(self)



# class SimpleProgram(Program):
#     def __init__(self, funcdecl):
#         self.funcdecl = funcdecl
#     def accept(self, visitor):
#         return visitor.visit_simple_program(self)

# class CompositeProgram(Program):
#     def __init__(self, funcdecl, program):
#         self.funcdecl = funcdecl
#         self.program = program
#     def accept(self, visitor):
#         return visitor.visit_composite_program(self)


    def visit_simple_program(self, SimpleProgram):
        SimpleProgram.funcdecl.accept(self)

    def visit_composite_program(self, CompositeProgram):
        CompositeProgram.funcdecl.accept(self)
        CompositeProgram.program.accept(self)

    def visitBodyConcrete(self, bodyConcrete):
        global tab
        print ('{ ')
        tab =  tab + 3
        if (bodyConcrete.stms != None):
            bodyConcrete.stms.accept(self)
        tab =  tab - 3
        print (blank(), '} ', sep='')

    def visitSingleStm(self, singleStm):
        singleStm.stm.accept(self)

    def visitCompoundStm(self, compoundStm):
        compoundStm.stm.accept(self)
        compoundStm.stms.accept(self)

    def visitStmExp(self, stmExp):
        print(blank(),sep='',end='')
        stmExp.exp.accept(self)
        print('')

    def visitStmWhile(self, stmWhile):
        print (blank(), 'while (', end='', sep='')
        stmWhile.exp.accept(self)
        print (')', end='', sep='')
        stmWhile.block.accept(self)

    def visitStmReturn(self, stmReturn):
        print (blank(), 'return ', end='', sep='')
        stmReturn.exp.accept(self)
        print (';')

    def visitAssignExp(self, assignExp):
        # print("visitAssignExp")
        assignExp.exp1.accept(self)
        print(' <- ', end='')
        assignExp.exp2.accept(self)

    def visitSomaExp(self, somaExp):
        # print("visitSomaExp")
        somaExp.exp1.accept(self)
        print(' + ', end='')
        somaExp.exp2.accept(self)

    def visitMenosExp(self, menosExp):
        menosExp.exp1.accept(self)
        print(' -', end='')
        menosExp.exp2.accept(self)

    def visitVezesExp(self, VezesExp):
        VezesExp.exp1.accept(self)
        print(' * ', end='')
        VezesExp.exp2.accept(self)

    def visitDividirExp(self,DividirExp):
        DividirExp.exp1.accept(self)
        print(' / ', end='')
        DividirExp.exp2.accept(self)

    def visitPotExp(self, potExp):
        potExp.exp3.accept(self)
        print(' ^ ', end='')
        potExp.exp4.accept(self)

    def visitIgualExp(self, IgualExp):
        IgualExp.exp15.accept(self)
        print(' == ', end='')
        IgualExp.exp16.accept(self)

    def visitMaiorExp(self, MaiorExp):
        MaiorExp.exp4.accept(self)
        print(' > ', end = '')
        MaiorExp.exp5.accept(self)

    def visitMenorExp(self,MenorExp):
        MenorExp.exp5.accept(self)
        print (' < ', end= '')
        MenorExp.exp6.accept(self)

    def visitMaiorIgualExp(self, MaiorIgualExp):
        MaiorIgualExp.exp6.accept(self)
        print(' >= ', end='')
        MaiorIgualExp.exp7.accept(self)

    def visitMenorIgualExp(self, MenorIgualExp):
        MenorIgualExp.exp7.accept(self)
        print(' <= ', end='')
        MenorIgualExp.exp8.accept(self)

    def visitDiferenteExp(self, DiferenteExp):
        DiferenteExp.exp8.accept(self)
        print('!= ',end='')
        DiferenteExp.exp9.accept(self)

    def visitAndExp(self, AndExp):
        AndExp.exp1.accept(self)
        print('&&', end='')
        AndExp.exp2.accept(self)
        
    def visitAndVetorExp(self,AndVetorExp):
        AndVetorExp.exp9.accept(self)
        print('&', end='')
        AndVetorExp.exp10.accept(self)

    def visitOrExp(self, OrExp):
        OrExp.exp12.accept(self)
        print(' || ', end='')
        OrExp.exp13.accept(self)

    def visitOrVetorExp(self,OrVetorExp):
        OrVetorExp.exp11.accept(self)
        print(' | ',end='')
        OrVetorExp.exp12.accept(self)

    def visitXorExp(self, XorExp):
        XorExp.exp14.accept(self)
        print(' xor ',end='')
        XorExp.exp15.accept(self)

    def visitNotExp(self, NotExp):
        NotExp.exp13.accept(self)
        print(' ! ',end='')
        NotExp.exp14.accept(self)

    def visitCallExp(self, callExp):
        # print("visitCallExp")
        callExp.call.accept(self)

    def visitNumIntExp(self, numIntExp):
        # print("visivisitNumIntExp")
        print(numIntExp.numInt, end='')
    
    def visitNumFloatExp(self, numFloatExp):
        # print("visivisitNumFloatExp")
        print(numFloatExp.numFloat, end='')

    def visitIdExp(self, idExp):
        # print("visitIdExp")
        print(idExp.id, end='')

    def visitBooleanExp(self, booleanExp):
        print(booleanExp.boolValue, end='')

    def visitParamsCall(self, paramsCall):
        # print("visitParamsCall")
        print(paramsCall.id, '(', end='', sep='')
        paramsCall.params.accept(self)
        print(')', end='')

    def visitNoParamsCall(self, simpleCall):
        # print("visitSimpleCall")
        print(blank(), simpleCall.id, '()', end='', sep='')

    def visitCompoundParams(self, compoundParams):
        # print("visitCompoundParams")
        compoundParams.exp.accept(self)
        print(', ', end='')
        compoundParams.params.accept(self)

    def visitSingleParam(self, singleParam):
        # print("visitSingleParam")
        singleParam.exp.accept(self)

    