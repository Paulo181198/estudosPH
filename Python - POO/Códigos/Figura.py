from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, cor):
        self.cor= cor
    
    @abstractmethod
    def calculoArea(self):
        pass

