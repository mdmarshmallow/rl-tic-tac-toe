import pandas as pd
from os import path


def generate_table():
    end_game_csv = pd.read_csv('end_game.csv')
    df = pd.DataFrame(end_game_csv)
    # gets all the rows where x wins
    x_df = df[df['class']]
    # changes class column to value columns of o
    x_df = x_df.rename(columns={'class': 'value'})
    x_df['value'] = 0
    # combines the board positions into one board column
    x_df['board'] = x_df[['TL', 'TM', 'TR', 'ML', 'MM', 'MR', 'BL', 'BM', 'BR']].apply(lambda x: ''.join(x), axis=1)
    x_df = x_df[['board', 'value']]

    # reverse the x data frame to make an o data frame
    def reverse_board(board_string):
        reversed_board = ''
        for elem in board_string:
            if elem == 'b':
                reversed_board += elem
            elif elem == 'x':
                reversed_board += 'o'
            else:
                reversed_board += 'x'
        return reversed_board
    o_df = pd.DataFrame(x_df['board'].apply(reverse_board))
    o_df['value'] = 1
    val_df = x_df.append(o_df, ignore_index=True)
    val_df.to_csv(r"value_table.csv")


def load_table():
    if not path.exists("value_table.csv"):
        generate_table()
    value_table_csv = pd.read_csv("value_table.csv")
    return pd.DataFrame(value_table_csv)[['board', 'value']]
