## sudoku solver by joshua
import copy
import sudokus

def SudokuSolver(SUDOKU):
    
    SIZE = 9
    
    def GenArray():
        array = []
        for i in range(SIZE):
            sub_array = []
            for j in range(SIZE):
                #Set defaults
                if SUDOKU[i][j] == 0:
                    sub_array.append({
                        "state": False,
                        "options": [1,2,3,4,5,6,7,8,9],
                        "number": 0
                        })
                if SUDOKU[i][j] != 0:
                    sub_array.append({
                        "state": True,
                        "options": None,
                        "number": int(SUDOKU[i][j])
                        })
            array.append(sub_array)
        return array
    
    def status():
        for i in range(SIZE):
            for j in range(SIZE):
                if SUDOKU[i][j] == 0:
                    return False
        return True
    
    def OnesAvailabe():
        for i in range(SIZE):
            for j in range(SIZE):
                if struct[i][j]["state"] == True:
                    continue
                if struct[i][j]["state"] == False:
                    if len(struct[i][j]["options"]) == 1:
                        return True
        return False

    def Block(i,j,SUDOKU=SUDOKU):
        block = SUDOKU[3*(i // 3)][3*(j // 3):3*(j // 3)+3] + \
            SUDOKU[3*(i // 3)+1][3*(j // 3):3*(j // 3)+3] + \
                SUDOKU[3*(i // 3)+2][3*(j // 3):3*(j // 3)+3]
        return block

    def Horizontal(i,SUDOKU=SUDOKU):
        return SUDOKU[i]

    def Vertical(j,SUDOKU=SUDOKU):
        return [row[j] for row in SUDOKU]

    def Options_Block(I,J):
        possibilities = []
        for y in range(3):
            for x in range(3):
                X = 3*(J // 3)+x
                Y = 3*(I // 3)+y
                if (Y == I) and (X == J):
                    continue
                if struct[Y][X]["state"] == True:
                    continue
                if struct[Y][X]["state"] == False:
                    possibilities.extend(struct[Y][X]["options"])
        return possibilities

    def Analyse(struct):
        for i in range(SIZE):
            for j in range(SIZE):
                if struct[i][j]["state"] == True:
                    continue
                if struct[i][j]["state"] == False:
                    options = struct[i][j]["options"][:]
                    #scanning options
                    for option in options:
                        #horizontal
                        if option in Horizontal(i):
                            struct[i][j]["options"].remove(option)
                            continue
                        #vertical
                        if option in Vertical(j):
                            struct[i][j]["options"].remove(option)
                            continue
                        #block
                        if option in Block(i,j):
                            struct[i][j]["options"].remove(option)
                            continue
        return struct
    
    def possible(grid, y, x, n):
        # Horizontal
        if n in Horizontal(y,grid):
            return False
        # Vertical
        if n in Vertical(x,grid):
            return False
        # Block
        if n in Block(y,x,grid):
            return False

        return True

    def solve(grid):
        def find_empty(grid):
            for i in range(SIZE):
                for j in range(SIZE):
                    if grid[i][j] == 0:
                        return i,j
            return None
        empty = find_empty(grid)
        if not empty:
            return True
        y, x = empty
        options = struct[y][x]["options"][:]
        for option in options:
            if possible(grid, y, x, option):
                grid[y][x] = option
                if solve(grid):
                    return True
                grid[y][x] = 0

    struct = GenArray()

    solved = False

    #Solver
    while not solved:

        before_iter = copy.deepcopy(SUDOKU)
        struct = Analyse(struct)

        #fill in (First scan is redundant, the second scan takes care of everything)
        # ↓ redundancy below (essentialy does the same as the loops later but less checks happen)
        for i in range(SIZE):
            for j in range(SIZE):
                if struct[i][j]["state"] == True:
                    continue
                if struct[i][j]["state"] == False:
                    if len(struct[i][j]["options"]) == 1:
                        number = int(struct[i][j]["options"][0])
                        struct[i][j]["state"] = True
                        struct[i][j]["options"] = None
                        struct[i][j]["number"] = number
                        SUDOKU[i][j] = number

        struct = Analyse(struct)
        if not OnesAvailabe():
            for i in range(SIZE):
                for j in range(SIZE):
                    if struct[i][j]["state"] == True:
                        continue
                    if struct[i][j]["state"] == False:
                        options = struct[i][j]["options"][:]
                        for option in options:
                            if option not in Options_Block(i,j):
                                struct[i][j]["state"] = True
                                struct[i][j]["options"] = None
                                struct[i][j]["number"] = option
                                SUDOKU[i][j] = option
                                struct = Analyse(struct)

        after_iter = copy.deepcopy(SUDOKU)

        if after_iter == before_iter:
            solve(SUDOKU)
            return SUDOKU
        
        solved = status()

    return SUDOKU

if __name__ == "__main__":
    SudokuSolver(sudokus.Sudoku3)
