"""
Challenge #2:

Given a list of numbers, create a function that returns the list but with each
element's index in the list added to itself. You should add 0 to the number at
index 0, add 1 to the number at index 1, etc.

Examples:
- add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
- add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
- add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]

Notes:
- The input list will only contain integers.
"""


def add_indexes(numbers):
    # Your code here
    new_list = []

    for index, value in enumerate(numbers):
        sum = index + value
        # add value to the new_list
        new_list.append(sum)

    return new_list

my_list = [1, 2, 3, 4, 5]
print(add_indexes(my_list)) # [1, 3, 5, 7, 9]

# print just the indeces in the range
# for item in range(len(my_list)):
#     print(item)

# print all values in the list
# for val in my_list:
#     print(val)

# print both value AND index in a list
# print(list(enumerate(my_list)))

# for item, value in enumerate(my_list):
#     print(item, value)