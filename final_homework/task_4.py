class Cell:
    def __init__(self, num):
        self.__val = None
        self.__num = num

    def __str__(self):
        if self.__val:
            return str(self.__val)
        return str(self.__num)

    def __eq__(self, other):
        if isinstance(other, Cell):
            return self.__val == other.__val
        return False

    @property
    def value(self):
        return self.__val

    def set_val(self, val):
        self.__val = val


class Board:
    def __init__(self):
        self.field = {key: Cell(key) for key in range(1, 10)}

    def __str__(self):
        b = ""
        b += "-" * 13 + "\n"
        for i in range(3):
            b += f'| {self.field[1 + i * 3]} | {self.field[2 + i * 3]} | {self.field[3 + i * 3]} |\n'
            b += "-" * 13 + "\n"
        return b


class Game:
    def __init__(self):
        self.board = Board()

    def _check_win(self):
        win_coord = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
        for coord in win_coord:
            if self.board.field[coord[0]] == self.board.field[coord[1]] == self.board.field[coord[2]]:
                return self.board.field[coord[0]].value
        return False

    def _take_input(self, player_token):
        valid = False
        while not valid:
            player_answer = input("Куда поставим " + player_token + "? ")
            try:
                player_answer = int(player_answer)
            except:
                print("Некорректный ввод. Вы уверены, что ввели число?")
                continue

            if 1 <= player_answer <= 9:
                print(self.board.field[player_answer])
                if not self.board.field[player_answer].value:
                    self.board.field[player_answer].set_val(player_token)
                    valid = True
                else:
                    print("Эта клетка уже занята")
            else:
                print("Некорректный ввод. Введите число от 1 до 9 чтобы сделать ход")

    def start(self):
        counter = 0
        while True:
            print(self.board)
            if counter % 2 == 0:
                self._take_input("X")
            else:
                self._take_input("O")
            counter += 1

            if counter > 4:
                winner = self._check_win()
                if winner:
                    print(winner, "выиграли")
                    break
            if counter == 9:
                print("Ничья")
                break


if __name__ == "__main__":
    game = Game()
    game.start()
