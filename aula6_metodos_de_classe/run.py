class MinhaClasse:

    estatico = "lhama"

    def __init__(self, estado) -> None:
        self.__estado = estado
    
    def print_variavel_classe(self):
        print(f"print_variavel_classe: {self.estatico}")
    
    @classmethod
    def alteracao_variavel_classe(cls):
        cls.estatico = "algumacoisa"

obj1 = MinhaClasse("wqewTrue")
obj2 = MinhaClasse(True)


obj1.print_variavel_classe()
# obj1.alteracao_variavel_classe()

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)
