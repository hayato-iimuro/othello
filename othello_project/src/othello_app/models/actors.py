#CPUを管理するクラス
import random

class Cpu:
    def __init__(self) -> None:
        pass


    def display_name(self) -> str:
        name = "CPU"
        return name



    #0~7の整数をランダムで取得
    def choice(self) -> tuple[int, int]:
        r = random.randint(0, 7)
        c = random.randint(0, 7)
        return r, c
    

    
    
class Player:
    def __init__(self) -> None:
        pass


    def display_name(self) -> str:
        name = "Player"
        return name


    def choice(self) -> tuple[int, int]:
        while True:
            try:
                r = int(input("行 (0-7): "))
                c = int(input("列 (0-7): "))
            except ValueError:
                print("数字を入力してください！")
                continue
            return r, c
    





