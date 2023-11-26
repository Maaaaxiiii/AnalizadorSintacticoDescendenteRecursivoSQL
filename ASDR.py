from TipoToken import TipoToken


class ASDR:
  def __init__(self, tokens):
      self.i = 0
      self.hayErrores = False
      self.preanalisis = tokens[self.i] if tokens else None
      self.tokens = tokens

  def parse(self):
      self.Q()

      if self.preanalisis.tipo == TipoToken.EOF and not self.hayErrores:
          print("Consulta correcta")
          return True
      else:
          print("Se encontraron errores")
          return False

    # Q -> select D from T
  def Q(self):
      self.match(TipoToken.SELECT)
      self.D()
      self.match(TipoToken.FROM)
      self.T()

    # D -> distinct P | P
  def D(self):
      if self.hayErrores:
          return

      if self.preanalisis.tipo == TipoToken.DISTINCT:
          self.match(TipoToken.DISTINCT)
          self.P()
      elif self.preanalisis.tipo == TipoToken.ASTERISCO or self.preanalisis.tipo == TipoToken.IDENTIFICADOR:
          self.P()
      else:
          self.hayErrores = True
          print("Se esperaba 'distinct' or '*' or 'identificador'")

    # P -> * | A
  def P(self):
      if self.hayErrores:
          return

      if self.preanalisis.tipo == TipoToken.ASTERISCO:
          self.match(TipoToken.ASTERISCO)
      elif self.preanalisis.tipo == TipoToken.IDENTIFICADOR:
          self.A()
      else:
          self.hayErrores = True
          print("Se esperaba '*' or 'identificador'")

    # A -> A2 A1
  def A(self):
      if self.hayErrores:
          return
      self.A2()
      self.A1()

    # A2 -> id A3
  def A2(self):
      if self.hayErrores:
          return

      if self.preanalisis.tipo == TipoToken.IDENTIFICADOR:
          self.match(TipoToken.IDENTIFICADOR)
          self.A3()
      else:
          self.hayErrores = True
          print("Se esperaba un 'identificador'")

    # A1 -> ,A | Ɛ
  def A1(self):
      if self.hayErrores:
          return

      if self.preanalisis.tipo == TipoToken.COMA:
          self.match(TipoToken.COMA)
          self.A()

    # A3 -> . id | Ɛ
  def A3(self):
      if self.hayErrores:
          return

      if self.preanalisis.tipo == TipoToken.PUNTO:
          self.match(TipoToken.PUNTO)
          self.match(TipoToken.IDENTIFICADOR)

    # T -> T2 T1
  def T(self):
      if self.hayErrores:
          return

      self.T2()
      self.T1()

    # T2 -> id T3
  def T2(self):
      if self.hayErrores:
          return

      if self.preanalisis.tipo == TipoToken.IDENTIFICADOR:
          self.match(TipoToken.IDENTIFICADOR)
          self.T3()
      else:
          self.hayErrores = True
          print("Se esperaba un 'identificador' de tabla")

    # T1 -> , T | Ɛ
  def T1(self):
      if self.hayErrores:
          return

      if self.preanalisis.tipo == TipoToken.COMA:
          self.match(TipoToken.COMA)
          self.T()

    # T3 -> id | Ɛ
  def T3(self):
    if self.hayErrores:
          return
    if(self.preanalisis.tipo == TipoToken.IDENTIFICADOR):
        self.match(TipoToken.IDENTIFICADOR);

  def match(self, tt):
      if self.preanalisis.tipo == tt:
          self.i += 1
          if self.i < len(self.tokens):
              self.preanalisis = self.tokens[self.i]
      else:
          self.hayErrores = True
          print("Error encontrado")
