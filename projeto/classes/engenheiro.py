from projeto.classes.abstracts.pessoa import Pessoa
from projeto.classes.endereco import Endereco

class Engenheiro(Pessoa):
    # Construtores
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crea: str, salario_final: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = self._verificar_crea(crea)
        self.salario_final_base_engenheiro = salario_final

    # Método de verificação.
    def _verificar_crea(self,valor):
        """Método para verificar CREA"""
        self._verificar_crea_tipo_invalido(valor)
        self._verificar_crea_vazio(valor)

        self.crea = valor
        return self.crea
    
    # Método auxiliar.
    def inicializar(self):
        return super().inicializar()

    # Método auxiliar.      
    def _verificar_crea_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O crea deve se manter como tipo texto!")

    # Método auxiliar.
    def _verificar_crea_vazio(self,valor):
        if not valor.strip():
            raise ValueError("O CREA não pode estar vazio.")

    # Implementando método abstrato.
    def salario_final(self) -> float:
        return self.salario_final_base_engenheiro * 1.10