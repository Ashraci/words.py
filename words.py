#ANY7 

def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    for num in nums:
        if num ==7:
            return True
        return False

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

#Convert
def convert_temp(unit_in, unit_out, temp):
       
    if unit_in == "f" and unit_out == "c":
        return (temp - 32) * 5 / 9
    elif unit_in == "c" and unit_out == "f":
        return (temp * 9 / 5) + 32
    elif unit_in == "f" and unit_out == "f":
        return temp
    elif unit_in == "c" and unit_out == "c":
        return temp
    else:
        return f"Invalid unit {unit_in}"

print(convert_temp("c", "f", 0))    # Output: 32.0
print(convert_temp("f", "c", 212))  # Output: 100.0

#Count Up

def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

  
 #IN RANGE

def in_range(nums, lowest, highest):
    """Print numbers inside range.

    Should print:

    20 fits
    30 fits
    """
    for num in nums:
        if num >= lowest and num <= highest:
            print(f"{num} fits")

in_range([10, 20, 30, 40, 50], 15, 30)

#Sum 

def sum_nums(nums):
    """Given list of numbers, return sum of those numbers.

    For example:
      sum_nums([1, 2, 3, 4])

    Should return (not print):
      10
    """  
    total = 0
    for num in nums:
        total += num
    return total

print("sum_nums returned", sum_nums([1, 2, 3, 4]))