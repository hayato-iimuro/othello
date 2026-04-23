from models.stone import Stone

# 盤面の状態を管理するクラス
class Field:
    def __init__(self) -> None:
        #空白は２つ
        self.board = [str(Stone.EMPTY)] * 64

        # 初期配置
        self.board[self.get_index(3, 3)] = str(Stone.WHITE)
        self.board[self.get_index(3, 4)] = str(Stone.BLACK)
        self.board[self.get_index(4, 3)] = str(Stone.BLACK)
        self.board[self.get_index(4, 4)] = str(Stone.WHITE)

    #マスの番号から座標を取得する
    def get_index(self, row: int, col: int) -> int:
        return row * 8 + col

    #盤面を作る
    def display_board(self) -> None:
        print("-" * 33)
        for i in range(64):
            if i % 8 == 7:
                print(f"| {self.board[i]} |")
                print("-" * 33)
            else:
                print(f"| {self.board[i]} ", end="")

    #盤面の範囲を定義する
    def disc_inside(self, row: int, col: int) -> bool:
        return 0 <= row <= 7 and 0 <= col <= 7