# import pytest
# from projeto.classes.abstracts.pessoa import Pessoa
# from projeto.tests.test_endereco import endereco_valido

# @pytest.fixture
# def pessoa_valida():
#     pessoa = Pessoa("Caio", "1234-5678", "Caioreal@gmail.com", endereco_valido)
#     return pessoa

# def test_nome_valido(pessoa_valida):
#     assert pessoa_valida.nome == "Caio"

# def test_numero_valido(pessoa_valida):
#     assert pessoa_valida.telefone == "1234-5678"

# def test_email_valido(pessoa_valida):
#     assert pessoa_valida.email == "Caioreal@gmail.com"

# def test_nome_tipo_invalido():
#     with pytest.raises(TypeError, match="O nome deve se manter como um texto!"):
#         Pessoa(22, "9876-5432", "Caioreal@gmail.com", endereco_valido)

# def test_nome_vazio():
#     with pytest.raises(TypeError, match="O nome não pode estar vazio!"):
#         Pessoa("", "9876-5432", "Caioreal@gmail.com", endereco_valido)

# def test_numero_tipo_valido():
#     with pytest.raises(TypeError, match="O telefone deve se manter como tipo texto!"):
#         Pessoa("Caio", 33, "Caioreal@gmail.com", endereco_valido)

# def test_email_tipo_valido():
#     with pytest.raises(TypeError, match="O email deve se manter como texto!"):
#         Pessoa("Caio", "9876-5432", 222, endereco_valido)