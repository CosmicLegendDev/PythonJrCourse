# 1 - 6
import random

def dice() -> int:
    return random.randint(1, 6)

if __name__ == "__main__":
    while(True):
        ans = input("Roll dice (Y/N)?")
        if ans == "Y":
            d_value = dice()
            print(f"Diced value: {d_value}")
        else:
            print("Game Over...!")
            break