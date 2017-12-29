'''
    Solver is based on ideas of Constrain Propagation and Search, presented by
    Peter Norwig in a tutorial: http://norvig.com/sudoku.html
'''

from utilities import *

#
# Strageties to solve Sudoku
#

# QUESTION: Code works for given tests but it runs into trouble for boards from internet,
# namely -- code doesn't 'stall' even on first board and encounters a box with no
# values at all, thus game stops.
# TODO: Need to implement recursion for board-posibilities-tree for Constrain-Propagation, just like in Search,
# so that when board is False, return to previous variant.


def naked_twins(values):
    for peer_family in [row_units, column_units, square_units]:
        for peer_list in peer_family:
            working_list = [(box, values[box]) for box in peer_list if len(values[box]) > 1]
            values_list_per_peer_set = [values[box] for box in peer_list]

            for box, value in working_list:
                if len(value) == 2 and values_list_per_peer_set.count(value) == 2:

                    # Remove digits of value from other boxes
                    for i, y in working_list:
                        if len(y) > 1 and i != box and y != value:
                            # DEBUG: print(i, 'is not', box, 'and value is', y,'. Removing:', value[0], value[1])
                            values[i] = values[i].replace(value[0], "")
                            values[i] = values[i].replace(value[1], "")
                            # DEBUG: print('Now value at box {} is {}'.format(i, values[i]))
    return values


def eliminate(values):
    '''Eliminate values from peers when one of peers is chosen'''
    for key, value in values.items():
        if len(value) == 1:
            for peer_key in list(peers[key]):
                values[peer_key] = values[peer_key].replace(value, "")
    return values


def only_choice(values):
    '''Set a value to box when a value is the only choice given peers'''
    for digit in '123456789':
        for unit in unitlist:
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values


def reduce_puzzle(values):
    '''Propogate constrains repeatedly to eliminate possibilities.'''
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        print("...........Elimination executed.")
        display(values)
        values = only_choice(values)
        print('...........Only Choice executed.')
        display(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


def search(values):
    '''Use Depth First Search if a Sudoku is not solved by Constrain Propagation alone.'''

    # Constrain propagation
    values = reduce_puzzle(values)
    if values == False:
        return False
    if all(len(values[s])==1 for s in boxes):
        return values

    # Depth first search
    box_id = min(  [  (s, len(values[s])) for s in boxes if len(values[s]) > 1  ], key=lambda t: t[1])[0]

    for value in values[box_id]:
        print("....................................Search: {} in a {}".format(value, values[box_id]))
        new_sudoku = values.copy()
        new_sudoku[box_id] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt


def solve(grid):
    values = grid2values(grid)
    values = search(values)
    return values

def load_board_from_file():
    filepath = 'input.txt'
    try:
        with open(filepath, 'r') as f:
            print("OK. File loaded.")
            return f.readline()
    except:
        print('Oops! File is not loaded.')


if __name__ == "__main__":
    sudoku_str = str(load_board_from_file())
    display(grid2values(sudoku_str))
    game = solve(sudoku_str)
    if game:
        display(game)
