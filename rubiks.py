import numpy as np

cube = np.empty((6, 3, 3), dtype = 'U6')

def indexing(letter):
    side = np.empty(9, dtype = 'U6')
    for index in np.arange(9):
        side[index] = letter + str(index)
    return side.reshape(3, 3)

def reset():
    letters = np.array(['B', 'R', 'G', 'O', 'Y', 'W'])
    x = 0
    for l in letters:
        cube[x] = indexing(l)
        x += 1
    print('Cube Reset!')
