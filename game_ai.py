import numpy as np
import table as tb

table = None


def choose_move(state):
    global table
    if table is None:
        table = tb.load_table()
    print(table)
    return 7
