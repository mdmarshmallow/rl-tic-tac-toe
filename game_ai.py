import table as tb
import pandas as pd
import numpy as np

table = None

EXPLORE_CHANCE = 10
ALPHA = 0.15


def choose_move(state):
    print(state)
    global table
    if table is None:
        # loads table as a pandas data frame
        table = tb.load_table()
    # add the initial state to the table if not there
    table_entry = table[table['board'] == ''.join(state)]
    if table_entry.empty:
        row_to_add = pd.DataFrame([[''.join(state), 0.5]], columns=['board', 'value'])
        table = table.append(row_to_add, ignore_index=True)
    # get all possible states from every possible move
    possible_states = []
    state_change = []
    for i in range(0, len(state)):
        if state[i] == 'b':
            possible_state = list(state)
            possible_state[i] = 'o'
            possible_states.append(possible_state)
            state_change.append(i)
    # maps states to each probability
    state_values = []
    for possible_state in possible_states:
        table_entry = table[table['board'] == ''.join(possible_state)]
        if table_entry.empty:
            state_values.append(0.5)
            # update the table with the new entry
            row_to_add = pd.DataFrame([[''.join(possible_state), 0.5]], columns=['board', 'value'])
            table = table.append(row_to_add, ignore_index=True)
        else:
            # TODO: check this code
            value = table[table['board'] == ''.join(possible_state)]['value']
            state_values.append(value)
    # chooses whether or not to explore
    if np.random.uniform(0.0, 100.0) < EXPLORE_CHANCE:
        # chooses a random move from state_change
        random_index = int(np.float64(np.round(np.random.uniform(0.0, len(state_change) - 1))).item())
        return state_change[random_index]
    # gets the state changes with the highest value
    max_state_changes = []
    largest_value = -1
    for i in range(0, len(state_change)):
        if not max_state_changes:
            max_state_changes.append(state_change[i])
            largest_value = state_values[i]
        elif state_values[i] == largest_value:
            max_state_changes.append(state_change[i])
        elif state_values[i] > largest_value:
            max_state_changes.clear()
            max_state_changes.append(state_change[i])
            largest_value = state_values[i]
    # choose the final state to change
    # if there are multiple maximum state changes, choose one at random
    if len(max_state_changes) > 1:
        random_change_index = int(np.float64(np.round(np.random.uniform(0.0, len(max_state_changes) - 1))).item())
        max_state_change = max_state_changes[random_change_index]
    else:
        max_state_change = max_state_changes[0]
    # get the next state
    next_state = list(state)
    next_state[max_state_change] = 'o'
    # update the table
    current_state_value = float(table[table['board'] == ''.join(state)]['value'])
    next_state_value = float(table[table['board'] == ''.join(next_state)]['value'])
    # calculate new current state value
    current_state_value = current_state_value + ALPHA * (next_state_value - current_state_value)
    # updates table
    table.loc[table['board'] == ''.join(state), 'value'] = current_state_value
    print(float(table[table['board'] == ''.join(state)]['value']))
    return max_state_change
