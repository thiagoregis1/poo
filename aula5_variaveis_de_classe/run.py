class MinhaClasse:

    estatico = "lhama"

    def __init__(self, estado) -> None:
        self.__estado = estado
        print(self.__estado)

obj1 = MinhaClasse("wqewTrue")
obj2 = MinhaClasse(True)

MinhaClasse.estatico = "programador"
obj1.estatico = "olá mundo"

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)
