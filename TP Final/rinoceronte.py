import animal

class Rinoceronte(animal.Animal):
    # --- Clase Rinoceronte, hereda de clase Animal --- #
    # --- Constructor: sobreescribe el método __init__ de la clase Animal --- #
    def __init__(self, id, id_cuidador_principal, largo_cuerno):
        # --- Llama al constructor de la clase base (Animal) para inicializar los atributos heredados --- #
        super().__init__(id, nombre, id_cuidador_principal)
        self.__largo_cuerno = largo_cuerno

    # -- Comandos -- #
    def establecer_largo_cuerno(self, largo_cuerno):
        self.__largo_cuerno = largo_cuerno

    # -- Consultas -- #
    def obtener_largo_cuerno(self):
        return self.__largo_cuerno