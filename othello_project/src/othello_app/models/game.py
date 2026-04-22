# ゲーム進行を管理するクラス

from models.field import Field

class Game:
    def __init__(self, field_object: Field) -> None:
        self.field = field_object
        self.turn = "⚫️"


    def flippable_point(self) -> None:
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

    def has_valid_move(self) -> bool:
        #星が一つでもあればTrueを返す
        return "⭐︎" in self.field.board

    # 石を置くメソッド
    def put_stone(self, row: int, col: int) -> bool:
        # 選択した座標が盤面の中かどうか判定
        if not self.field.disc_inside(row, col):
            print("盤面の中にコマを置いてください。")
            return False  # ループをやり直すためにFalseを返す

        # コマが置かれていないかを判定
        xy_index = self.field.get_index(row, col)
        if self.field.board[xy_index] not in ("⬜︎", "⭐︎"):
            print("そこにはすでにコマがあります。")
            return False
        
        # ひっくり返すことができるコマがなければメッセージを表示
        flippable = self.can_flip(row, col)
        if not flippable:
            print("ひっくり返せるコマがないので置けません。")
            return False

        # コマを置く
        self.field.board[xy_index] = self.turn
            
        # 挟んだ石をひっくり返す
        for index in flippable:
            self.field.board[index] = self.turn

        # ターンを交代する
        self.turn = "⚪️" if self.turn == "⚫️" else "⚫️"
        return True  # 成功した場合はTrueを返す

    # 引数として受けとった座標にコマを置いた場合に、ひっくり返せるコマのリストを返す
    def can_flip(self, row: int, col:int) -> list:
        opponent = "⚪️" if self.turn == "⚫️" else "⚫️"
        flippable_list = []
        #隣のマスの相対的座標
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        #コマを置いたマスの隣のマスを探索する
        for dr, dc in directions:
            temp_candidates = []
            nr, nc = row + dr, col + dc
            #その方向に相手のコマが連続している限り探索を続け、相手のコマの座標をtemp_candidatesに追加する
            while (self.field.disc_inside(nr, nc)) and (self.field.board[self.field.get_index(nr, nc)] == opponent):
                temp_candidates.append(self.field.get_index(nr, nc))
                nr += dr
                nc += dc
            # もし進んだマスのコマが自分の色であった場合、そこで探索を終了し、temp_candidatesをflippable_listに追加する
            if (self.field.disc_inside(nr, nc)) and (self.field.board[self.field.get_index(nr, nc)] == self.turn):
                flippable_list.extend(temp_candidates)
        
        return flippable_list