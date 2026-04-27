import textwrap
import pytest
import pytest_mock
import random
from src.othello_app.models.stone import Stone
from src.othello_app.models.field import Field
from src.othello_app.models.game import Game
from src.othello_app.models.othello import Othello
from src.othello_app.models.actors import Cpu


fie = Field()
gem = Game(fie)
oth = Othello()
cpu = Cpu()

