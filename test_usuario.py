from dominio import Usuario , Leilao
import pytest

@pytest.fixture
def vini():
    return Usuario('Vini',100)

@pytest.fixture
def leilao():
    return Leilao('Celular')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(vini,leilao):
    vini.propoe.lance(Leilao, 50.0)
    assert vini.carteira == 50.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(vini,leilao):
    vini.propoe.lance(Leilao, 1.0)
    assert vini.carteira == 99.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(vini,leilao):

    vini.propoe.lance(Leilao, 100.0)
    assert vini.carteira == 0.0

def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira(vini,leilao):
    with pytest.raises(ValueError):
        vini.propoe.lance(Leilao, 200.0)
