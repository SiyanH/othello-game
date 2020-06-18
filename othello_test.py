from othello import Othello, MOVE_DIRS
from board import Board
import score, copy, unittest

# Define two common states of board of size 8x8 as constants for testing
EMPTY_BOARD = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
INITIAL_BOARD = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 1, 0, 0, 0],
                 [0, 0, 0, 1, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], 
                 [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

class TestOthello(unittest.TestCase):
    '''
        Test methods for class Othello
    '''
    def test_init(self):
        # Test for board of size 0
        game = Othello(0)
        self.assertEqual(game.n, 0)
        self.assertEqual(game.board, [])

        # Test for board of size 2x2
        game = Othello(2)
        self.assertEqual(game.n, 2)
        expected_board = [[0, 0], [0, 0]]
        self.assertEqual(game.board, expected_board)

        # Test for board of size 4x4
        game = Othello(4)
        self.assertEqual(game.n, 4)
        expected_board = [[0, 0, 0, 0], [0, 0, 0, 0],
                          [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(game.board, expected_board)
        self.assertEqual(game.square_size, 50)
        self.assertEqual(game.board_color, 'forest green')
        self.assertEqual(game.line_color, 'black')
        self.assertEqual(game.tile_size, 20)
        self.assertEqual(game.tile_colors, ['black', 'white'])
        self.assertEqual(game.move, ())
        self.assertEqual(game.current_player, 0)
        self.assertEqual(game.num_tiles, [2, 2])

        # Test for board of size 8x8
        game = Othello()
        self.assertEqual(game.n, 8)
        self.assertEqual(game.board, EMPTY_BOARD)
        self.assertEqual(game.square_size, 50)
        self.assertEqual(game.board_color, 'forest green')
        self.assertEqual(game.line_color, 'black')
        self.assertEqual(game.tile_size, 20)
        self.assertEqual(game.tile_colors, ['black', 'white'])
        self.assertEqual(game.move, ())
        self.assertEqual(game.current_player, 0)
        self.assertEqual(game.num_tiles, [2, 2])
    
    def test_initialize_board(self):
        # Test for board of size 0
        game = Othello(0)
        game.initialize_board()
        self.assertEqual(game.board, [])

        # Test for board of size 2x2
        game = Othello(2)
        game.initialize_board()
        expected_board = [[2, 1], [1, 2]]
        self.assertEqual(game.board, expected_board)

        # Test for board of size 4x4
        game = Othello(4)
        game.initialize_board()
        expected_board = [[0, 0, 0, 0], [0, 2, 1, 0], 
                          [0, 1, 2, 0], [0, 0, 0, 0]]
        self.assertEqual(game.board, expected_board)

        # Test for board of size 8x8
        game = Othello()
        game.initialize_board()
        self.assertEqual(game.board, INITIAL_BOARD)

    def test_make_move(self):
        game = Othello()
        game.initialize_board()

        # Test making illegal moves before making any legal moves
        illegal_moves = [(), (3, 3), (3, 4), (4, 3), (4, 4), (-1, 0), 
                         (8, 2), (-5, 9), (0, 0), (3, 1), (2, 2), (5, 3)]
        for move in illegal_moves:
            game.move = move
            game.make_move()
            self.assertEqual(game.board, INITIAL_BOARD)
            self.assertEqual(game.num_tiles, [2, 2])

        # Test making legal moves for different players
        game.move = (2, 3)
        game.make_move()
        self.assertEqual(game.board[2][3], 1)
        self.assertEqual(game.board[3][3], 1)
        self.assertEqual(game.board[4][3], 1)

        game.current_player = 1
        game.move = (2, 2)
        game.make_move()
        self.assertEqual(game.board[2][2], 2)
        self.assertEqual(game.board[3][3], 2)
        self.assertEqual(game.board[4][4], 2)

        game.current_player = 0
        game.move = (4, 5)
        game.make_move()
        self.assertEqual(game.board[4][3], 1)
        self.assertEqual(game.board[4][4], 1)
        self.assertEqual(game.board[4][5], 1)

        # Test making illegal moves after making some legal moves
        game.current_player = 1
        game.move = (5, 4)
        game.make_move()
        self.assertEqual(game.board[5][4], 0)
        game.move = (5, 2)
        game.make_move()
        self.assertEqual(game.board[5][2], 0)
        game.move = (6, 0)
        game.make_move()
        self.assertEqual(game.board[6][0], 0)

    def test_is_legal_move(self):
        game = Othello()
        game.initialize_board()

        # Test illegal moves before making any legal moves
        illegal_moves = [(), (3, 3), (3, 4), (4, 3), (4, 4), (-1, 0), 
                         (8, 2), (-5, 9), (0, 0), (3, 1), (2, 2), (5, 3)]

        for move in illegal_moves:
            self.assertFalse(game.is_legal_move(move))

        # Test legal moves for player 1 (black tile)
        legal_moves = [(2, 3), (3, 2), (5, 4), (4, 5)]
        for move in legal_moves:
            self.assertTrue(game.is_legal_move(move)) 
        
        # Let player 1 make a legal move
        game.move = (2, 3)
        game.make_move()
        
        # Test legal/illegal moves for player 2 (white tile)
        game.current_player = 1
        legal_moves = [(2, 4), (2, 2), (4, 2)]
        for move in legal_moves:
            self.assertTrue(game.is_legal_move(move))
        illegal_moves = [(3, 2), (5, 3), (5, 4), (4, 5), (3, 5), (6, 1)]
        for move in illegal_moves:
            self.assertFalse(game.is_legal_move(move))
    
    def test_is_valid_coord(self):
        # Test for board of size 0 (no valid coordinate)
        game = Othello(0)

        coords = [(0, 0), (1, 2), (3, 8), (0, 1), (-4, 3), (8, -7), (-1, -5)]
        for coord in coords:
            self.assertFalse(game.is_valid_coord(coord[0], coord[1]))

        # Test for board of size 4x4
        game = Othello(4)

        invalid_coords = [(4, 0), (1, 4), (5, 8), (3, 9), (0, -1),
                          (-2, 3), (8, -7), (-1, -5), (-2, -2)]
        for coord in invalid_coords:
            self.assertFalse(game.is_valid_coord(coord[0], coord[1]))
        
        valid_coords = []
        for i in range(4):
            for j in range(4):
                valid_coords.append((i, j))
        for coord in valid_coords:
            self.assertTrue(game.is_valid_coord(coord[0], coord[1]))

        # Test for board of size 8x8
        game = Othello()

        invalid_coords = [(8, 0), (1, 8), (9, 10), (3, 9), (0, -1),
                          (-2, 3), (8, -7), (-1, -5), (-2, -2)]
        for coord in invalid_coords:
            self.assertFalse(game.is_valid_coord(coord[0], coord[1]))
        
        valid_coords = []
        for i in range(8):
            for j in range(8):
                valid_coords.append((i, j))
        for coord in valid_coords:
            self.assertTrue(game.is_valid_coord(coord[0], coord[1]))

    def test_has_legal_move(self):
        game = Othello()
        game.initialize_board()

        # Test when the board is in the initial state
        self.assertTrue(game.has_legal_move())

        # Test when player 1 (black tile) has legal moves
        game.board = [[2, 0, 0, 1, 0, 0, 0, 2], [2, 1, 1, 1, 0, 0, 2, 0],
                      [2, 1, 2, 1, 2, 2, 2, 2], [1, 1, 1, 1, 1, 2, 1, 0],
                      [2, 2, 2, 1, 2, 1, 2, 0], [0, 2, 1, 1, 1, 2, 1, 2], 
                      [1, 1, 2, 0, 1, 2, 1, 1], [1, 0, 0, 2, 1, 0, 0, 1]]
        self.assertTrue(game.has_legal_move())

        # Test when player 2 (white tile) has legal moves
        game.current_player = 1
        game.board = [[2, 0, 0, 1, 1, 1, 1, 2], [2, 1, 1, 2, 0, 0, 1, 1],
                      [2, 1, 2, 1, 2, 2, 1, 2], [1, 1, 1, 1, 1, 1, 2, 0],
                      [2, 2, 1, 1, 1, 2, 2, 0], [0, 2, 1, 1, 2, 2, 1, 2], 
                      [1, 1, 1, 2, 2, 2, 2, 1], [1, 0, 1, 1, 1, 2, 0, 1]]
        self.assertTrue(game.has_legal_move())

        # Test when player 2 (white tile) has no legal moves
        game.board = [[2, 0, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 1, 1, 1, 1],
                      [2, 1, 2, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
                      [2, 2, 1, 1, 1, 2, 2, 1], [0, 2, 1, 1, 2, 2, 2, 1], 
                      [1, 2, 1, 2, 2, 2, 2, 1], [1, 2, 2, 2, 2, 2, 0, 1]]
        self.assertFalse(game.has_legal_move())

        # Test when the board is full (both players have no legal moves)
        game.board = [[2, 1, 2, 2, 2, 2, 2, 2], [2, 1, 1, 2, 1, 1, 1, 1],
                      [2, 1, 2, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 2, 1, 1], [1, 1, 1, 1, 1, 2, 1, 1], 
                      [1, 2, 1, 2, 2, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]]
        self.assertFalse(game.has_legal_move())
        game.current_player = 0
        self.assertFalse(game.has_legal_move())

    def test_get_legal_moves(self):
        game = Othello()
        game.initialize_board()

        # Test legal moves for player 1 (black tile)
        legal_moves = [(2, 3), (3, 2), (4, 5), (5, 4)]
        self.assertEqual(game.get_legal_moves(), legal_moves)

        # Let player 1 make a legal move
        game.move = (2, 3)
        game.make_move()
        
        # Test legal moves for player 2 (white tile)
        game.current_player = 1
        legal_moves = [(2, 2), (2, 4), (4, 2)]
        self.assertEqual(game.get_legal_moves(), legal_moves)

        # Test when player 1 has legal moves but player 2 has no legal moves
        game.current_player = 0
        game.board = [[2, 0, 2, 2, 2, 2, 2, 2], 
                      [2, 2, 2, 2, 1, 1, 1, 1],
                      [2, 1, 2, 1, 1, 1, 1, 1], 
                      [1, 1, 1, 1, 1, 1, 1, 1],
                      [2, 2, 1, 1, 1, 2, 2, 1], 
                      [0, 2, 1, 1, 2, 2, 2, 1], 
                      [1, 2, 1, 2, 2, 2, 2, 1], 
                      [1, 2, 2, 2, 2, 2, 0, 1]]
        legal_moves = [(0, 1), (5, 0), (7, 6)]
        self.assertEqual(game.get_legal_moves(), legal_moves)

        game.current_player = 1
        self.assertEqual(game.get_legal_moves(), [])

        # Test when the board is full (both players have no legal moves)
        game.board = [[2, 1, 2, 2, 2, 2, 2, 2], [2, 1, 1, 2, 1, 1, 1, 1],
                      [2, 1, 2, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 2, 1, 1], [1, 1, 1, 1, 1, 2, 1, 1], 
                      [1, 2, 1, 2, 2, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]]
        self.assertEqual(game.get_legal_moves(), [])
        game.current_player = 0
        self.assertEqual(game.get_legal_moves(), [])

    def test_has_tile_to_flip(self):
        game = Othello()
        game.initialize_board()

        # Test when the board is in the initial state
        # Test two moves for player 1 (black tile) in all flipping directions
        self.assertTrue(game.has_tile_to_flip((2, 3), (+1, 0)))
        no_flip_dirs = [(-1, -1), (-1, +1), (0, -1), (0, +1),
                        (+1, -1), (-1, 0), (+1, +1)]
        for direction in no_flip_dirs:
            self.assertFalse(game.has_tile_to_flip((2, 3), direction))
        
        self.assertTrue(game.has_tile_to_flip((3, 2), (0, +1)))
        no_flip_dirs = [(-1, -1), (-1, +1), (0, -1), (+1, 0), 
                        (+1, -1), (-1, 0), (+1, +1)]
        for direction in no_flip_dirs:
            self.assertFalse(game.has_tile_to_flip((3, 2), direction))
        
        # Let player 1 make a legal move
        game.move = (2, 3)
        game.make_move()
        
        # Test two moves for player 2 (white tile)
        game.current_player = 1

        self.assertTrue(game.has_tile_to_flip((2, 4), (+1, 0)))
        no_flip_dirs = [(-1, -1), (-1, +1), (0, -1), (0, +1), 
                        (+1, -1), (-1, 0), (+1, +1)]
        for direction in no_flip_dirs:
            self.assertFalse(game.has_tile_to_flip((2, 4), direction))
        
        self.assertTrue(game.has_tile_to_flip((2, 2), (+1, +1)))
        no_flip_dirs =  [(-1, -1), (-1, 0), (-1, +1), (0, -1),
                         (0, +1), (+1, -1), (+1, 0)]
        for direction in no_flip_dirs:
            self.assertFalse(game.has_tile_to_flip((2, 2), direction))

        # Test when player 1 has tiles to flip but player 2 does not
        game.board = [[2, 0, 2, 2, 2, 2, 2, 2], 
                      [2, 2, 2, 2, 1, 1, 1, 1],
                      [2, 1, 2, 1, 1, 1, 1, 1], 
                      [1, 1, 1, 1, 1, 1, 1, 1],
                      [2, 2, 1, 1, 1, 2, 2, 1], 
                      [0, 2, 1, 1, 2, 2, 2, 1], 
                      [1, 2, 1, 2, 2, 2, 2, 1], 
                      [1, 2, 2, 2, 2, 2, 0, 1]]

        game.current_player = 0
        flip_dirs = {(0, 1) : [(+1, 0), (+1, +1)], 
                     (5, 0) : [(-1, 0), (0, +1), (-1, +1)],
                     (7, 6) : [(-1, 0), (0, -1), (-1, -1)]}
        for move in flip_dirs:
            for direction in flip_dirs[move]:
                self.assertTrue(game.has_tile_to_flip(move, direction))

        game.current_player = 1
        for direction in MOVE_DIRS:
            self.assertFalse(game.has_tile_to_flip((0, 1), direction))
            self.assertFalse(game.has_tile_to_flip((5, 0), direction))
            self.assertFalse(game.has_tile_to_flip((7, 6), direction))

    def test_flip_tiles(self):
        game = Othello()
        game.initialize_board()

        # Let player 1 make a legal move
        game.move = (2, 3)
        game.board[2][3] = 1
        game.num_tiles[0] += 1
        
        # Test fliping tiles for player 1 (black tile)
        game.flip_tiles()
        expected_board = copy.deepcopy(INITIAL_BOARD)
        expected_board[2][3] = expected_board[3][3] = 1
        self.assertEqual(game.board, expected_board)
        self.assertEqual(game.num_tiles, [4, 1])

        # Test fliping tiles for player 2 (black tile)
        game.current_player = 1
        game.move = (2, 2)
        game.board[2][2] = 2
        game.num_tiles[1] += 1

        game.flip_tiles()
        expected_board[2][2] = expected_board[3][3] = 2
        self.assertEqual(game.board, expected_board)
        self.assertEqual(game.num_tiles, [3, 3])

        # Test when player 1 has tiles to flip but player 2 does not
        game.board = [[2, 0, 2, 2, 2, 2, 2, 2], 
                      [2, 2, 2, 2, 1, 1, 1, 1],
                      [2, 1, 2, 1, 1, 1, 1, 1], 
                      [1, 1, 1, 1, 1, 1, 1, 1],
                      [2, 2, 1, 1, 1, 2, 2, 1], 
                      [0, 2, 1, 1, 2, 2, 2, 1], 
                      [1, 2, 1, 2, 2, 2, 2, 1], 
                      [1, 2, 2, 2, 2, 2, 0, 1]]
        game.num_tiles = [30, 31]

        game.current_player = 0
        game.move = (0, 1)
        game.board[0][1] = 1
        game.num_tiles[0] += 1

        game.flip_tiles()
        expected_board = [[2, 1, 2, 2, 2, 2, 2, 2], 
                          [2, 1, 1, 2, 1, 1, 1, 1],
                          [2, 1, 2, 1, 1, 1, 1, 1], 
                          [1, 1, 1, 1, 1, 1, 1, 1],
                          [2, 2, 1, 1, 1, 2, 2, 1], 
                          [0, 2, 1, 1, 2, 2, 2, 1], 
                          [1, 2, 1, 2, 2, 2, 2, 1], 
                          [1, 2, 2, 2, 2, 2, 0, 1]]
        self.assertEqual(game.board, expected_board)
        self.assertEqual(game.num_tiles, [33, 29])

        game.current_player = 1
        moves = [(5, 0), (7, 6)]
        for move in moves:
            game.move = move
            game.flip_tiles()
            self.assertEqual(game.board, expected_board)
            self.assertEqual(game.num_tiles, [33, 29])
    
    def test_make_random_move(self):
        game = Othello()
        game.initialize_board()

        # Test when the board is in the initial state
        game.make_random_move()
        legal_moves = [(2, 3), (3, 2), (5, 4), (4, 5)]
        self.assertIn(game.move, legal_moves)

        # Test after player 1 makes a legal move
        game = Othello()
        game.initialize_board()
        game.move = (2, 3)
        game.make_move()
        
        # Test making random moves for player 2 (white tile)
        game.current_player = 1
        game.make_random_move()
        legal_moves = [(2, 4), (2, 2), (4, 2)]
        self.assertIn(game.move, legal_moves)

        # Test when player 1 has legal moves but player 2 has no legal moves
        # Try making random moves for both players
        game.current_player = 0
        game.board = [[2, 0, 2, 2, 2, 2, 2, 2], 
                      [2, 2, 2, 2, 1, 1, 1, 1],
                      [2, 1, 2, 1, 1, 1, 1, 1], 
                      [1, 1, 1, 1, 1, 1, 1, 1],
                      [2, 2, 1, 1, 1, 2, 2, 1], 
                      [0, 2, 1, 1, 2, 2, 2, 1], 
                      [1, 2, 1, 2, 2, 2, 2, 1], 
                      [1, 2, 2, 2, 2, 2, 0, 1]]
        game.make_random_move()
        legal_moves = [(0, 1), (5, 0), (7, 6)]
        self.assertIn(game.move, legal_moves)

        game.current_player = 1
        game.move = ()
        game.make_random_move()
        self.assertEqual(game.move, ()) 

        # Test when the board is full (both players have no legal moves)
        game.board = [[2, 1, 2, 2, 2, 2, 2, 2], [2, 1, 1, 2, 1, 1, 1, 1],
                      [2, 1, 2, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 2, 1, 1], [1, 1, 1, 1, 1, 2, 1, 1], 
                      [1, 2, 1, 2, 2, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]]
        game.move = ()
        game.make_random_move()
        self.assertEqual(game.move, ()) 

        game.current_player = 0
        game.move = ()
        game.make_random_move()
        self.assertEqual(game.move, ()) 

    def test_str(self):
        # Test for board of size 4x4
        game = Othello(4)
        expected_str = 'Current player: ' + str(game.current_player + 1) + \
                       '\n' + '# of black tiles -- 1: ' + \
                       str(game.num_tiles[0]) + '\n' + \
                       '# of white tiles -- 2: ' + str(game.num_tiles[1]) \
                       + '\n' + 'State of the board:\n' + \
                       '[0, 0, 0, 0]\n' * 4
        self.assertEqual(game.__str__(), expected_str)

        game.initialize_board()
        expected_str = 'Current player: ' + str(game.current_player + 1) + \
                       '\n' + '# of black tiles -- 1: ' + \
                       str(game.num_tiles[0]) + '\n' + \
                       '# of white tiles -- 2: ' + str(game.num_tiles[1]) \
                       + '\n' + 'State of the board:\n' + \
                       '[0, 0, 0, 0]\n' + \
                       '[0, 2, 1, 0]\n' + \
                       '[0, 1, 2, 0]\n' + \
                       '[0, 0, 0, 0]\n'
        self.assertEqual(game.__str__(), expected_str)

        # Test for board of size 8x8
        game = Othello()
        expected_str = 'Current player: ' + str(game.current_player + 1) + \
                       '\n' + '# of black tiles -- 1: ' + \
                       str(game.num_tiles[0]) + '\n' + \
                       '# of white tiles -- 2: ' + str(game.num_tiles[1]) \
                       + '\n' + 'State of the board:\n' + \
                       '[0, 0, 0, 0, 0, 0, 0, 0]\n' * 8
        self.assertEqual(game.__str__(), expected_str)

        game.initialize_board()
        expected_str = 'Current player: ' + str(game.current_player + 1) + \
                       '\n' + '# of black tiles -- 1: ' + \
                       str(game.num_tiles[0]) + '\n' + \
                       '# of white tiles -- 2: ' + str(game.num_tiles[1]) \
                       + '\n' + 'State of the board:\n' + \
                       '[0, 0, 0, 0, 0, 0, 0, 0]\n' + \
                       '[0, 0, 0, 0, 0, 0, 0, 0]\n' + \
                       '[0, 0, 0, 0, 0, 0, 0, 0]\n' + \
                       '[0, 0, 0, 2, 1, 0, 0, 0]\n' + \
                       '[0, 0, 0, 1, 2, 0, 0, 0]\n' + \
                       '[0, 0, 0, 0, 0, 0, 0, 0]\n' + \
                       '[0, 0, 0, 0, 0, 0, 0, 0]\n' + \
                       '[0, 0, 0, 0, 0, 0, 0, 0]\n'
        self.assertEqual(game.__str__(), expected_str)

    def test_eq(self):
        game1 = Othello(4)
        game2 = Othello(4)
        game3 = Othello(8)

        self.assertTrue(game1 == game2)
        self.assertFalse(game1 == game3)
        self.assertFalse(game2 == game3)

        game1.board[0][0] = 1
        self.assertFalse(game1 == game2)

        game2.board[0][0] = 1
        self.assertTrue(game1 == game2)

        game1.current_player = 1
        self.assertFalse(game1 == game2)

        game2.current_player = 1
        self.assertTrue(game1 == game2)

        game2.current_player = 2
        self.assertFalse(game1 == game2)
    
    def test_is_on_board(self):
        '''
            Valid input: every point on the board (including on the line but 
            excluding on the bound)
        '''
        # Test for board of size 4x4
        game = Othello(4)
        
        on_board = [(0.0, 0.0), (40.1, 39.5), (75.0, -77.2), (-22.78, -11.16),
                    (-61.99, 5.0), (50.0, -50.0), (-71.23, 0.0)]
        for point in on_board:    
            self.assertTrue(game.is_on_board(point[0], point[1]))

        not_on_board = [(-100.0, 100.0), (100.0, 100.0), (150.23, 77.0),
                        (5.0, -100.10), (-68.98, 177.54), (-1.5, 200.2)]
        for point in not_on_board:    
            self.assertFalse(game.is_on_board(point[0], point[1]))

        # Test for board of size 8x8
        game = Othello()
        
        on_board = [(0.0, 0.0), (40.1, 39.5), (175.0, -77.2), 
                    (-22.78, -11.16), (-61.99, 195.0), (50.0, -50.0), 
                    (-71.23, 0.0), (99.0, 188.0)]
        for point in on_board:    
            self.assertTrue(game.is_on_board(point[0], point[1]))

        not_on_board = [(-200.0, 200.0), (200.0, 200.0), (250.23, 77.0),
                        (5.0, -200.10), (-368.98, 177.54), (-31.5, 200.2),
                        (320.56, 201.11), (-278.9, -150.3)]
        for point in not_on_board:    
            self.assertFalse(game.is_on_board(point[0], point[1]))

    def test_is_on_line(self):
        # Test for board of size 4x4
        game = Othello(4)

        on_line = [(0.0, 0.0), (-10.12, 0.0), (50.0, 33.11), 
                   (58.62, -50.0), (-50.0, -50.0), (88.26, 50.0)]
        for point in on_line:    
            self.assertTrue(game.is_on_line(point[0], point[1]))  

        not_on_line = [(10.0, 10.0), (-52.3, 28.1), (40.1, 39.5), 
                       (88.77, 100.0), (75.0, -77.2), (-22.78, -11.16), 
                       (-61.99, 5.0), (-100.0, 33.11)]  
        for point in not_on_line:    
            self.assertFalse(game.is_on_line(point[0], point[1])) 
        
        # Test for board of size 8x8
        game = Othello()

        on_line = [(0.0, 0.0), (-10.12, 0.0), (-100.0, 33.11), 
                   (58.62, -150.0), (-50.0, -50.0), (88.26, 100.0),
                   (199.0, 50.0)]
        for point in on_line:    
            self.assertTrue(game.is_on_line(point[0], point[1]))  

        not_on_line = [(10.0, 10.0), (-52.3, 28.1), (140.1, 39.5), 
                       (88.88, 200.0), (75.0, -77.2), (-22.78, -111.16), 
                       (-61.99, 105.0), (200.0, 50.0)]  
        for point in not_on_line:    
            self.assertFalse(game.is_on_line(point[0], point[1])) 

    def test_convert_coord(self):
        # Test for board of size 4x4
        game = Othello(4)

        valid_coords = [(0.0, 0.0), (40.1, 39.5), (75.0, -77.2), 
                        (-22.78, -11.16), (-61.99, 5.0), (-71.23, 0.0)]
        expected_results = [(1, 2), (1, 2), (3, 3), (2, 1), (1, 0), (1, 0)]
        for i in range(len(valid_coords)):
            self.assertEqual(game.convert_coord(valid_coords[i][0], 
                             valid_coords[i][1]), expected_results[i])
        
        invalid_coords = [(-100.0, 100.0), (100.0, 100.0), (150.23, 77.0),
                          (5.0, -100.10), (-68.98, 177.54), (-1.5, 200.2)]
        for i in range(len(invalid_coords)):
            self.assertEqual(game.convert_coord(invalid_coords[i][0], 
                             invalid_coords[i][1]), ())
        
        # Test for board of size 8x8
        game = Othello()

        valid_coords = [(0.0, 0.0), (40.1, 39.5), (175.0, -77.2), 
                        (-22.78, -11.16), (-61.99, 105.1), (-71.23, 0.0),
                        (-159.23, 175.02), (-111.0, 99.9), (82.56, 130.78),
                        (-100.0, 100.0), (100.0, 100.0)]
        expected_results = [(3, 4), (3, 4), (5, 7), (4, 3), (1, 2), (3, 2),
                            (0, 0), (2, 1), (1, 5), (1, 2), (1, 6)]
        for i in range(len(valid_coords)):
            self.assertEqual(game.convert_coord(valid_coords[i][0], 
                             valid_coords[i][1]), expected_results[i])
        
        invalid_coords = [(250.23, 77.0), (5.0, -200.10), (-68.98, 377.54), 
                          (-1.5, 200.0), (200.0, 200.0), (-200.0, -200.0), 
                          (200.0, -100.0)]
        for i in range(len(invalid_coords)):
            self.assertEqual(game.convert_coord(invalid_coords[i][0], 
                             invalid_coords[i][1]), ())
    
    def test_get_coord(self):
        # Test for board of size 4x4
        game = Othello(4)

        # Test valid points (on board but not on line)
        valid_points = [(40.1, 39.5), (75.0, -77.2), (-22.78, -11.16), 
                        (-61.99, 5.0), (-71.23, 1.0)]
        expected_results = [(1, 2), (3, 3), (2, 1), (1, 0), (1, 0)]
        for i in range(len(valid_points)):    
            game.get_coord(valid_points[i][0], valid_points[i][1])
            self.assertEqual(game.move, expected_results[i])

        # Test invalid points (on line or not on board)
        invalid_points = [(0.0, 0.0), (-100.0, 100.0), (150.23, 77.0),
                          (5.0, -100.10), (-68.98, 177.54), (-71.23, 0.0)]           
        for point in invalid_points:
            game.get_coord(point[0], point[1])  
            self.assertEqual(game.move, ())

        # Test for board of size 8x8
        game = Othello()

        # Test valid points (on board but not on line)
        valid_points = [(40.1, 39.5), (175.0, -77.2), 
                        (-22.78, -11.16), (-61.99, 105.1),
                        (-159.23, 175.02), (-111.0, 99.9), (82.56, 130.78)]
        expected_results = [(3, 4), (5, 7), (4, 3), (1, 2),
                            (0, 0), (2, 1), (1, 5)]
        for i in range(len(valid_points)):    
            game.get_coord(valid_points[i][0], valid_points[i][1])
            self.assertEqual(game.move, expected_results[i])

        # Test invalid points (on line or not on board)
        invalid_points = [(0.0, 0.0), (-100.0, 100.0), (100.0, 100.0), 
                          (250.23, 77.0), (5.0, -200.10), (-68.98, 377.54), 
                          (-1.5, 200.0), (200.0, 200.0), (-200.0, -200.0), 
                          (200.0, -100.0), (-71.23, 0.0)]    
        for point in invalid_points:
            game.get_coord(point[0], point[1])  
            self.assertEqual(game.move, ())

    def test_get_tile_start_pos(self):
        # Test for board of size 4x4
        game = Othello(4)
        invalid_squares = [(), (4, 1), (4, 4), (0, 4), (-2, 4), (5, 9), 
                           (-6, -3), (4, -3), (8, 3), (2, -4), (1, 20)]
        for square in invalid_squares:
            self.assertEqual(game.get_tile_start_pos(square), ())
        
        valid_squares = [(0, 0), (1, 0), (2, 3), (3, 3), (1, 2), (3, 1)]
        expected_results = [((-95.0, 75.0), -20), ((-95.0, 25.0), -20), 
                            ((95.0, -25.0), 20), ((95.0, -75.0), 20), 
                            ((45.0, 25.0), 20), ((-45.0, -75.0), -20)]
        for i in range(len(valid_squares)):
            self.assertEqual(game.get_tile_start_pos(valid_squares[i]), 
                             expected_results[i]) 
        
        # Test for board of size 8x8
        game = Othello()
        invalid_squares = [(), (8, 1), (8, 8), (0, 8), (-2, 8), (5, 9), 
                           (-6, -3), (8, -3), (12, 3), (2, -4), (1, 20)]
        for square in invalid_squares:
            self.assertEqual(game.get_tile_start_pos(square), ())
        
        valid_squares = [(0, 0), (1, 0), (5, 3), (3, 7), (1, 2), (6, 6)]
        expected_results = [((-195.0, 175.0), -20), ((-195.0, 125.0), -20),
                             ((-45.0, -75.0), -20), ((195.0, 25.0), 20),
                             ((-95.0, 125.0), -20), ((145.0, -125.0), 20)]
        for i in range(len(valid_squares)):
            self.assertEqual(game.get_tile_start_pos(valid_squares[i]), 
                             expected_results[i]) 


class TestBoard(unittest.TestCase):
    '''
        Test extra methods (different from those in class Othello) 
        for class Board
    '''
    def test_str(self):
        # Test for board of size 4x4
        board = Board(4)
        expected_str = 'State of the board:\n' + '[0, 0, 0, 0]\n' * 4
        self.assertEqual(board.__str__(), expected_str)

        # Test for board of size 8x8
        board = Board(8)
        expected_str = 'State of the board:\n' + \
                       '[0, 0, 0, 0, 0, 0, 0, 0]\n' * 8
        self.assertEqual(board.__str__(), expected_str)

    def test_eq(self):
        board1 = Board(4)
        board2 = Board(4)
        board3 = Board(8)

        self.assertTrue(board1 == board2)
        self.assertFalse(board1 == board3)
        self.assertFalse(board2 == board3)

        board1.board[0][0] = 1
        self.assertFalse(board1 == board2)

        board2.board[0][0] = 1
        self.assertTrue(board1 == board2)

class TestScore(unittest.TestCase):
    '''
        Test functions in score module
    '''
    def test_read_scores(self):
        # Test reading a file that doesn't exist
        self.assertEqual(score.read_scores('file_not_exist.txt'), '')

        # Test reading an empty file
        self.assertEqual(score.read_scores('test_read_empty_file.txt'), '')

        # Test reading a file containing some scores
        expected_data = ('asdef32 48\nYES!!! 38\ndog ee 37\nKing 14\n'
                         'asa 2\nLI*(02 12gh 12\nsadness 4\n'
                         'James W. 9\nKing 3\n... 27\n')
        self.assertEqual(score.read_scores('test_read_scores.txt'), 
                         expected_data)
    
    def test_write_scores(self):
        # Test writing a file that doesn't exist
        score.write_scores('Green 28\n', 'test_write_new_file.txt')

        infile = open('test_write_new_file.txt', 'r')
        score1 = infile.read()
        infile.close()

        self.assertEqual(score1, 'Green 28\n')

        # Test writing an empty file
        score.write_scores('Sasa 17\n', 'test_write_empty_file.txt')
        infile = open('test_write_empty_file.txt', 'r')
        score2 = infile.read()
        infile.close()
        self.assertEqual(score2, 'Sasa 17\n')

        # Test writing a file containing some scores (append the score)
        score.write_scores('Sasa 17\n', 'test_write_scores1.txt')
        infile = open('test_write_scores1.txt', 'r')
        scores = infile.read()
        infile.close()
        expected_scores = ('asdef32 48\nYES!!! 38\ndog ee 37\nKing 14\n'
                           'asa 2\nLI*(02 12gh 12\nsadness 4\n'
                           'James W. 9\nKing 3\n... 27\nSasa 17\n')
        self.assertEqual(scores, expected_scores)

        # Test rewriting a file containing some scores
        new_scores = 'Kate 50\nasdef32 48\nYES!!! 38\ndog ee 37\nKing 14\n'
        score.write_scores(new_scores, 'test_write_scores2.txt', 'w')
        infile = open('test_write_scores2.txt', 'r')
        scores = infile.read()
        infile.close()
        self.assertEqual(scores, new_scores)

    def test_update_scores(self):
        # Test updating a file that doesn't exist
        new_record = score.update_scores('Green', 28, 
                     'test_update_new_file.txt')
        self.assertEqual(new_record, 'Green 28')

        infile = open('test_update_new_file.txt', 'r')
        scores = infile.read()
        infile.close()
        self.assertEqual(scores, 'Green 28\n')

        # Test updating an empty file
        new_record = score.update_scores('Sasa', 17, 
                     'test_update_empty_file.txt')
        self.assertEqual(new_record, 'Sasa 17')   

        infile = open('test_update_empty_file.txt', 'r')
        scores = infile.read()
        infile.close()
        self.assertEqual(scores, 'Sasa 17\n')

        # Test updating a file containing some scores
        # Writing a score lower than the highest score in the file
        new_record = score.update_scores('King', 14, 
                     'test_update_scores1.txt')
        self.assertEqual(new_record, 'King 14')   

        infile = open('test_update_scores1.txt', 'r')
        scores = infile.read()
        infile.close()
        expected_scores = 'asdef32 48\nYES!!! 38\ndog ee 37\nKing 14\n'
        self.assertEqual(scores, expected_scores)

        # Test updating another file containing some scores
        # Writing a score higher than the highest score in the file
        new_record = score.update_scores('King', 50, 
                     'test_update_scores2.txt')
        self.assertEqual(new_record, 'King 50')   

        infile = open('test_update_scores2.txt', 'r')
        scores = infile.read()
        infile.close()
        expected_scores = 'King 50\nasdef32 48\nYES!!! 38\ndog ee 37\n'
        self.assertEqual(scores, expected_scores)


def main():
    unittest.main(verbosity = 3)


main()


