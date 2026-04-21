import random
#CPUを管理するクラス
class Cpu:
    def __init__(self):
        self.othello_board = Field()
        self.manager = Game(self.othello_board)

    #0~7の整数をランダムで取得
    def cpu_choice(self):
        num = random.randint(0, 7)
        return num


# 盤面の状態を管理するクラス
class Field:
    def __init__(self):
        self.board = ['⬜︎'] * 64

        # 初期配置
        self.board[self.get_index(3, 3)] = "⚪️"
        self.board[self.get_index(3, 4)] = "⚫️"
        self.board[self.get_index(4, 3)] = "⚫️"
        self.board[self.get_index(4, 4)] = "⚪️"

    #マスの番号から座標を取得する
    def get_index(self, row, col):
        return row * 8 + col

    #盤面を作る
    def display_board(self):
        print("-" * 41)
        for i in range(64):
            if i % 8 == 7:
                print(f"| {self.board[i]} |")
                print("-" * 41)
            else:
                print(f"| {self.board[i]} ", end="")

    #盤面の範囲を定義する
    def disc_inside(self, row, col):
        return 0 <= row <= 7 and 0 <= col <= 7


# ゲーム進行を管理するクラス
class Game:
    def __init__(self, field_object):
        self.field = field_object
        self.turn = "⚫️"

    def flippable_point(self):
        # 1. 前のターンで付けた⭐︎をすべて ⬜︎ にリセットする
        for i in range(64):
            if self.field.board[i] == "⭐︎":
                self.field.board[i] = "⬜︎"
        
        # 2. 現在のプレイヤーが石を置ける場所を探索し、⭐︎を配置する
        for r in range(8):
            for c in range(8):
                if self.field.board[self.field.get_index(r, c)] == "⬜︎":
                    # Pythonicな書き方: リストが空でない場合はTrueとして扱われる
                    if self.can_flip(r, c):
                        # 相手の石ではなく、空きマスそのものに⭐︎を置く
                        self.field.board[self.field.get_index(r, c)] = "⭐︎"

    def has_valid_move(self):
        #星が一つでもあればTrueを返す
        return "⭐︎" in self.field.board

    # 石を置くメソッド
    def put_stone(self, row, col):
        # 選択した座標が盤面の中かどうか判定
        if not self.field.disc_inside(row, col):
            print("盤面の中にコマを置いてください。")
            return False  # ループをやり直すためにFalseを返す

        # コマが置かれていないかを判定
        target_index = self.field.get_index(row, col)
        if self.field.board[target_index] not in ("⬜︎", "⭐︎"):
            print("そこにはすでにコマがあります。")
            return False
        
        # ひっくり返すことができるコマがなければメッセージを表示
        flippable = self.can_flip(row, col)
        if not flippable:
            print("ひっくり返せるコマがないので置けません。")
            return False

        # コマを置く
        self.field.board[target_index] = self.turn
            
        # 挟んだ石をひっくり返す
        for index in flippable:
            self.field.board[index] = self.turn

        # ターンを交代する
        self.turn = "⚪️" if self.turn == "⚫️" else "⚫️"
        return True  # 成功した場合はTrueを返す

    # 引数として受けとった座標にコマを置いた場合に、ひっくり返せるコマのリストを返す
    def can_flip(self, row, col):
        opponent = "⚪️" if self.turn == "⚫️" else "⚫️"
        flippable_list = []
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        for dr, dc in directions:
            temp_candidates = []
            nr, nc = row + dr, col + dc
            
            while (self.field.disc_inside(nr, nc)) and (self.field.board[self.field.get_index(nr, nc)] == opponent):
                temp_candidates.append(self.field.get_index(nr, nc))
                nr += dr
                nc += dc
                
            if (self.field.disc_inside(nr, nc)) and (self.field.board[self.field.get_index(nr, nc)] == self.turn):
                flippable_list.extend(temp_candidates)
        
        return flippable_list


class Othello:
    def __init__(self):
        self.othello_board = Field()
        self.manager = Game(self.othello_board)
        self.cpu = Cpu()

    def run(self):
        while True:
            #
            self.manager.flippable_point()
            self.othello_board.display_board()
            
            print(f"現在は {self.manager.turn} の番です。")
            
            if not self.manager.has_valid_move():
                print(f"{self.manager.turn}はおける場所がないためパスです。")
                self.manager.turn = "⚪️" if self.manager.turn == "⚫️" else "⚫️"

                # パス後、相手も置ける場所がないか（ゲーム終了か）を確認
                self.manager.update_stars()
                if not self.manager.has_valid_move():
                    print("両者ともおける場所がありません。ゲーム終了です！")
                    break
                continue

            if self.manager.turn == "⚫️":
                r = self.cpu.cpu_choice()
                c = self.cpu.cpu_choice()
            else:
                try:
                    r = int(input("行 (0-7): "))
                    c = int(input("列 (0-7): "))
                except ValueError:
                    print("数字を入力してください！")
                    continue

            # 石を置く処理。置けなかった場合（False）は、continueでループの先頭に戻る
            success = self.manager.put_stone(r, c)
            if not success:
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


# 実務でよく使われるイディオム: 直接実行された場合のみゲームを開始する
if __name__ == "__main__":
    othello = Othello()
    othello.run()


