import unittest
from copy import deepcopy
from game_module import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.initial_state = [['.' for _ in range(3)] for _ in range(3)]
        self.game = Game(deepcopy(self.initial_state))

    def test_init(self):
        game_init = Game(deepcopy(self.initial_state))
        self.assertEqual(game_init.state, self.initial_state)

    def test_move_by_player(self):
        player = 'X'
        new_state = self.game.move(player, pos=(0, 0))
        expected_state = [['X', '.', '.'],
                          ['.', '.', '.'],
                          ['.', '.', '.']]
        self.assertEqual(new_state, expected_state)
        new_state = self.game.move(player, pos=(0, 1))
        expected_state = [['X', 'X', '.'],
                          ['.', '.', '.'],
                          ['.', '.', '.']]
        self.assertEqual(new_state, expected_state)
        new_state = self.game.move(player, pos=(1, 2))
        expected_state = [['X', 'X', '.'], ['.', '.', 'X'], ['.', '.', '.']]
        self.assertEqual(new_state, expected_state)

    def test_bad_player_move(self):
        tempor_game = Game(state=[['X', 'X', 'X'],
                                  ['.', '.', '.'],
                                  ['.', '.', '.']])
        old_state = deepcopy(tempor_game.state)
        new_state = tempor_game.move('X', pos=(0, 0))
        self.assertNotEqual(new_state, old_state)

    def test_move_by_robot(self):
        player = 'O'
        new_state = self.game.move(player, robo=True)
        self.assertNotEqual(self.game.state, self.initial_state)
        self.assertEqual(new_state, self.game.state)

    def test_move_availability(self):
        player = 'O'
        temporary_game = Game(deepcopy(self.initial_state))
        for move in range(8):
            temporary_game.move(player, robo=True)
            self.assertTrue(temporary_game.move_availiale())
        temporary_game.move(player, robo=True)
        self.assertFalse(temporary_game.move_availiale())

        full_state = deepcopy(temporary_game.state)
        temporary_game.move('O', robo=True)
        self.assertEqual(full_state, temporary_game.state)

    def test_game_won(self):
        player = 'X'
        vertical = Game(state=[['X', '.', '.'],
                               ['X', '.', '.'],
                               ['X', '.', '.']])
        self.assertTrue(vertical.won(player))
        horizontal = Game(state=[['X', 'X', 'X'],
                                 ['.', '.', '.'],
                                 ['.', '.', '.']])
        self.assertTrue(horizontal.won(player))
        diagonal = Game(state=[['X', '.', '.'],
                               ['.', 'X', '.'],
                               ['.', '.', 'X']])
        self.assertTrue(diagonal.won(player))
        doesnt = Game(state=[['X', '.', '.'],
                             ['.', '.', '.'],
                             ['.', '.', 'X']])
        self.assertFalse(doesnt.won(player))

    def test_robot_move_range(self):
        intermediate_state = [['X', 'O', 'X'],
                              ['O', 'X', 'O'],
                              ['O', '.', '.']]
        intermediate_game = Game(intermediate_state)
        r, c = intermediate_game.robot_move()
        self.assertIn((r, c), [(2, 1), (2, 2)])
