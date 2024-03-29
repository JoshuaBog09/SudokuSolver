import unittest
import sudokus
import sudokusolver

class TestSudokuSolver(unittest.TestCase):

    def test_Easy1(self):
        self.assertEqual(sudokusolver.SudokuSolver(sudokus.Sudoku1),(
            [[4, 6, 5, 7, 3, 8, 1, 9, 2], 
             [3, 7, 8, 2, 9, 1, 5, 6, 4],
             [1, 2, 9, 6, 5, 4, 8, 7, 3],
             [2, 4, 1, 3, 6, 9, 7, 5, 8],
             [6, 5, 3, 8, 2, 7, 4, 1, 9],
             [9, 8, 7, 4, 1, 5, 2, 3, 6],
             [8, 1, 4, 9, 7, 3, 6, 2, 5],
             [5, 3, 2, 1, 4, 6, 9, 8, 7],
             [7, 9, 6, 5, 8, 2, 3, 4, 1]]))
    
    def test_Easy2(self):
        self.assertEqual(sudokusolver.SudokuSolver(sudokus.Sudoku2),(
            [[1, 8, 2, 3, 7, 5, 4, 6, 9], 
            [3, 5, 9, 6, 4, 8, 2, 7, 1],
            [7, 4, 6, 1, 2, 9, 3, 8, 5],
            [9, 6, 5, 4, 8, 2, 7, 1, 3],
            [2, 7, 1, 5, 3, 6, 9, 4, 8],
            [4, 3, 8, 7, 9, 1, 6, 5, 2],
            [6, 2, 4, 8, 1, 3, 5, 9, 7],
            [8, 9, 7, 2, 5, 4, 1, 3, 6],
            [5, 1, 3, 9, 6, 7, 8, 2, 4]]))

    def test_Medium(self):
        self.assertEqual(sudokusolver.SudokuSolver(sudokus.Sudoku3),(
            [[8, 7, 1, 6, 5, 9, 2, 3, 4],
             [4, 5, 9, 3, 1, 2, 6, 8, 7], 
             [3, 2, 6, 4, 7, 8, 5, 9, 1], 
             [9, 3, 4, 7, 2, 5, 1, 6, 8], 
             [6, 1, 2, 9, 8, 3, 7, 4, 5], 
             [7, 8, 5, 1, 6, 4, 9, 2, 3], 
             [2, 4, 3, 5, 9, 1, 8, 7, 6], 
             [1, 6, 8, 2, 4, 7, 3, 5, 9], 
             [5, 9, 7, 8, 3, 6, 4, 1, 2]]))
    
    def test_Hard(self):
        self.assertEqual(sudokusolver.SudokuSolver(sudokus.Sudoku4),(
            [[3, 5, 1, 2, 8, 6, 4, 9, 7],
             [4, 9, 2, 1, 5, 7, 6, 3, 8], 
             [7, 8, 6, 9, 3, 4, 5, 1, 2], 
             [2, 7, 5, 4, 6, 9, 1, 8, 3], 
             [9, 3, 8, 5, 2, 1, 7, 6, 4], 
             [6, 1, 4, 8, 7, 3, 2, 5, 9], 
             [8, 2, 9, 6, 4, 5, 3, 7, 1], 
             [1, 6, 3, 7, 9, 2, 8, 4, 5], 
             [5, 4, 7, 3, 1, 8, 9, 2, 6]]))

if __name__ == '__main__':
    unittest.main()
