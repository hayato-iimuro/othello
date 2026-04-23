
import textwrap
import pytest
from src.othello_app.models.field import Field
from src.othello_app.models.game import Game

fie = Field()
gem = Game(fie)


#Fieldクラスのテスト
def test_get_index():
    assert fie.get_index(2, 5) == 21

def test_display_board(capsys):
    

    fie.display_board()

    captured = capsys.readouterr()

    expected_output = textwrap.dedent("""\
             0    1    2    3    4    5    6    7
           -----------------------------------------
        0  |    |    |    |    |    |    |    |    |
           -----------------------------------------
        1  |    |    |    |    |    |    |    |    |
           -----------------------------------------
        2  |    |    |    |    |    |    |    |    |
           -----------------------------------------
        3  |    |    |    | ⚪️ | ⚫️ |    |    |    |
           -----------------------------------------
        4  |    |    |    | ⚫️ | ⚪️ |    |    |    |
           -----------------------------------------
        5  |    |    |    |    |    |    |    |    |
           -----------------------------------------
        6  |    |    |    |    |    |    |    |    |
           -----------------------------------------
        7  |    |    |    |    |    |    |    |    |
           -----------------------------------------
    """)
    
    # 前後の余計な空白を strip() で取り除いて比較するのがコツです
    assert captured.out == expected_output


def test_disc_inside():
    assert fie.disc_inside(8, 5) == False


#以下Gameクラスのテスト
def test_flippable_point():
    pass


def test_has_valid_move():
    assert gem.has_valid_move() == True


