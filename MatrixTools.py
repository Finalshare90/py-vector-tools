from typing import List, Callable
import VectorTools as vt

Matrix = List[List[float]]

def shape(M:Matrix):
    
    vt.assertSizes(M)

    rows = len(M)
    collumns = len(M[0])
    
    return rows, collumns 

def getRow(M:Matrix, r:int):
    return M[r]

def getColumn(A: Matrix, j: int) -> vt.Vector:
    
    columnValues = []

    cycle = 0
    while cycle < len(A):
        columnValues.append(A[cycle][j])

        cycle += 1

    return columnValues

def newMatrix(rows:int, collumns:int,
              genFn: Callable[[int,int,Matrix],Matrix]) -> Matrix:

    """
    Creates a new matrix using genFn, if genFn = none, creates a blank
    matrix of Rows x Collumns zeros.
    """

    matrix:Matrix = []

    collumnsCycle = 0
    while collumnsCycle < collumns:

        matrix.append([])

        rowCycle = 0
        while rowCycle < rows:

            matrix[collumnsCycle].append(0)

            rowCycle += 1;

        collumnsCycle += 1

    if genFn is not None:

        blankMatrix = matrix

        matrix = genFn(rows,collumns, blankMatrix)

    return matrix
