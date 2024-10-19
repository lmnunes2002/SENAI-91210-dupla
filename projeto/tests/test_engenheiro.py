import pytest
from projeto.classes.engenheiro import Engenheiro
from projeto.tests.test_endereco import endereco_valido

@pytest.fixture
def engenheiro_valido():
    engenheiro = Engenheiro("Caio", "1234-5678", "Caioreal@gmail.com", endereco_valido, "2345", "3000")
    return engenheiro

def test_crea_valido(engenheiro_valido):
    assert engenheiro_valido.crea == "2345"

def test_mudar_crea_valido(engenheiro_valido):
    engenheiro_valido.crea = "5135"
    assert engenheiro_valido.crea == "5135"

def test_mudar_salario_final(engenheiro_valido):
    engenheiro_valido.salario_final = "6000"
    assert engenheiro_valido.salario_final == "6000"

def test_crea_tipo_invalido():
    with pytest.raises(TypeError, match="O crea deve se manter como tipo texto!"):
        Engenheiro("Caio", "1234-5678", "Caioreal@gmail.com", endereco_valido, True, "3000")

def test_crea_vazio():
    with pytest.raises(ValueError, match= "O CREA não pode estar vazio."):
        Engenheiro("Caio", "1234-5678", "Caioreal@gmail.com", endereco_valido, "", "3000")
