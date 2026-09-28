from cancion import Cancion
from circulo import Circulo

### 2) En el archivo main.py, instanciar la clase “Cancion” 3 veces. ###
cancion1 = Cancion("Sweet Child O' Mine", 356, "Hard rock")
cancion2 = Cancion("Smells Like Teen Spirit", 301, "Rock")
cancion3 = Cancion("Wonderwall", 258, "Britpop")

### 3)​ En el archivo main.py, imprimir el valor del atributo genero para cada ###
###    instancia creada de la clase “Cancion”.                                ###
print(f"El genero de {cancion1.nombre} es {cancion1.genero}")
print(f"El genero de {cancion2.nombre} es {cancion2.genero}")
print(f"El genero de {cancion3.nombre} es {cancion3.genero}")

### 4)​ En el archivo main.py, modificar el valor del atributo genero de una de ###
###    las instancias de “Cancion” e imprimir nuevamente su valor.             ###
cancion2.establecerGenero("Grunge")
print(f"Ahora el genero de {cancion2.nombre} es {cancion2.genero}")

print("#########################################################")

### 6)​ En el archivo main.py, instanciar la clase “Circulo” 3 veces. ###
circulo1 = Circulo(5)
circulo2 = Circulo(10)
circulo3 = Circulo(20)

### 7)​ En el archivo main.py, imprimir el valor del diámetro para cada instancia ###
###    de “Circulo” creada.                                                      ###
print(circulo1.obtenerDiametro())
print(circulo2.obtenerDiametro())
print(circulo3.obtenerDiametro())

### 8)​ En el archivo main.py, imprimir el valor del atributo PI para cada ###
### instancia de “Circulo” creada.                                        ###
print(circulo1.PI)
print(circulo2.PI)
print(circulo3.PI)

### 9)​ En el archivo main.py, crear 2 instancias más de “Circulo” que tengan    ###
###    valores idénticos para el radio, e imprimir el resultado de compararlas  ###
###    utilizando el operador ==.                                               ###
circulo4 = Circulo(2)
circulo5 = Circulo(2)

### 10)​En el archivo main.py, imprimir el resultado de comparar los valores del ###
###    perímetro de cada instancia creada en el punto anterior.                 ###
print(circulo4 == circulo5)
print(circulo4.obtenerPerimetro() == circulo5.obtenerPerimetro())