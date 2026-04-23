
import textwrap
import pytest
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


#Othelloクラスのテスト
def test_run():
    pass


#Cpuクラスのテスト
def test_cpu_choice():
    assert 0 <= cpu.cpu_choice() <= 7
    assert cpu.cpu_choice() != str

