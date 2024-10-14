import pytest
from projeto.classes.abstracts.pessoa import Pessoa
from projeto.classes.endereco import Endereco

@pytest.fixture
def pessoa_valida():
    pessoa = Pessoa("Caio", "1234-5678", "Caioreal@gmail.com", Endereco("Rua Fernando de Noronha", "6", "N/A", "4128", "Salvador"))
    return pessoa

def test_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Caio"

def test_alterar_nome_valido(pessoa_valida):
    pessoa_valida.nome = "Lucas"
    assert pessoa_valida.nome == "Lucas"

def test_numero_valido(pessoa_valida):
    assert pessoa_valida.telefone == "9876-5432"

def test_alterar_numero_valido(pessoa_valida):
    pessoa_valida.telefone = "2345-6789"
    assert pessoa_valida.telefone == "2345-6789"

def test_email_valido(pessoa_valida):
    assert pessoa_valida.email == "Caioreal@gmail.com"

def test_alterar_email_valido(pessoa_valida):
    pessoa_valida.email = "Lucaix@gmail.com"
    assert pessoa_valida.email == "Lucaix@gmail.com"

def test_nome_tipo_invalido():
    with pytest.raises(TypeError, match="O nome deve se manter como um texto!"):
        Pessoa(22, "9876-5432", "Caioreal@gmail.com", Endereco("Rua Fernando de Noronha", "6", "N/A", "4128", "Salvador"))

def test_nome_vazio():
    with pytest.raises(TypeError, match="O nome não pode estar vazio!"):
        Pessoa("", "9876-5432", "Caioreal@gmail.com", Endereco("Rua Fernando de Noronha", "6", "N/A", "4128", "Salvador"))

def test_numero_tipo_valido():
    with pytest.raises(TypeError, match="O telefone deve se manter como tipo texto!"):
        Pessoa("Caio", 33, "Caioreal@gmail.com", Endereco("Rua Fernando de Noronha", "6", "N/A", "4128", "Salvador"))

def test_email_tipo_valido():
    with pytest.raises(TypeError, match="O email deve se manter como texto!"):
        Pessoa("Caio", "9876-5432", 222, Endereco("Rua Fernando de Noronha", "6", "N/A", "4128", "Salvador"))