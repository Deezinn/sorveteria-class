from sorvete import Sorvete

class SorveteComum(Sorvete):
    def __init__(self, suporte=None, cobertura=None):
        super().__init__(preco=10, suporte=suporte, cobertura=cobertura)
