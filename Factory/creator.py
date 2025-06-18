from abc import ABC, abstractmethod
from Factory.concrete_classes import *

class Interface(ABC):

    @abstractmethod
    def createPoduct(self, tipo, nome, preco):
        pass

class Creator(Interface):

    def createPoduct(self, tipo, nome, preco):
        if tipo == "clothing":
            return Clothing(nome, preco)
