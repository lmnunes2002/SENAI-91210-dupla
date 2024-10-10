from classes.abstracts.pessoa import Pessoa
from classes.endereco import Endereco

class Engenheiro(Pessoa):
    # Construtores
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crea: str) -> None:
        super().__init__(nome, telefone, email, endereco)

        self.crea = self._verificar_crea(crea)

    # Método abstrato
    def _verificar_crea(self,valor):
        """Método para verificar crea"""

        self._verificar_crea_tipo_invalido(valor)

        self.crea = valor
        return self.crea
    
    def _verificar_crea_tipo_invalido(self,valor):
        """Método para verificar crea inválido"""
        if not isinstance(valor, str):
            raise TypeError("O crea deve se manter como tipo texto!")

    def salario_final(self) -> float:
        return self.salario * 1.10
    
    def inicializar(self):
        return super().inicializar()

        
    def __str__(self) -> str:
        return (
            f"\nEngenheiro:"
            f"{super().__str__()}"
            f"\nNúmero de CREA: {self.crea}"
        )