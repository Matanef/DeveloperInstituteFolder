import numpy as np

zero = np.zeros(10)
print(zero)
# ---------------------------------------------------------------
zeroOne = np.zeros(10)
zeroOne[4] = 1
print(zeroOne)
# ---------------------------------------------------------------
rangeOne = np.arange(10, 49)
print(rangeOne)
# ---------------------------------------------------------------
rangeOneReverse = np.arange(10, 49)
print(rangeOne[::-1])

# ---------------------------------------------------------------
rangeTwo = range(9)
rangeTwoArr = np.array(rangeTwo)
rangeTwoArr = rangeTwoArr.reshape((3,3))
print(rangeTwoArr, '\n')
print(rangeTwo)
# ---------------------------------------------------------------
rangeTwoSecond = np.arange(9).reshape((3, 3))
print(rangeTwoSecond)
print('Array of 9', rangeTwoArr, '\n')
# ---------------------------------------------------------------
nonZero =  [1,2,0,0,4,0]
nonZeroNew = np.array(nonZero)
print('line 29', nonZeroNew)
print('\n')
nonZeroFinal = np.nonzero(nonZeroNew)
print(nonZeroFinal)
# ---------------------------------------------------------------
nonZeroSecond = np.nonzero(np.array([1,2,0,0,4,0]))
print(nonZeroSecond)
# ---------------------------------------------------------------
print('\n')
diag = np.eye(3, dtype=int)
print('diag', diag)
# ---------------------------------------------------------------
matrix = np.random.random((3,3,3))
print(matrix)
# ---------------------------------------------------------------
matrixTen = np.random.random((10,10))
matrixTenMin = np.amin(matrixTen)
matrixTenMax = np.amax(matrixTen)
print(matrixTen)
print('\n')
print('Min Value:', matrixTenMin)
print('\n')
print('Max Value: ', matrixTenMax)
print('\n')
# ---------------------------------------------------------------
vectorThirt = np.random.random((30))
print(vectorThirt)
print('\n')
vectorThirtMean = np.mean(vectorThirt)
print('Mean Value:' , vectorThirtMean)
print('\n')
# ---------------------------------------------------------------
twoDArray = np.ones((9,9))
print("original to check how it looks like")
print(twoDArray)
print('\n')
twoDArray[1:-1,1:-1] = 0
print("with Zeros")
print(twoDArray)
print('\n')
# ---------------------------------------------------------------

def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 0)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value
    
twoDArrayFin = np.pad(twoDArray, 1, pad_with)
print(twoDArrayFin)




x = np.pad(twoDArray, pad_width=2, mode='constant', constant_values=0)
print('\n')
print(x)
# ---------------------------------------------------------------
'''python
0 * np.nan = Exepected output = error since we will be unable to multiply a NaN
result = nan

np.nan == np.nan = Exepected output = False since they are place holders and do not equalt to each other 
result = False

np.inf > np.nan = Exepected output True, since Infinity supposed to be larger the nan
result: False (so i don't understand)

np.nan - np.nan = Exepected output: thought that 0 but it's not possible since this is a nan so, nan?
results = nan

0.3 == 3 * 0.1 = Exepected output 
'''
print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(0.3 == 3 * 0.1)

# ---------------------------------------------------------------


diagFive = np.arange(25).reshape(5,5)

print('\n')
print(diagFive)
print('\n')

print("np.diag(diagFive)", '\n')
print(np.diag(diagFive))
print('\n')

diagFiveFine = np.diag(np.diag(diagFive))
print(diagFiveFine)

# wasn't able to switch the numbers in the diagonal.

g = np.diag([1,2,3,4,7])
print('\n')
print(g)

gLess = np.diag([1,2,3,4,7], -1)
print('\n')
print(gLess)

checkM = np.ones((2,3))
print(checkM)
print('\n')
checkM = np.zeros((8,8),dtype=int)
print(checkM)

# Creating the Array
a = np.arange(25).reshape(5,5)
print(a, '\n')

# Extracting diag values from the array and presenting them
print("Performing Diag on array [a] to extract values to a new Array", '\n')
print(np.diagonal(a), '\n')

# crating a new Array of zeros with the diag values we extracted as a diagonal in this array
b = np.diag(np.diagonal(a))
print("Using the array we created with diag values as a diagonal ")
print(b, '\n')

# substracting values of A from B
a = a-b
print(a, '\n')

# creating a new array with the desired values
c= np.diag([1,2,3,4,7])
print("this is c", '\n')
print(c)
# ---------------------------------------------------------------

# x = np.ones((2,2))
# print(x)
print("Checkerboard pattern:")
x = np.zeros((8,8),dtype=int)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)

# ---------------------------------------------------------------

# ravel = np.unravel_index([22, 41, 37], (7,6))
# print(ravel)

# ---------------------------------------------------------------

# testArray = np.ones((2,2))
print('Tile')
x = np.zeros((2,2),dtype=int)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(np.tile(x, (4,4)))

# ---------------------------------------------------------------

matrixFive = np.random.random((5,5))
print(matrixFive)
xmax, xmin = matrixFive.max(), matrixFive.min()
normMatrix = (matrixFive - xmin)/(xmax - xmin)
print("After normalization:")
print(normMatrix)

# ---------------------------------------------------------------

twoByFour = np.arange(1,9).reshape((2,4))
print('twobyfour')
print(twoByFour)
print('\n')
newTwoByFour = np.dtype([('dtype', np.int16)])
print('newTwoByFour')
print(newTwoByFour)
print('\n')

# ---------------------------------------------------------------

matrixFivebythree = np.random.random((5,3))*10
matrixThreeByTwo = np.random.random((3,2))*10
print('matrixFivebythree')
print(matrixFivebythree)
print('\n')
print('matrixThreeByTwo')
print(matrixThreeByTwo)
print('\n')

print('Multiplication of 5x3 by 3x2')
print(np.dot(matrixFivebythree,matrixThreeByTwo))
print('\n')

# ---------------------------------------------------------------
negate = np.arange(11)
print(negate)

negateNew = np.negative(negate)
print(negateNew)

negate[(3 < negate) & (negate <= 8)] *= -1
print(negate)

# ---------------------------------------------------------------

