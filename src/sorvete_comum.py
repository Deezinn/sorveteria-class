from sorvete import Sorvete

class SorveteComum(Sorvete):
   def __init__(self, suporte=None, cobertura=None):
      super().__init__(preco=15, suporte=suporte, cobertura=cobertura)

   @property
   def sorvete_casquinha(self):
      return 'R$15 do sorvete e R$2 da casquinha.'

   @property
   def sorvete_copinho(self):
      return 'R$15 do sorvete e R$1 do copinho.'

   @property
   def sorvete_cobertura(self):
      return 'R$15 do sorvete e R$1 de acrescimo se for simples ou R$2 se for especial.'

   @sorvete_casquinha.setter
   def sorvete_casquinha(self, adicional):
      self._preco += adicional
      self._suporte = 'casquinha'


   @sorvete_copinho.setter
   def sorvete_copinho(self, adicional):
      self._preco += adicional
      self._suporte = 'copinho'

   @sorvete_cobertura.setter
   def sorvete_cobertura(self, cobertura):
      if cobertura == 'simples':
         self._preco += 1
      elif cobertura == 'especial':
         self._preco += 2
      else:
         raise ValueError("Cobertura deve ser 'simples' ou 'especial'")
      self._cobertura = cobertura
