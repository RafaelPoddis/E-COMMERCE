from abc import ABC, abstractmethod
from enum import Enum

class UserType(Enum):
    VIP = "vip"
    BASE = "base"

class User(ABC):
    
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email
        self.tipo = UserType.BASE

    def __str__(self):
        return f"Nome: {self.nome}\nTipo: {self.tipo}"
    
    def set_tipo(self, tipo):
        self.tipo = tipo
