from typing import List
from typing import Annotated
from math import sqrt

Vector = List[float]

def merge(vec:Vector) -> int:
    """
    Merge index values into a single one
    """

    result = 0
    x = None
    y = None

    cycle = 0
    while cycle < len(vec):

        if x == None:
            x = vec[cycle]
            cycle = cycle + 1

        if cycle >= len(vec):
            y = 0
        
        if y == None:
            y = vec[cycle]
        
        if x is not None:
            result = result + x + y
            x = None
            y = None

        cycle = cycle + 1

    return result


def sum(x:Vector, y:Vector) -> Vector:
    """
    Sum 2 Vectors.
    NOTE: both vectors SHOULD to have the same length
    """

    assert len(x) == len(y), "Vector sizes are not equal!"

    newVector:Vector = []

    cycle = 0

    for pairs in x:
        newVector.append(x[cycle] + y[cycle])
        cycle = cycle + 1

    return newVector

def subtract(x:Vector, y:Vector) -> Vector:
    """
    Subtract 2 Vectors.
    NOTE: both vectors SHOULD to have the same length
    """

    assert len(x) == len(y), "Vector sizes are not equal!"
    newVector:Vector = []

    cycle = 0
    for element in x:
        newVector.append(x[cycle] - y[cycle])
        cycle = cycle + 1

    return newVector


def assertSizes(vec:List[Vector]):
    """
    Check's the sizes of each element and compares it
    with element 0.
    """
    vecSizes:List[int] = []

    for element in vec:
        vecSizes.append(len(element))
    
    cycle = 0
    for element in vecSizes:
        assert element == vecSizes[0], "The element %s is bigger than element 0!" %cycle
        cycle = cycle + 1


def sumVectorElements(vec:List[Vector]) -> Vector:
    """
    Sum's vector elements always syncronizing the elements indexes of each vector.
    [[1,2],[3,4]] = [4,6]
    """
    
    assertSizes(vec)
    newVector:Vector = []

    cycle1:int = 0
    for listElement in vec[0]:

        vectorToSum = []

        cycle2:int = 0
        for vectorsElement in vec:
            
            vectorToSum.append(vec[cycle2][cycle1])

            cycle2 = cycle2 + 1

        newVector.append(merge(vectorToSum))

        cycle1 = cycle1 + 1

    return newVector



def scalar(n:int, vec:Vector) -> Vector:
    """
    Multiplies each vec element by N.
    scalar(n,v) = v[n * index]  
    """

    resultVector = [] 
    for vecElement in vec:
        resultVector.append(vecElement * n)
    
    return resultVector

def mean(vecList:List[Vector]) -> Vector:
    return scalar(1/len(vecList),sumVectorElements(vecList))


def scalarProduct(x:Vector, y:Vector) -> float:
    """Return's the product of X * Y
    [1,2,3] * [4,5,6] = 32
    """
    assertSizes([x,y])
  
    product = []

    cycle:int = 0
    while len(x) > cycle:    
        product.append(x[cycle] * y[cycle])
        cycle = cycle + 1
    
    return merge(product) 

def sumOfSquares(vec:Vector) -> float:
    return scalarProduct(vec, vec)

def magnitude(vec:Vector) -> float:
    """
    The square root of a entire vector 
    """
    return sqrt(sumOfSquares(vec))

def distance(x:Vector, y:Vector) -> float:
    return magnitude(subtract(x,y))
