import numpy as np

#create empty 6 dimensional ndarray for 3x3 cube

cube = np.empty((6, 3, 3), dtype = 'U6')

#function to generate a 6x6 ndarray with the given letter indexes

def indexing(letter):
    side = np.empty(9, dtype = 'U6')
    for index in np.arange(9):
        side[index] = letter + str(index)
    return side.reshape(3, 3)

#reset the cube ndarray to default instances

def reset():
    letters = np.array(['B', 'R', 'G', 'O', 'Y', 'W'])
    x = 0
    for l in letters:
        cube[x] = indexing(l)
        x += 1
    print('Cube Reset!')

# Front Turn (F)

def front_turn():
    original_cube = np.copy(cube)
    cube[1, :, 0]  = original_cube[4, -1, :]
    cube[4, -1, :] = original_cube[3, :, -1]
    cube[3, :, -1] = original_cube[-1, 0, :]
    cube[-1, 0, :] = np.flip(original_cube[1, :, 0])
    cube[0] = np.flip(cube[0].T, axis=1)
    return cube