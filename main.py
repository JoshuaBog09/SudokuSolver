## sudoku solver by joshua
import sudokus

def SudokuSolver(SUDOKU):
    
    SIZE = 9
    Loops = 0
    SUDOKU = SUDOKU
    
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

    def Block(i,j):
        block = SUDOKU[3*(i // 3)][3*(j // 3):3*(j // 3)+3] + \
            SUDOKU[3*(i // 3)+1][3*(j // 3):3*(j // 3)+3] + \
                SUDOKU[3*(i // 3)+2][3*(j // 3):3*(j // 3)+3]
        return block

    def Horizontal(i):
        return SUDOKU[i]

    def Vertical(j):
        return [row[j] for row in SUDOKU]

    def Options_Horizontal(I,J):
        possibilities = []
        for x in range(SIZE):
            if x == J:
                possibilities.append(0)
                continue
            if struct[I][x]["state"] == True:
                possibilities.append(1)
                continue
            if struct[I][x]["state"] == False:
                possibilities.append(struct[I][x]["options"])
        return possibilities

    def Options_Vertical(I,J):
        possibilities = []
        for y in range(SIZE):
            if y == I:
                continue
            if struct[y][J]["state"] == True:
                continue
            if struct[y][J]["state"] == False:
                possibilities.extend(struct[y][J]["options"])
        return possibilities

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

    struct = GenArray()

    solved = False

    #Solver
    while not solved:

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

        if Loops >= 1_000:
            print("Failed")
            return None
        solved = status()
        Loops += 1

    print("----------------")
    print(SUDOKU, f"Solved after {Loops} iterations")
    print("----------------")

    return SUDOKU

if __name__ == "__main__":
    SudokuSolver(sudokus.Sudoku3)
