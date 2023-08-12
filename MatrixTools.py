from typing import List
import VectorTools as vt

Matrix = List[List[float]]

def shape(M:Matrix):
    
    vt.assertSizes(M)

    rows = len(M)
    collums = len(M[0])
    
    return rows, collums 