# 盤面の状態を管理するクラス
class Field:
    def __init__(self) -> None:
        #空白は２つ
        self.board = ['  '] * 64

        # 初期配置
        self.board[self.get_index(3, 3)] = "⚪️"
        self.board[self.get_index(3, 4)] = "⚫️"
        self.board[self.get_index(4, 3)] = "⚫️"
        self.board[self.get_index(4, 4)] = "⚪️"

    #マスの番号から座標を取得する
    def get_index(self, row: int, col: int) -> int:
        return row * 8 + col

    #盤面を作る
    def display_board(self) -> None:
        print("     0    1    2    3    4    5    6    7")
        print("   " + "-" * 41)
        for i in range(64):
            if i % 8 == 0:
                print(str(int(i) // 8) + "  ",end="")
            if i % 8 == 7:
                print(f"| {self.board[i]} |")
                print("   " + "-" * 41)
            else:
                print(f"| {self.board[i]} ", end="")

    #盤面の範囲を定義する
    def disc_inside(self, row: int, col: int) -> bool:
        return 0 <= row <= 7 and 0 <= col <= 7