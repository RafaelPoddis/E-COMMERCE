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
        elif tipo == "eletronic":
            return Eletronic(nome, preco)
        elif tipo == "beauty":
            return Beauty(nome, preco)
        elif tipo == "toys":
            return Toys(nome, preco)
        elif tipo == "books":
            return Books(nome, preco)
        elif tipo == "gorceries":
            return Groceries
        else:
            raise ValueError("Tipo invalido de produto!")
