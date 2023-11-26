class Token:
  def __init__(self, tipo, lexema, posicion):
      self.tipo = tipo
      self.lexema = lexema
      self.posicion = posicion

  def __eq__(self, other):
      if not isinstance(other, Token):
          return False

      return self.tipo == other.tipo

  def __str__(self):
      return f"{self.tipo} {self.lexema} "