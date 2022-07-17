import unittest
import sudokus
import main

class TestSudokuSolver(unittest.TestCase):

    def test_sudoku1(self):
        self.assertEqual(main.SudokuSolver(sudokus.Sudoku1),(
            [[4, 6, 5, 7, 3, 8, 1, 9, 2], 
             [3, 7, 8, 2, 9, 1, 5, 6, 4],
             [1, 2, 9, 6, 5, 4, 8, 7, 3],
             [2, 4, 1, 3, 6, 9, 7, 5, 8],
             [6, 5, 3, 8, 2, 7, 4, 1, 9],
             [9, 8, 7, 4, 1, 5, 2, 3, 6],
             [8, 1, 4, 9, 7, 3, 6, 2, 5],
             [5, 3, 2, 1, 4, 6, 9, 8, 7],
             [7, 9, 6, 5, 8, 2, 3, 4, 1]]))
    
    def test_sudoku2(self):
        pass

if __name__ == '__main__':
    unittest.main()