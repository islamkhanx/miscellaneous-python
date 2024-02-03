from random import choice


CROSS = 'X'


class Game:
    def __init__(self, state: list[list[str]]) -> None:
        """Initializes game at a given state

        Args:
            state (list[list[str]]): 3 X 3 game state
        """
        self.state = state

    def move(self, player: str, robo: bool = False,
             pos: tuple[int] = None) -> list[list]:
        """Makes a move in a game either by player or by AI
           if move is not availiable makes no move;
           if move by player is not on empty space, then performed by AI
        Args:
            player (str): mark of a player making move
            robo (bool, optional): if move must be performed by AI.
            Defaults to False.
            pos (tuple[int], optional):row and column of a move by real player.
            Defaults to None.
        Returns:
            list[list]: state of the game after move,
            internally state is also changed
        """
        if not self.move_availiale():
            return self.state

        r, c = self.robot_move() if robo else pos

        # if move isn't legal, it is performed by AI :)
        if pos:
            if self.state[r][c] != '.':
                return self.move(player, robo=True)

        self.state[r][c] = player
        return self.state

    def won(self, player: str = CROSS) -> bool:
        """Check if crosses or zeros have won the game

        Args:
            player (str, optional): mark of the player
            that is candidate to win.
            Defaults to CROSS.

        Returns:
            bool: if particuar player wins
        """
        fields = [''.join(x) for x in self.state]

        # horizontal win check
        if (player * 3 in fields):
            return True

        # diagonal win check
        diagonals = (
            [line[i] for i, line in enumerate(fields)],
            [line[-1-i] for i, line in enumerate(fields)]
            )
        if ([player] * 3 in diagonals):
            return True

        # vertical win check
        fields_T = list(zip(*fields))
        if (player,)*3 in fields_T:
            return True

        return False

    def robot_move(self) -> tuple[int]:
        """Looks at the game state to determine move;
        move is made randomly among availiable cells;
        it is guaranteed that if this method is called,
        at least one move is availiable
        Returns:
            tuple[int]: row and column of move
        """
        game_state = self.state
        availiable = []
        for r in range(3):
            for c in range(3):
                if game_state[r][c] == '.':
                    availiable.append((r, c))

        r, c = choice(availiable)
        return r, c

    def move_availiale(self) -> bool:
        """Checks if ther is any availiable move
        in the game

        Returns:
            bool: presence of availiable move
        """

        for row in self.state:
            if '.' in row:
                return True
        return False
