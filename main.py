from cancion import Cancion

cancion1 = Cancion("Bohemian Rapsody", 355, "Rock opera")
cancion2 = Cancion("Smells Like Teen Spirit", 301, "Rock")
cancion3 = Cancion("Sweet Child O'Mine", 356, "Hard rock")

print(cancion1.obtenerGenero())
print(cancion2.obtenerGenero())
print(cancion3.obtenerGenero())

cancion2.establecerGenero("Grunge")
print(cancion2.obtenerGenero())