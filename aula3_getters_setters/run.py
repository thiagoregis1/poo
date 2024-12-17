class MinhaClasse:
    def __init__(self) -> None:
        self.__valor = None

    def setter(self, valor: int) -> None:
        self.__valor = valor

    # @propertyi
    def getter(self) -> int:
        return self.__valor

my_class = MinhaClasse()
#my_class.valor = 3 #mudando o __valor para valor  e ferindo o encapsulamento
# my_class.setter(42)
# valor = my_class.getter()
# print(valor)

my_class.setter(22)
print(my_class.getter)
