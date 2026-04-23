#CPUを管理するクラス
import random

class Cpu:
    def __init__(self) -> None:
        pass

    #0~7の整数をランダムで取得
    def cpu_choice(self) -> int:
        num = random.randint(0, 7)
        return num