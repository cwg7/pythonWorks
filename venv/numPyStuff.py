import numpy as np

# TASK: Create a numpy array called myarray which consists of 101 evenly linearly spaced points between 0 and 10.
# MAKE SURE TO READ THE FULL INSTRUCTIONS ABOVE CAREFULLY, AS THE EVALUATION SCRIPT IS VERY STRICT.
# Link to Solution: https://gist.github.com/Pierian-Data/ea9c4d2fc6c98ac74af18134cd924867
# import ?
# myarray = ?


myArray = np.linspace(0,10,101)

#print(myArray)


# TASK: Use numpy to check how many rolls were greater than 2. For example if dice_rolls=[1,2,3] then the answer is 1.
# NOTE: Many different ways to do this! Your final answer should be an integer.
# MAKE SURE TO READ THE FULL INSTRUCTIONS ABOVE CAREFULLY, AS THE EVALUATION SCRIPT IS VERY STRICT.
# Link to Solution: https://gist.github.com/Pierian-Data/ea3121efac5dd3338c280ff10068f9c8


dice_rolls = np.array([3, 1, 5, 2, 5, 1, 1, 5, 1, 4, 2, 1, 4, 5, 3, 4, 5, 2, 4, 2, 6, 6, 3, 6, 2, 3, 5, 6, 5])

bool_arr = dice_rolls > 2
#print(dice_rolls[bool_arr])

total_rolls_over_two = len(dice_rolls[bool_arr])
#print(total_rolls_over_two)


# TASK: Use numpy to check the total remaining in the account after the series of transactions.
# NOTE: Many different ways to do this!
# MAKE SURE TO READ THE FULL INSTRUCTIONS ABOVE CAREFULLY, AS THE EVALUATION SCRIPT IS VERY STRICT.
# Link to Solution: https://gist.github.com/Pierian-Data/225a449484e12e0535fbbac2231b426b

import numpy as np
account_transactions = np.array([100,-200,300,-400,100,100,-230,450,500,2000])

# SOLUTION
account_total = np.sum(account_transactions)
#print(account_total)


#2. Create an array of 10 zeros
arr = np.zeros(10)
#print(arr)

#3. Create an array of 10 ones

arr1 = np.ones(10)
#print(arr1)

# 4. Create an array of 10 fives
arr = np.ones(10) * 5
#print(arr)

# 5. Create an array of the integers from 10 to 50
arr = np.arange(10,51)

# 6. Create an array of all the even integers from 10 to 50

arr = np.arange(10,51,2)
#print(arr)

# 7. Create a 3x3 matrix with values ranging from 0 to 8

#arr = np.arange(0,9)
#solution = arr.reshape(3,3)
arr = np.arange(0,9).reshape(3,3)
#print(arr)

# 8. Create a 3x3 identity matrix

arr = np.eye(3)
#print(arr)

# Use NumPy to generate a random number between 0 and 1
x = np.random.random()
#print(x)

# 10. Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

rand_num = np.random.normal(0,1,25)


# 11. Create the following matrix:
# [0.01 0.02 0.03 0.04 0.05 0.06 0.07 0.08 0.09 0.1  0.11 0.12 0.13 0.14
#  0.15 0.16 0.17 0.18 0.19 0.2  0.21 0.22 0.23 0.24 0.25 0.26 0.27 0.28
#  0.29 0.3  0.31 0.32 0.33 0.34 0.35 0.36 0.37 0.38 0.39 0.4  0.41 0.42
#  0.43 0.44 0.45 0.46 0.47 0.48 0.49 0.5  0.51 0.52 0.53 0.54 0.55 0.56
#  0.57 0.58 0.59 0.6  0.61 0.62 0.63 0.64 0.65 0.66 0.67 0.68 0.69 0.7
#  0.71 0.72 0.73 0.74 0.75 0.76 0.77 0.78 0.79 0.8  0.81 0.82 0.83 0.84
#  0.85 0.86 0.87 0.88 0.89 0.9  0.91 0.92 0.93 0.94 0.95 0.96 0.97 0.98
#  0.99 1.  ]

arr = np.arange(.01,1.01,.01)
#print(arr)


# 12. Create an array of 20 linearly spaced points between 0 and 1:

myArray = np.linspace(0,1,20)
#print(myArray)

mat = np.arange(1,26).reshape(5,5)
# grabbing selected values of matrix below

# print(mat)
# print("\n")
#
# #get rows 3-5
#
# mod = mat[2:]
# print(mod)
#
# print("\n")
#
# #get the last 4 numbers of the selected rows
# newMod = mat[2:,1:]
# print(newMod)
#
# mat = np.arange(1,26).reshape(5,5)
# mat = mat[:3,1]
# print(mat)

# Get sum of all values in matrix
sum = np.sum(mat)
#print(sum)

# Get standard deviation of all values in mat
stdev = np.std(mat)
#print(stdev)

# Get the sum of all columns in mat

sumCol = mat.sum(axis = 0)
#print(sumCol)

# Way to ensure how to get same random number
way = np.random.seed(101)
sameRandom = np.random.rand(1)
#print(sameRandom)

