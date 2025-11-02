'''
Write a function which calculates the average of the numbers in a given array.

Note: Empty arrays should return 0.

level 8kyu

'''

def find_average(numbers):
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return  0