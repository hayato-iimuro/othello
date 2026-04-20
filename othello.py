class Field:
    def __init__ (self):
        self.board = ['E'] * 64

        self.board[self.get_index(3,3)] = "W"
        self.board[self.get_index(3,4)] = "B"
        self.board[self.get_index(4,3)] = "B"
        self.board[self.get_index(4,4)] = "W"
    

    def get_index(self, row, col):
        num = row * 8 + col
        return num


    def display_board(self):
        print("---------------------------------")
        for i in range(64):
            if i%8 == 7:
                print(f"| {self.board[i]} |")
                print("---------------------------------")
            else:
                print(f"| {self.board[i]} ",end="")


    def disc_inside(self, row, col):
        return 0 <= row <= 7 and 0 <= col <= 7


    
class Game:
    def __init__(self, field_object):
        self.field = field_object
        self.turn = "B"


    def put_stone(self, row, col):

        if not self.field.disc_inside(row, col):
            print("盤面の中にコマを置いてください。")
            return

        if self.field.board[self.field.get_index(row, col)] != "E":
            print("そこにはすでにコマがあります。")
            return
        

        flippable = self.can_flip(row, col)
        if not flippable:
            print("ひっくり返せるコマがないので置けません。")
            return
        

        self.field.board[self.field.get_index(row, col)] = self.turn
            

        for index in flippable:
            self.field.board[index] = self.turn
            
        self.turn = "W" if self.turn == "B" else "B"

        self.field.display_board()


    def can_flip(self, row, col):
    
        opponent = "W" if self.turn == "B" else "B"

        flippable_list = []

        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

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
    

    def has_valid_move(self):
        for r in range(8):
            for c in range(8):
                if self.field.board[self.field.get_index(r, c)] == "E":
                    if self.can_flip(r, c) != []:
                        return True
        return False



class Othello:
    def __init__(self):
        self.othello_board = Field()
        self.manager = Game(self.othello_board)


    def run(self):
        self.othello_board.display_board()

        while True:
            print(f"現在は {self.manager.turn} の番です。")
            
            if not self.manager.has_valid_move():
                print(f"{self.manager.turn}はおける場所がないためパスです。")

                self.manager.turn = "W" if self.manager.turn == "B" else "B"

                if not self.manager.has_valid_move():
                    print("ゲーム終了です！")
                    break

                continue

            try:
                r = int(input("行 (0-7): "))
                c = int(input("列 (0-7): "))
            except ValueError:
                print("数字を入力してください！")
                continue

            self.manager.put_stone(r, c)
            
        black_score = self.othello_board.board.count("B")
        white_score = self.othello_board.board.count("W")

        print(f"結果: 黒 {black_score} - 白 {white_score}")

        if black_score > white_score:
            print("黒の勝ちです！")
        elif black_score == white_score:
            print("引き分けです！")
        else:
            print("白の勝ちです！")


othello = Othello()
othello.run()