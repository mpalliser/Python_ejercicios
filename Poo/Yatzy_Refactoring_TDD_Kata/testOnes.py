import pytest
from yatzy import Yatzy

# Chance
# The player scores the sum of all dice, no matter what they read.


def testOnes():
    assert 1 == Yatzy.ones(1, 2, 3, 4, 5)
    assert 2 == Yatzy.ones(1, 1, 3, 4, 5)
    assert 3 == Yatzy.ones(1, 1, 1, 4, 5)