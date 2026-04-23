import textwrap
import pytest
import pytest_mock
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


#Fieldクラスのテスト
def test_get_index():
    x = y = random.randint(0, 100)
    assert fie.get_index(2, 5) == 21
    assert fie.get_index(10, 4) == 84
    assert fie.get_index(64, 30) == 64 * 8 + 30
    assert fie.get_index(x, y) == x * 8 + y


def test_display_board(capsys):
    

    fie.display_board()

    captured = capsys.readouterr()

    expected_output = textwrap.dedent("""\
        ---------------------------------
        | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
        ---------------------------------
        | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
        ---------------------------------
        | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
        ---------------------------------
        | 0 | 0 | 0 | -1 | 1 | 0 | 0 | 0 |
        ---------------------------------
        | 0 | 0 | 0 | 1 | -1 | 0 | 0 | 0 |
        ---------------------------------
        | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
        ---------------------------------
        | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
        ---------------------------------
        | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
        ---------------------------------
    """)
    
    assert captured.out == expected_output


def test_disc_inside():
    assert fie.disc_inside(8, 5) == False
    assert fie.disc_inside(7, 7) == True
    assert fie.disc_inside(0, 0) == True