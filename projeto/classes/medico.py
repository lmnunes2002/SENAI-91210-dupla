from projeto.classes.abstracts.pessoa import Pessoa
from projeto.classes.endereco import Endereco

class Medico(Pessoa):
    # Construtor.
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crm: str, salarioFinal: float) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = self._verificar_crm(crm)
        self.salarioFinal = self.salario_final(salarioFinal)

    # Método de verificação.
    def _verificar_crm(self, valor):
        """Método para verificar CRM"""
        self.__verificar_crm_invalido(valor)
        self.__verificar_crm_vazio(valor)
        self.__verificar_crm_tam(valor)

        self.crm = valor
        return valor
    
        # Método auxiliar
    def __verificar_crm_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O CRM deve ser alfa-numérico.")
        
    # Método auxiliar.
    def __verificar_crm_vazio(self, valor):
        if not valor.strip():
            raise ValueError("O CRM não pode estar vazio.")
        
    # Método auxiliar.
    def __verificar_crm_tam(self, valor):
        if len(valor) != 12:
            raise ValueError("O tamanho do CRM não pode ser diferente de 12 caractéres.")
        
   # Implementando o método abstrato.
    def salario_final(self) -> float:
        return self.salario_base  