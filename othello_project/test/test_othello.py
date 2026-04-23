import textwrap
import pytest
from unittest.mock import MagicMock
import pytest_mock
import random
from src.othello_app.models.stone import Stone
from src.othello_app.models.field import Field
from src.othello_app.models.game import Game
from src.othello_app.models.othello import Othello
from src.othello_app.models.cpu import Cpu


fie = Field()
gam = Game(fie)
oth = Othello()
cpu = Cpu()


from unittest.mock import MagicMock
import pytest

def test_run_bulletproof(mocker):
    # 1. 各モックの作成
    mock_manager = MagicMock()
    mock_board = MagicMock()
    mock_cpu = MagicMock()

    # 2. 状態の初期設定
    mock_manager.turn = str(Stone.WHITE)
    mock_manager.put_stone.return_value = True
    
    #白の石を1度だけ置かせて、その後２回連続で石が置けない処理をし、ゲームを終了させる。
    mock_manager.has_valid_move.side_effect = [True, False, False]

    # スコア計算
    mock_board.board.count.side_effect = lambda color: 2 if color == str(Stone.BLACK) else 4

    # 3. インスタンス化
    oth = Othello(manager=mock_manager, othello_board=mock_board, cpu=mock_cpu)

    #石を置く場所を3,4で入力した場合を想定。
    mocker.patch("builtins.input", side_effect=["3", "4"])
    
    mock_print = mocker.patch("builtins.print")

    # 4. 実行
    oth.run()

    # 5. 検証
    # 少なくとも1回は(3, 4)で置こうとしたか
    mock_manager.put_stone.assert_any_call(3, 4)
    mock_print.assert_any_call("白の勝ちです！")