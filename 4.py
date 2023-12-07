import random

stones = random.randint(4, 30)
print("Камней в кучке:", stones)

while stones > 0:
    while True:
        try:
            print("Первый игрок берет камни из кучи (от 1 до 3):")
            player1 = int(input())
            if player1 < 1 or player1 > 3:
                print("Неверное значение.")
            else:
                stones -= player1
                print("Камней в кучке:", stones)
                break
        except:
            print("Неверное значение")
        if stones == 1:
            print("Первый игрок победил!!!")
            exit()
    while True:
        try:
            print("Второй игрок берет камни из кучи (от 1 до 3):")
            player2 = int(input())
            if player2 < 1 or player2 > 3:
                print("Неверное значение.")
            else:
                stones -= player2
                print("Камней в кучке:", stones)
                break
        except ValueError:
            print("Неверное значение")
        if stones == 1:
            print("Второй игрок победил!!!")
            exit()
