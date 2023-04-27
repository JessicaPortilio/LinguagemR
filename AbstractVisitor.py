from abc import abstractmethod, ABCMeta

class AbstractVisitor(metaclass=ABCMeta):

    @abstractmethod
    def visitFuncDeclConcrete(self, funcDecl):
        pass

    @abstractmethod
    def visitSignatureConcrete(self, signature):
        pass

    @abstractmethod
    def visitSingleSigParams(self, singleSigParams):
        pass

    @abstractmethod
    def visitCompoundSigParams(self, compoundSigParams):
        pass

    @abstractmethod
    def visitBodyConcrete(self, body):
        pass

    @abstractmethod
    def visitSingleStm(self, singlestm):
        pass

    @abstractmethod
    def visitCompoundStm(self, compoundStm):
        pass

    @abstractmethod
    def visitStmExp(self, stmExp):
        pass

    @abstractmethod
    def visitStmWhile(self, stmWhile):
        pass

    @abstractmethod
    def visitStmReturn(self, stmReturn):
        pass

    @abstractmethod
    def visitAssignExp(self, assignExp):
        pass

    @abstractmethod
    def visitSomaExp(self, somaExp):
        pass
    
    @abstractmethod
    def visitMenosExp(self, menosExp):
        pass

    @abstractmethod
    def visitVezesExp(self, VezesExp):
        pass

    @abstractmethod
    def visitDividirExp(self,DividirExp):
        pass

    @abstractmethod
    def visitPotExp(self, potExp):
        pass

    @abstractmethod
    def visitIgualExp(self, IgualExp):
        pass

    @abstractmethod
    def visitMaiorExp(self, MaiorExp):
        pass

    @abstractmethod
    def visitMenorExp(self,MenorExp):
        pass
    
    @abstractmethod
    def visitMaiorIgualExp(self, MaiorIgualExp):
        pass

    @abstractmethod
    def visitMenorIgualExp(self, MenorIgualExp):
        pass

    @abstractmethod
    def visitDiferenteExp(self, DiferenteExp):
        pass

    @abstractmethod
    def visitAndExp(self, AndExp):
        pass
    
    @abstractmethod
    def visitAndVetorExp(self,AndVetorExp):
        pass

    @abstractmethod
    def visitOrExp(self, OrExp):
        pass

    @abstractmethod
    def visitOrVetorExp(self,OrVetorExp):
        pass

    @abstractmethod
    def visitXorExp(self, XorExp):
        pass

    @abstractmethod
    def visitNotExp(self, NotExp):
        pass

    @abstractmethod
    def visitCallExp(self, callExp):
        pass

    @abstractmethod
    def visitNumIntExp(self, numIntExp):
        pass

    @abstractmethod
    def visitNumFloatExp(self, numFloatExp):
        pass

    @abstractmethod
    def visitIdExp(self, idExp):
        pass

    @abstractmethod
    def visitBooleanExp(self, booleanExp):
        pass

    @abstractmethod
    def visitParamsCall(self, paramsCall):
        pass

    @abstractmethod
    def visitNoParamsCall(self, simpleCall):
        pass

    @abstractmethod
    def visitCompoundParams(self, compoundParams):
        pass

    @abstractmethod
    def visitSingleParam(self, singleParam):
        pass