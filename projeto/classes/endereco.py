class Endereco:
    # Construtor.
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = self._verificar_logradouro(logradouro)
        self.numero = self._verificar_numero(numero)
        self.complemento = self._verificar_complemento(complemento)
        self.cep = self._verificar_cep(cep)
        self.cidade = cidade
    
    # Método para verificação.
    def _verificar_logradouro(self, valor):
        """Método para verificação de logradouro"""
        self.__verificar_logradouro_tipo_invalido(valor)
        self.__verificar_logradouro_vazio(valor)

        self.logradouro = valor
        return self.logradouro
    
    # Método auxiliar.
    def __verificar_logradouro_tipo_invalido(self, valor):
        """Método auxiliar para verificação de tipo para logradouro"""
        if not isinstance(valor, str):
            raise TypeError("O logradouro deve ser um texto.")
        
    # Método auxiliar.
    def __verificar_logradouro_vazio(self, valor):
        """Método auxiliar para verificação de logradouro vazio"""
        if not valor.strip():
            raise ValueError("O logradouro não pode estar vazio.")
        
   # Método para verificação.
    def _verificar_numero(self, valor):
        """Método para verificação de número"""
        self.__verificar_numero_tipo_invalido(valor)
        self.__verificar_numero_vazio(valor)

        self.numero = valor
        return self.numero
    
    # Método auxiliar.
    def __verificar_numero_tipo_invalido(self, valor):
        """Método auxiliar para verificação de tipo para número"""
        if not isinstance(valor, str):
            raise TypeError("O número deve ser um texto.")
        
    # Método auxiliar.
    def __verificar_numero_vazio(self, valor):
        """Método auxiliar para verificação de número vazio"""
        if not valor.strip():
            raise ValueError("O número não pode estar vazio.")
        
 # Método para verificação.
    def _verificar_complemento(self, valor):
        """Método para verificação de complemento"""
        self.__verificar_complemento_tipo_invalido(valor)
        self.__verificar_complemento_vazio(valor)

        self.complemento = valor
        return self.complemento
    
    # Método auxiliar.
    def __verificar_complemento_tipo_invalido(self, valor):
        """Método auxiliar para verificação de tipo para complemento"""
        if not isinstance(valor, str):
            raise TypeError("O complemento deve ser um texto.")
        
    # Método auxiliar.
    def __verificar_complemento_vazio(self, valor):
        """Método auxiliar para verificação de complemento vazio"""
        if not valor.strip():
            raise ValueError("O complemento não pode estar vazio.")
        
    # Método para verificação.
    def _verificar_cep(self, valor):
        """Método para verificação de CEP"""
        self.__verificar_cep_tipo_invalido(valor)
        self.__verificar_cep_vazio(valor)

        self.cep = valor
        return self.cep
    
    # Método auxiliar.
    def __verificar_cep_tipo_invalido(self, valor):
        """Método auxiliar para verificação de tipo para CEP"""
        if not isinstance(valor, str):
            raise TypeError("O CEP deve ser um texto.")
        
    # Método auxiliar.
    def __verificar_cep_vazio(self, valor):
        """Método auxiliar para verificação de CEP vazio"""
        if not valor.strip():
            raise ValueError("O CEP não pode estar vazio.")

    # Método para verificação.
    def _verificar_cidade(self, valor):
        """Método para verificação de cidade"""
        self.__verificar_cidade_tipo_invalido(valor)
        self.__verificar_cidade_vazio(valor)

        self.cidade = valor
        return self.cidade
    
    # Método auxiliar.
    def __verificar_cidade_tipo_invalido(self, valor):
        """Método auxiliar para verificação de tipo para cidade"""
        if not isinstance(valor, str):
            raise TypeError("A cidade deve ser um texto.")
        
    # Método auxiliar.
    def __verificar_cidade_vazio(self, valor):
        """Método auxiliar para verificação de cidade vazia"""
        if not valor.strip():
            raise ValueError("O cidade não pode estar vazia.")