import pytest
from projeto.classes.endereco import Endereco

@pytest.fixture
def endereco_valido():
    endereco = Endereco("Rua dos Curiós", "123", "apartamento 101", "12345-678", "Salvador")
    return endereco

def test_endereco_valido(endereco_valido):
    assert endereco_valido.logradouro == "Rua dos Curiós"
    assert endereco_valido.numero == "123"
    assert endereco_valido.complemento ==  "apartamento 101"
    assert endereco_valido.cep == "12345-678"
    assert endereco_valido.cidade == "Salvador"

def test_logradouro_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O logradouro deve ser um texto."):
        Endereco(123, "123", "apartamento 101", "12345-678", "Salvador")

def test_logradouro_vazio_retorna_mensagem():
    with pytest.raises(ValueError, match="O logradouro não pode estar vazio."):
        Endereco("", "123", "apartamento 101", "12345-678", "Salvador")

def test_numero_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O número deve ser um texto."):
        Endereco("Rua dos Curiós", True, "apartamento 101", "12345-678", "Salvador")

def test_numero_vazio_retorna_mensagem():
    with pytest.raises(ValueError, match="O número não pode estar vazio."):
        Endereco("Rua dos Curiós", "", "apartamento 101", "12345-678", "Salvador")

def test_complemento_tipo_invalido_retorna_mesnagem():
    with pytest.raises(TypeError, match="O complemento deve ser um texto."):
        Endereco("Rua dos Curiós", "123", True, "12345-678", "Salvador")

def test_complemento_vazio_retorna_mensagem():
    with pytest.raises(ValueError, match="O complemento não pode estar vazio."):
        Endereco("Rua dos Curiós", "123", "", "12345-678", "Salvador")

def test_cep_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O CEP deve ser um texto."):
        Endereco("Rua dos Curiós", "123", "apartamento 101", 123, "Salvador")

def test_cep_vazio_retorna_mensagem():
    with pytest.raises(ValueError, match="O CEP não pode estar vazio."):
        Endereco("Rua dos Curiós", "123", "apartamento 101", "", "Salvador")

def test_cidade_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="A cidade deve ser um texto."):
        Endereco("Rua dos Curiós", "123", "apartamento 101", "12345-678", 123)

def test_cidade_vazio_retorna_mensagem():
    with pytest.raises(ValueError, match="O cidade não pode estar vazia."):
        Endereco("Rua dos Curiós", "123", "apartamento 101", "12345-678", "")