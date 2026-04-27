import textwrap
import pytest
from unittest.mock import MagicMock
import random
from src.othello_app.models.stone import Stone
from src.othello_app.models.field import Field
from src.othello_app.models.game import Game
from src.othello_app.models.othello import Othello
from src.othello_app.models.actors import Cpu


fie = Field()
gam = Game(fie)

cpu = Cpu()


from unittest.mock import MagicMock
import pytest


def test_players_selecrt(mocker):

    othello = Othello()

    mocker.patch("builtins.input", side_effect=["1", "2"])
    
    mock_print = mocker.patch("builtins.print")

    othello.players_select()

    mock_print.assert_any_call("黒:Player 白:CPU で対戦を開始します。")

    

def test_result(mocker):

    mock_manager = MagicMock()
    mock_board = MagicMock()

    #黒に48を白に16を返す返す
    mock_board.board.count.side_effect = lambda color: 48 if color == str(Stone.BLACK) else 16


    oth = Othello(manager=mock_manager, othello_board=mock_board)
    mock_print = mocker.patch("builtins.print")

    oth.result()

    mock_print.assert_any_call("黒の勝ちです！")



def test_run(mocker):
    # 1. 各モックの作成
    mock_manager = MagicMock()
    mock_board = MagicMock()
    mock_cpu = MagicMock()
    mock = MagicMock()
    othello = Othello(manager=mock_manager,othello_board=mock_board)

    #処理をスキップ
    mocker.patch.object(othello, "players_select")
    mocker.patch.object(othello, "result")

    # 2. 状態の初期設定
    mock_manager.turn = str(Stone.WHITE)
    mock_manager.put_stone.return_value = True
    

    othello.actors = {str(Stone.BLACK): MagicMock(), str(Stone.WHITE): MagicMock()}

    #白の石を1度だけ置かせて、その後２回連続で石が置けない処理をし、ゲームを終了させる。
    mock_manager.has_valid_move.side_effect = [True, False, False]

    #play_turn関数が(3, 4)を返すようにする
    mocker.patch("src.othello_app.models.othello.play_turn", return_value=(3, 4))
    mock_print = mocker.patch("builtins.print")

    
    mock_print = mocker.patch("builtins.print")

    # 実行
    othello.run()

    mock_print.assert_any_call("両者ともおける場所がありません。ゲーム終了です！")

