'''
    Siyan
    CS5001
    Fall 2018
    November 28, 2018
'''

import turtle

# Defines sizes of the square and tile, colors of the board, line, 
# and tile as constants
SQUARE = 50
TILE = 20
BOARD_COLOR = 'forest green'
LINE_COLOR = 'black'
TILE_COLORS = ['black', 'white']

class Board:
    ''' Board class.
        Attributes: n, an integer for number of squares for a row/column
                    board, a nested list which stores the state of the board
                    (0 for no tile, 1 for black tiles and 2 for white tiles)
                    square_size, an integer for size of the squares
                    board_color, a string for color of the board
                    line_color, a string for color of the lines of the board
                    tile_size, an integer for size of the radius of the tile
                    tile_colors, a list of strings for colors of the tile
                    move, a tuple for coordinates of the player's next move
        n (integer) is required in the __init__ function
        board (list), square_size (integer), board_color (string), 
        line_color (string), tile_size (integer), tile_colors (list), 
        move (tuple) are not taken in the __init__

        Methods: draw_board, draw_lines, is_on_board, is_on_line, 
                 convert_coord, get_coord, get_tile_start_pos, draw_tile, 
                 __str__ and __eq__
    '''

    def __init__(self, n):
        ''' 
            Initilizes the attributes. 
            Only takes one required parameter; others have default values.
        '''
        self.n = n
        self.board = [[0] * n for i in range(n)]
        self.square_size = SQUARE
        self.board_color = BOARD_COLOR
        self.line_color = LINE_COLOR
        self.tile_size = TILE
        self.tile_colors = TILE_COLORS
        self.move = ()

    def draw_board(self):
        ''' Method: draw_board
            Parameters: self
            Returns: nothing
            
            Does: Draws an nxn board. Color of the board and lines are set 
                  to self.board_color and self.line_color respectively.
        '''
        turtle.setup(self.n * self.square_size + self.square_size, 
                    self.n * self.square_size + self.square_size)
        turtle.screensize(self.n * self.square_size, self.n * self.square_size)
        turtle.bgcolor('white')

        # Create the turtle to draw the board
        othello = turtle.Turtle(visible = False)
        othello.penup()
        othello.speed(0)
        othello.hideturtle()

        # Set line color and fill color
        othello.color(self.line_color, self.board_color)
        
        # Move the turtle to the upper left corner
        corner = -self.n * self.square_size / 2
        othello.setposition(corner, corner)
        
        # Draw the board background
        othello.begin_fill()
        for i in range(4):
            othello.pendown()
            othello.forward(self.square_size * self.n)
            othello.left(90)
        othello.end_fill()
        
        # Draw the horizontal lines
        for i in range(self.n + 1):
            othello.setposition(corner, self.square_size * i + corner)
            self.draw_lines(othello)
        
        # Draw the vertical lines
        othello.left(90)
        for i in range(self.n + 1):
            othello.setposition(self.square_size * i + corner, corner)
            self.draw_lines(othello)

    def draw_lines(self, turt):
        ''' Method: draw_lines
            Parameters: self, turt (turtle object)
            Returns: nothing

            Does: Draws lines of the board.
        '''
        turt.pendown()
        turt.forward(self.square_size * self.n)
        turt.penup()

    def is_on_board(self, x, y):
        ''' Method: is_on_board
            Parameters: self, x (float), y (float)
            Returns: boolean (True if the point is on board, False otherwise)

            Does: Checks whether the given point is on the board.
                
                  About the input: (x, y) are the coordinates of a point 
                  on the screen.
        '''
        bound = self.n / 2 * self.square_size
        
        if - bound < x < bound and - bound < y < bound:
            return True
        return False

    def is_on_line(self, x, y):
        ''' Method: is_on_board
            Parameters: self, x (float), y (float)
            Returns: boolean (True if the point is on line, False otherwise)

            Does: Checks whether the given point is on the line (i.e, the 
                  boundary of a square).
                
                  About the input: (x, y) are the coordinates of a point 
                  on the screen.
        '''
        if self.is_on_board(x, y):   
            if x % self.square_size == 0 or y % self.square_size == 0:
                return True
        return False

    def convert_coord(self, x, y):
        ''' Method: convert_coord
            Parameters: self, x (float), y (float)
            Returns: a tuple of integers (row, col)

            Does: Converts the coordinates from (x, y) to (row, col).
                
                  About the input: (x, y) are the coordinates of a point 
                  on one of the squares of the board.
        '''
        if self.is_on_board(x, y):
            row = int(self.n / 2 - 1 - y // self.square_size)
            col = int(self.n / 2 + x // self.square_size)
            return (row, col)
        return ()

    def get_coord(self, x, y):
        ''' Method: get_coord
            Parameters: self, x (float), y (float)
            Returns: nothing
            
            Does: Gets and converts the (x, y) coordinates of where the user 
                  clicks. If the user clicks on the board, converts (x, y) 
                  to (row, col) and saves the result to self.move; otherwise, 
                  sets self.move to an empty tuple.
        '''
        if self.is_on_board(x, y) and not self.is_on_line(x, y):
            self.move = self.convert_coord(x, y)
        else:
            self.move = ()

    def get_tile_start_pos(self, square):
        ''' Method: get_tile_start_pos
            Parameters: self, square (tuple of integers)
            Returns: a tuple containing the (x, y) coordinates of the starting 
                     position for drawing the tile and the radius of the tile
            
            Does: Calculates the (x, y) coordinates of the starting position
                  for drawing the tile, and sets the radius of the tile to
                  draw.
                  
                  About the input: square is the (row, col) of a square
        '''
        if square == ():
            return ()
        
        for i in range(2):
            if square[i] not in range(self.n):
                return ()

        row, col = square[0], square[1]

        y = ((self.n - 1) / 2 - row) * self.square_size
        if col < self.n / 2:
            x = (col - (self.n - 1) / 2) * self.square_size - self.tile_size
            r = - self.tile_size
        else:
            x = (col - (self.n - 1) / 2) * self.square_size + self.tile_size
            r = self.tile_size
        
        return ((x, y), r)

    def draw_tile(self, square, color):
        ''' Method: draw_tile
            Parameters: self, square (tuple of integers), color (integer)
            Returns: nothing
            Does: Draws a tile of a specific color on the board 
                  using turtle graphics.
                
                  About the input: square is the (row, col) of the square in 
                  which the tile is drawn; color is an integer 0 or 1 to 
                  represent the 1st or 2nd color in the list of colors 
                  (self.colors) to use.
        '''
        # Get starting position and radius of the tile
        pos = self.get_tile_start_pos(square)
        if pos:
            coord = pos[0]
            r = pos[1]
        else:
            print('Error drawing the tile...')
            return
        
        # Create the turtle to draw the tile
        tile = turtle.Turtle(visible = False)
        tile.penup()
        tile.speed(0)
        tile.hideturtle()

        # Set color of the tile
        tile.color(self.tile_colors[color])

        # Move the turtle to the starting postion for drawing
        tile.setposition(coord)
        tile.setheading(90)
        
        # Draw the tile
        tile.begin_fill()
        tile.pendown()
        tile.circle(r)
        tile.end_fill()

    def __str__(self):
        ''' 
            Returns a printable version of the board to print.
        '''
        explanation = 'State of the board:\n'
        board_str = ''
        for row in self.board:
            board_str += str(row) + '\n' 
        printable_str = explanation + board_str

        return printable_str

    def __eq__(self, other):
        '''
            Compares two instances. 
            Returns True if they have the same board attribute, 
            False otherwise.
        '''
        return self.board == other.board
