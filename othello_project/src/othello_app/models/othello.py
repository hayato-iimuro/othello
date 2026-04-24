from .stone import Stone
from .field import Field
from .game import Game
from .actors import Cpu, Player

class Othello:
    def __init__(self, manager=None, othello_board=None ,cpu=None) -> None:
        self.othello_board = othello_board or Field()
        self.manager = manager or Game(self.othello_board)
        self.actors = {}

    def run(self) -> None:
        #PvPかPvCかを選択する

        black_key = str(Stone.BLACK.value)
        white_key = str(Stone.WHITE.value)

        try:
            a = int(input(f"『黒』を選んでください。  1.Player 2.CPU "))
            b = int(input(f"『白』を選んでください。  1.Player 2.CPU "))

            self.actors[black_key] = Player() if a == 1 else Cpu()
            self.actors[white_key] = Player() if b == 1 else Cpu()

            if a == b == 1:
                print(f"黒:Player 白:Player で対戦を開始します。")

            elif a == 1 and b == 2:
                print(f"黒:Player 白:CPU で対戦を開始します。")

            elif a == 2 and b == 1:
                print(f"黒:CPU 白:Player で対戦を開始しまします。")

            elif a == b == 2:
                print(f"黒：CPU 白:CPU で対戦を開始します。")
        except ValueError:
            print("数字を入力してください！")

       




        self.manager.flippable_point()
        self.othello_board.display_board()


        while True:
            
            current_actor = self.actors[self.manager.turn]
            
            print(f"現在は {self.manager.turn} の番です。")
            
            #コマをおける場所があるかチェックし、なければメッセージする
            if not self.manager.has_valid_move():
                print(f"{self.manager.turn}はおける場所がないためパスです。")
                self.manager.turn = str(Stone.WHITE) if self.manager.turn == str(Stone.BLACK) else str(Stone.BLACK)

                # パス後、相手も置ける場所がないか（ゲーム終了か）を確認
                self.manager.flippable_point()
                if not self.manager.has_valid_move():
                    print("両者ともおける場所がありません。ゲーム終了です！")
                    break
                continue
            
            
            

            r, c = current_actor.choice()



            

            # 石を置く処理。置けなかった場合（False）は、continueでループの先頭に戻る
            success = self.manager.put_stone(r, c)
            if success:
                if self.manager.turn == str(Stone.WHITE):
                    #コマをおける場所を⭐︎にする
                    self.manager.flippable_point()
                    self.othello_board.display_board()

            else:
                continue
            
            
        # ゲーム終了時のスコア計算
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