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
print(total_rolls_over_two)