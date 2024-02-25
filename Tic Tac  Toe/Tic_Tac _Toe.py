#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 21:10:19 2024

@author: ahmedeldesoky
"""

def create_board():
  """Initializes the game board as a 3x3 list of empty strings."""
  return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
  """Prints the game board in a user-friendly format."""
  for row in board:
    print('| ' + ' | '.join(row) + ' |')
  print('-' * 9)

def handle_move(board, player, symbol):
  """Takes player move, validates it, and updates the game board."""
  while True:
    move = input(f"Player {player}, enter your move (row,col): ").split(',')
    try:
      row, col = int(move[0]), int(move[1])
      if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
        board[row][col] = symbol
        return
      else:
        print("Invalid move. Try again.")
    except ValueError:
      print("Invalid input format. Please enter row and column as numbers separated by a comma.")

def check_win(board, symbol):
  """Checks if the given symbol has achieved a win (rows, columns, diagonals)."""
  # Check rows and columns
  for i in range(3):
    if all(board[i][j] == symbol for j in range(3)):
      return True
    if all(board[j][i] == symbol for j in range(3)):
      return True
  # Check diagonals
  if all(board[i][i] == symbol for i in range(3)):
    return True
  if all(board[i][2-i] == symbol for i in range(3)):
    return True
  return False

def check_tie(board):
  """Checks if all squares are filled, indicating a tie."""
  return all(symbol != ' ' for row in board for symbol in row)

def main():
  """Main game loop that handles player turns and game logic."""
  board = create_board()
  player = 1
  symbol = 'X'

  while True:
    print_board(board)
    handle_move(board, player, symbol)

    if check_win(board, symbol):
      print_board(board)
      print(f"Player {player} wins!")
      break

    if check_tie(board):
      print_board(board)
      print("It's a tie!")
      break

    player = player % 2 + 1
    symbol = 'O' if symbol == 'X' else 'X'

if __name__ == "__main__":
  main()
