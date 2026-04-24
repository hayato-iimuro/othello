from .stone import Stone
from .field import Field
from .game import Game

from .actors import Cpu, Player, GamePlayer, play_turn

class Othello:
    def __init__(self, manager=None, othello_board=None) -> None:
        self.othello_board = othello_board or Field()
        self.manager = manager or Game(self.othello_board)
        # 型ヒントを追加して、辞書の中身がGamePlayerであることを明示します
        self.actors = {}

    def players_select(self) -> None:
        
        black = str(Stone.BLACK.value)
        white = str(Stone.WHITE.value)

        # プレイヤー選択
        while True:
            try:
                a = int(input("『黒』を選んでください。 1.Player 2.CPU: "))
                b = int(input("『白』を選んでください。 1.Player 2.CPU: "))
                
                if a not in (1, 2) or b not in (1, 2):
                    continue
                break
            except ValueError:
                print("数字を入力してください！")

        self.actors[black] = Player() if a == 1 else Cpu()
        self.actors[white] = Player() if b == 1 else Cpu()

        
        print(f"黒:{self.actors[black].display_name()} 白:{self.actors[white].display_name()} で対戦を開始します。")

    def result(self) -> None:
        
        black_score = self.othello_board.board.count(str(Stone.BLACK))
        white_score = self.othello_board.board.count(str(Stone.WHITE))

        self.manager.flippable_point()
        print(f"\n結果: 黒 {black_score} - 白 {white_score}")

        if black_score > white_score:
            print("黒の勝ちです！")
        elif black_score < white_score:
            print("白の勝ちです！")
        else:
            print("引き分けです！")

    def run(self) -> None:
        
        self.players_select()

        self.manager.flippable_point()
        self.othello_board.display_board()

        while True:
            current_actor = self.actors[self.manager.turn]
            
            if not self.manager.has_valid_move():
                print(f"{self.manager.turn} はおける場所がないためパスです。")
                # ターンを交代
                self.manager.turn = str(Stone.WHITE) if self.manager.turn == str(Stone.BLACK) else str(Stone.BLACK)

                # ゲーム終了判定
                self.manager.flippable_point()
                if not self.manager.has_valid_move():
                    print("両者ともおける場所がありません。ゲーム終了です！")
                    break
                continue

            
            r, c = play_turn(current_actor)

            # 石を置く処理。
            success = self.manager.put_stone(r, c)
            
            if not success:
                print("そこには置けません。別の座標を選んでください。")
                continue


            self.manager.flippable_point()
            self.othello_board.display_board()
            

        self.result()