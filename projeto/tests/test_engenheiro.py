# import pytest
# from projeto.tests.test_endereco import endereco_valido
# from projeto.classes.engenheiro import Engenheiro

# @pytest.fixture
# def pessoa_valida():
#     engenheiro = Engenheiro("Caio", "1234-5678", "Caioreal@gmail.com", endereco_valido, "2345")
#     return engenheiro

# def test_crea_valido(engenheiro_valido):
#     assert engenheiro_valido.crea == "2345"

# def test_mudar_crea_valido(engenheiro_valido):
#     engenheiro_valido.crea = "5135"
#     assert engenheiro_valido.crea == "5135"

# def test_crea_tipo_invalido():
#     with pytest.raises(TypeError, match="O crea deve se manter como tipo texto!"):
#         Engenheiro("Caio", "1234-5678", "Caioreal@gmail.com", endereco_valido, True)