import pytest
from projeto.classes.medico import Medico
from projeto.tests.test_endereco import endereco_valido

@pytest.fixture
def medico_valido():
    medico = Medico("Lucas", "1234-5678", "lucas@email.com", endereco_valido, "123456789-BA", 5000.0)
    return medico

def test_medico_valido(medico_valido):
    assert medico_valido.nome == "Lucas"
    assert medico_valido.telefone == "1234-5678"
    assert medico_valido.email == "lucas@email.com"
    assert medico_valido.endereco == endereco_valido
    assert medico_valido.crm == "123456789-BA"
    assert medico_valido.salario_final() == 7000.0

def test_crm_tipo_invalido_retorna_mensagem():
    with pytest.raises(TypeError, match="O CRM deve ser alfa-numérico."):
        Medico("Lucas", "1234-5678", "lucas@email.com", endereco_valido, True, 5000.0)

def test_crm_vazio_retorna_mensagem():
    with pytest.raises(ValueError, match= "O CRM não pode estar vazio."):
        Medico("Lucas", "1234-5678", "lucas@email.com", endereco_valido, "", 5000.0)

def test_crm_tam_errado_retorna_mensagem():
    with pytest.raises(ValueError, match= "O tamanho do CRM não pode ser diferente de 12 caractéres."):
        Medico("Lucas", "1234-5678", "lucas@email.com", endereco_valido, "12345678-BA", 5000.0)