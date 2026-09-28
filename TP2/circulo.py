### 5) ###

class Circulo():
  PI = 3.14
  def __init__(self, radio):
    self.radio = radio

  def establecer_Radio(self, radio):
    self.radio = radio

  def obtenerRadio(self):
    return self.radio

  def obtenerDiametro(self):
    return (self.radio * 2)

  def obtenerArea(self):
    return self.radio**2 * Circulo.PI

  def obtenerPerimetro(self):
    return self.radio * self.radio * Circulo.PI