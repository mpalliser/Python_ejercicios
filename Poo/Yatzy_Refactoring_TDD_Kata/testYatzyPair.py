import pytest
from yatzy import Yatzy

# Chance
# The player scores the sum of all dice, no matter what they read.


def test_chance():
    # iterar sobre *args evita codigo cableado a 5 argumentos
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)  

def test_yatzy():
    ### Yatzy: 
#If all dice have the same number,
#the player scores 50 points. 
    assert 50 == Yatzy.yatzy(1,1,1,1,1)
    assert 0 == Yatzy.yatzy(1,1,2,1,1)

def test_ones():
    #The player scores the sum of the dice that reads one.
    assert 2 == Yatzy.ones(1,1,2,4,4)
    assert 1 == Yatzy.ones(2,3,2,5,1)
    assert 0 == Yatzy.ones(3,3,3,4,5)

  
def test_twos():
    assert 4 == Yatzy.twos(2,3,2,5,1)

def test_threes():
    assert 3 == Yatzy.threes(2,3,2,5,1)
    assert 6 == Yatzy.threes(3,3,2,5,1)
    assert 9 == Yatzy.threes(3,3,3,5,1)

@pytest.fixture
def inyector():
    # Es el setup de unittest o de JUnit
    tirada = Yatzy(1, 2, 3, 4, 5)
    return tirada


def test_fours(inyector):
    # Es necesario un objeto ya creado
    valorEsperado = 4
    # No puedo testear con fixtures = inyeccion de dependencias
    # los metodos estaticos como chance()
    assert valorEsperado == inyector.fours()


def test_score_pair():
    # iterar sobre *args evita codigo cableado a 5 argumentos
    assert 6 == Yatzy.pair(1, 1, 3, 3, 5)
    assert 2 == Yatzy.pair(1, 1, 3, 4, 6)
    assert 10 == Yatzy.pair(4, 5, 5, 6, 1)
    assert 8 == Yatzy.pair(2, 4, 4, 3, 3)
    assert 12 == Yatzy.pair(6, 6, 1, 3, 3)
    assert 0 == Yatzy.pair(6, 4, 1, 2, 3)

def test_two_pair():
    #If there are two pairs of dice with the same number, the
    #player scores the sum of these dice. 
    assert 8 == Yatzy.two_pair(1,1,2,3,3)
    assert 0 == Yatzy.two_pair(1,1,2,3,4)
    assert 0 == Yatzy.two_pair(1,4,2,5,3)
    assert 6 == Yatzy.two_pair(1,1,2,2,2)
    assert 0 == Yatzy.two_pair(1,3,3,3,3)

def test_three_of_a_kind():
    '''
    If there are three dice with the same number, the player
    scores the sum of these dice. 
    '''
    assert 9 == Yatzy.three_of_a_kind(5,4,3,3,3)
    assert 0 == Yatzy.three_of_a_kind(1,1,2,3,3)
    assert 12 == Yatzy.three_of_a_kind(4,4,4,4,1)

def test_four_of_a_kind():
    '''
    If there are four dice with the same number, the player
    scores the sum of these dice.  
    '''
    assert 24 == Yatzy.four_of_a_kind(6,6,6,6,1)
    assert 0 == Yatzy.four_of_a_kind(2,2,2,1,1)
    assert 4 == Yatzy.four_of_a_kind(3,1,1,1,1)
    assert 12 == Yatzy.four_of_a_kind(3,3,3,3,3)

  

