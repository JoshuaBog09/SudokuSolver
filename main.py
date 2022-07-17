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

    struct = GenArray()

    solved = False

    #Solver
    while not solved:
        #analyse
        for i in range(SIZE):
            for j in range(SIZE):
                if struct[i][j]["state"] == True:
                    continue
                if struct[i][j]["state"] == False:
                    options = struct[i][j]["options"][:]
                    #scanning options
                    for option in options:
                        #horizontal
                        if option in SUDOKU[i]:
                            struct[i][j]["options"].remove(option)
                            continue
                        #vertical
                        if option in [row[j] for row in SUDOKU]:
                            struct[i][j]["options"].remove(option)
                            continue
                        #block
                        block = SUDOKU[3*(i // 3)][3*(j // 3):3*(j // 3)+3] + \
                            SUDOKU[3*(i // 3)+1][3*(j // 3):3*(j // 3)+3] + \
                                SUDOKU[3*(i // 3)+2][3*(j // 3):3*(j // 3)+3]
                        if option in block:
                            struct[i][j]["options"].remove(option)
                            continue
        if not OnesAvailabe():
            """
            A guess will need to be made here, for a cell with to options.
            If the guess doesn't work the other instance needs to be taken 
            """
            print("Currently unsolvable")
            print(struct)
            return None

        #fill in
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

        solved = status()
        Loops += 1

    print("----------------")
    print(SUDOKU, f"Solved after {Loops} iterations")
    print("----------------")
    return SUDOKU

if __name__ == "__main__":
    print(SudokuSolver(sudokus.Sudoku2))
