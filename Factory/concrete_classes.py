from abc import ABC, abstractmethod

class Product(ABC):

    def __init__(self, nome, preco):
        self.name = name
        self.preco = preco

    def __str__(self):
        return f"Nome: {self.nome}\nPreço: {self.preco}"

class Eletronic(Product):
    pass

class Beauty(Product):
    pass

class Clothing(Product):
    pass

class Toys(Product):
    pass

class Books(Product):
    pass

class Groceries(Product):
    pass
