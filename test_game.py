from unittest import TestCase
from game import Game
from game_result import GameResult


class TestGame(TestCase):
    def setUp(self):
        self.game = Game()
        super().setUp()

    def assert_illegal_argument(self, guessNumber):
        try:
            self.game.guess(guessNumber)
            self.fail()
        except TypeError:
            pass

    def test_exception_when_invalid_input(self):
        self.assert_illegal_argument(None)
        self.assert_illegal_argument("12")
        self.assert_illegal_argument("1234")
        self.assert_illegal_argument("12s")
        self.assert_illegal_argument("121")

    def asssert_matched_number(self, result, solved, strikes, balls):
        self.assertIsNotNone(result)
        self.assertEqual(solved, result.get_solved())
        self.assertEqual(strikes, result.get_strikes())
        self.assertEqual(balls, result.get_balls())

    def test_return_solve_result_if_matched_number(self):
        self.generate_question("123")
        self.asssert_matched_number(self.game.guess("123"), True, 3, 0)

    def generate_question(self, question_nuber):
        self.game.question = question_nuber

    def test_return_solve_result_if_unmatched_number(self):
        self.generate_question("123")
        self.asssert_matched_number(self.game.guess("456"), False, 0, 0)

    def test_return_solve_result_if_some_matched_number(self):
        self.generate_question("123")
        self.asssert_matched_number(self.game.guess("120"), False, 2, 0)
        self.asssert_matched_number(self.game.guess("061"), False, 0, 1)
        self.asssert_matched_number(self.game.guess("136"), False, 1, 1)
