import animal


class Aguila(animal.Animal):
    def __init__(self, id, nombre, id_cuidador_principal, largo_alas, largo_pico):
            super().__init__(id, nombre, id_cuidador_principal)
            self.__largo_alas = largo_alas
            self.__largo_pico = largo_pico

