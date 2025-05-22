class Sorvete:
    def __init__(self, preco, suporte, cobertura):
        self._preco = preco
        self._suporte = suporte
        self._cobertura = cobertura

    @property
    def preco(self):
        return self._preco

    @property
    def suporte(self):
        return self._suporte

    @property
    def cobertura(self):
        return self._cobertura

