from classes.endereco import Endereco
from abc import ABC, abstractmethod

class Pessoa(ABC):
    # Construtor
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = self._verificar_nome(nome)
        self.telefone = self._verificar_telefone(telefone)
        self.email = self._verificar_email(email)
        self.endereco = endereco

    # Método abstrato
    @abstractmethod
    def salario_final(self) -> float:
        pass

    def _verificar_nome(self,valor):
        """Método para verificar nome"""
    
        self.__verificar_nome_tipo_invalido(valor)
        self.__verificar_nome_vazio(valor)

        self.nome = valor
        return self.nome
    
    def __verificar_nome_tipo_invalido(self,valor):
        """Método para verificar nome inválido"""
    
        if not isinstance(valor, str):
            raise TypeError("O nome deve se manter como um texto.")
        
    def __verificar_nome_vazio(self,valor):
        """Método para verificar nome vazio"""

        if not valor.strip():
            raise TypeError("O nome não pode estar vazio.")
        
    def _verificar_telefone(self,valor):
        """Método para verificar telefone"""
    
        self._verificar_telefone_tipo_invalido(valor)
    
        self.telefone = valor
        return self.telefone
    
    def _verificar_telefone_tipo_invalido(self,valor):
        """Método para verificar telefone inválido"""
        
        if not isinstance(valor, str):
            raise TypeError("O telefone deve se manter como tipo texto.")
        
    def _verificar_email(self,valor):
        """Método para verificar email"""
    
        self._verificar_email_tipo_invalido(valor)

        self.email = valor
        return self.email
    
    def _verificar_email_tipo_invalido(self,valor):
        """Método para verificar email inválido"""

        if not isinstance(valor, str):
            raise TypeError("O email deve se manter como texto.")
    

    
    def __str__(self) -> str:
        return (
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\nEndereço: {self.endereco}"
        )