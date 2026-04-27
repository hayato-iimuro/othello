import textwrap
import pytest
import pytest_mock
import random
from src.othello_app.models.stone import Stone
from src.othello_app.models.field import Field
from src.othello_app.models.game import Game
from src.othello_app.models.othello import Othello
from src.othello_app.models.actors import Cpu, Player, GamePlayer
from src.othello_app.models import actors


fie = Field()
gem = Game(fie)
oth = Othello()
cpu = Cpu()
player = Player()


def test_display_name():
    assert cpu.display_name() == "CPU"
    assert player.display_name() == "Player"
    