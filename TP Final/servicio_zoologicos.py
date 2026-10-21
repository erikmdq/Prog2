import json
import zoologico
import jirafa
import aguila
import rinoceronte
import empleado


class ServicioZoologicos:

    def obtener_por_id(self, id_zoologico):

        with open("datos.json", "r", encoding="utf-8") as f:
            datos = json.load(f)

        zoologicos = []

        for objeto in datos:
            zoologicos.append(self.__extraer_zoologico(objeto))

        for zoo in zoologicos:
            if zoo.obtener_id() == int(id_zoologico):
                return zoo

        return None

    def __extraer_zoologico(self, objeto):
        zoo = zoologico.Zoologico(objeto.get("id"), objeto.get("nombre"))

        empleados = objeto.get("empleados")
        for emp in empleados:
            empleado_registro = empleado.Empleado(
                emp.get("id"), emp.get("nombres"), emp.get("apellidos")
            )
            zoo.agregar_empleado(empleado_registro)

        animales = objeto.get("animales")

        for ani in animales:
            match ani.get("tipo"):
                case "jirafa":
                    animal_registro = jirafa.Jirafa(
                        ani.get("id"),
                        ani.get("nombre"),
                        ani.get("id_cuidador_principal"),
                        ani.get("largo_cuello"),
                    )
                    zoo.agregar_animal(animal_registro)
                case "aguila":
                    animal_registro = aguila.Aguila(
                        ani.get("id"),
                        ani.get("nombre"),
                        ani.get("id_cuidador_principal"),
                        ani.get("largo_alas"),
                        ani.get("largo_pico"),
                    )
                    zoo.agregar_animal(animal_registro)
                case "rinoceronte":
                    animal_registro = rinoceronte.Rinoceronte(
                        ani.get("id"),
                        ani.get("nombre"),
                        ani.get("id_cuidador_principal"),
                        ani.get("largo_cuerno"),
                    )
                    zoo.agregar_animal(animal_registro)

        return zoo
