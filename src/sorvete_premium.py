from sorvete import Sorvete

class SorvetePremium(Sorvete):
    def __init__(self, suporte=None, cobertura=None):
        super().__init__(preco=15, suporte=suporte, cobertura=cobertura)

    @property
    def sorvete_casquinha(self):
        return self._preco + 2, 'casquinha'

    @sorvete_casquinha.setter
    def sorvete_casquinha(self,_):
        self._preco += 2
        self._suporte = 'casquinha'

    @property
    def sorvete_copinho(self):
        return self._preco + 2, 'copinho'

    @sorvete_copinho.setter
    def sorvete_copinho(self,_):
        self._preco += 1
        self._suporte = 'copinho'
