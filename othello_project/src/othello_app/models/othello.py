from models.field import Field
from models.game import Game
from models.cpu import Cpu

class Othello:
    def __init__(self) -> None:
        self.othello_board = Field()
        self.manager = Game(self.othello_board)
        self.cpu = Cpu()

    def run(self) -> None:
        self.manager.flippable_point()
        self.othello_board.display_board()


        while True:
            
            
            
            print(f"現在は {self.manager.turn} の番です。")
            
            #コマをおける場所があるかチェックし、なければメッセージする
            if not self.manager.has_valid_move():
                print(f"{self.manager.turn}はおける場所がないためパスです。")
                self.manager.turn = "⚪️" if self.manager.turn == "⚫️" else "⚫️"

                # パス後、相手も置ける場所がないか（ゲーム終了か）を確認
                self.manager.flippable_point()
                if not self.manager.has_valid_move():
                    print("両者ともおける場所がありません。ゲーム終了です！")
                    break
                continue
            #黒のターンをCPUに操作させる
            if self.manager.turn == "⚫️":
                r = self.cpu.cpu_choice()
                c = self.cpu.cpu_choice()
            #白のターンはプレイヤーにコマを置く場所を選択させる
            else:
                try:
                    r = int(input("行 (0-7): "))
                    c = int(input("列 (0-7): "))
                except ValueError:
                    print("数字を入力してください！")
                    continue

            # 石を置く処理。置けなかった場合（False）は、continueでループの先頭に戻る
            success = self.manager.put_stone(r, c)
            if success:
                if self.manager.turn == "⚪️":
                    #コマをおける場所を⭐︎にする
                    self.manager.flippable_point()
                    self.othello_board.display_board()

            else:
                continue
            
            
        # ゲーム終了時のスコア計算
        black_score = self.othello_board.board.count("⚫️")
        white_score = self.othello_board.board.count("⚪️")

        print(f"\n結果: 黒 {black_score} - 白 {white_score}")

        if black_score > white_score:
            print("黒の勝ちです！")
        elif black_score < white_score:
            print("白の勝ちです！")
        else:
            print("引き分けです！")