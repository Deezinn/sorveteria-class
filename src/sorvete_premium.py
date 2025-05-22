from sorvete import Sorvete

class SorvetePremium(Sorvete):
    def __init__(self, preco=15, suporte=None, cobertura=None):
        super().__init__(preco, suporte, cobertura)

    @property
    def sorvete_casquinha(self):
        self._preco += 2
        self._suporte = 'casquinha'
        return self._preco, self._suporte

    @sorvete_casquinha.setter
    def sorvete_casquinha(self,_):
        self._preco += 2
        self._suporte = 'casquinha'

    @property
    def sorvete_copinho(self):
        self._preco += 1
        self._suporte = 'copinho'
        return self._preco, self._suporte

    @sorvete_copinho.setter
    def sorvete_copinho(self,_):
        self._preco += 1
        self._suporte = 'copinho'

