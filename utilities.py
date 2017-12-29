"""
    Utilities.py is based on Peter Norwig tutorial on Sudoku solving using Search
    and Constrain Propagation ideas.
    Tutorial URL: http://norvig.com/sudoku.html
"""

rows = 'ABCDEFGHI'
cols = '123456789'
boxes = [r + c for r in rows for c in cols]
history = {}  # history must be declared here so that it exists in the assign_values scope


def cross(A, B):
    """Cross product of elements in A and elements in B """
    return [x+y for x in A for y in B]


row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]

diag_a = [str(rows[i])+str(cols[i]) for i in range(len(rows))]
diag_b = [str(rows[i])+str(cols[8-i]) for i in range(len(rows))]
diagonal_units = [diag_a, diag_b]

unitlist = row_units + column_units + square_units + diagonal_units

units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)


def grid2values(string_of_values):
    ''' A function to convert the string representation of a puzzle into a dictionary form '''
    assert len(string_of_values) == 81
    new_dict = dict()
    for index, key in enumerate(boxes):
        if string_of_values[index] == '.':
            new_dict[key] = '123456789'
        else:
            new_dict[key] = string_of_values[index]
    return new_dict


def display(values):
    """Display the values as a 2-D grid."""
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    print()
