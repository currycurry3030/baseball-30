from game_result import GameResult


class Game:
    def __init__(self) -> None:
        self.question = ""

    def is_solved(self, guessNumber):
        return guessNumber == self.question

    def guess(self, guessNumber):
        self.assert_illegal_value(guessNumber)
        if self.is_solved(guessNumber):
            return self.get_success_game_result()
        else:
            return self.get_unsolved_game_result(guessNumber)

    def get_unsolved_game_result(self, guessNumber):
        strikes = 0
        balls = 0
        for i in range(len(self.question)):
            if self.question.find(guessNumber[i]) == i:
                strikes += 1
            elif self.question.find(guessNumber[i]) > -1:
                balls += 1
        return GameResult(False, strikes, balls)

    def get_success_game_result(self):
        return GameResult(True, 3, 0)

    def assert_illegal_value(self, guessNumber):
        if guessNumber is None:
            raise TypeError()
        if len(guessNumber) != 3:
            raise TypeError()
        for number in guessNumber:
            if not ord('0') <= ord(number) <= ord('9'):
                raise TypeError()
        if len(set(guessNumber)) != len(guessNumber):
            raise TypeError()
