'''
    Siyan
    CS5001
    Fall 2018
    November 30, 2018
'''

import othello

def main():
    # Initializes the game
    game = othello.Othello()
    game.draw_board()
    game.initialize_board()

    # Starts playing the game
    # The user makes a move by clicking one of the squares on the board
    # The computer makes a random legal move every time
    # Game is over when there are no more lagal moves or the board is full
    game.run()


main()
