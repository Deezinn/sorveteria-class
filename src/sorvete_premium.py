from sorvete import Sorvete

class SorvetePremium(Sorvete):
    def __init__(self, suporte=None, cobertura=None):
        super().__init__(preco=15, suporte=suporte, cobertura=cobertura)

    @property
    def sorvete_casquinha(self):
        return self._preco, 'casquinha'

    @property
    def sorvete_copinho(self):
        return self._preco, 'copinho'

    @property
    def sorvete_cobertura(self):
        return self._preco, self._cobertura

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
            print('erro')
            
        self._cobertura = cobertura


sp = SorvetePremium()
sp.sorvete_cobertura = 'simples'
print(sp.sorvete_cobertura)
