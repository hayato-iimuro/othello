import textwrap
import pytest
import pytest_mock
from unittest.mock import MagicMock
import random
from src.othello_app.models.stone import Stone
from src.othello_app.models.field import Field
from src.othello_app.models.game import Game
from src.othello_app.models.othello import Othello
from src.othello_app.models.cpu import Cpu


fie = Field()
gem = Game(fie)
oth = Othello()
cpu = Cpu()


#以下Gameクラスのテスト
def test_flippable_point(capsys):

    gem.flippable_point()
    fie.display_board()

    captured = capsys.readouterr()

    expected_output = textwrap.dedent("""\
        ---------------------------------
        | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
        ---------------------------------
        | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
        ---------------------------------
        | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 |
        ---------------------------------
        | 0 | 0 | 5 | -1 | 1 | 0 | 0 | 0 |
        ---------------------------------
        | 0 | 0 | 0 | 1 | -1 | 5 | 0 | 0 |
        ---------------------------------
        | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 |
        ---------------------------------
        | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
        ---------------------------------
        | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
        ---------------------------------
    """)
    
    
    assert captured.out == expected_output


def test_has_valid_move():
    assert gem.has_valid_move() == True
    gem.flippable_point()
    assert gem.has_valid_move() == True



def test_put_stone():
    assert gem.put_stone(10,5) == False
    assert gem.put_stone(3, 3) == False
    assert gem.put_stone(1, 1) == False
    assert gem.put_stone(2, 3) == True



def test_can_flip():
    assert gem.can_flip(10, 5) == []
    assert gem.can_flip(2,3) == []
