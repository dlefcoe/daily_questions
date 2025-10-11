def find_missing_number(arr):
    """
    Finds the missing number in an unsorted list of numbers 
    that should range from 1 to N, where N is one more than 
    the length of the list.

    Args:
        arr (list): An unsorted list of numbers with one number missing.

    Returns:
        int: The missing number.
    """
    
    # The list contains numbers from 1 to N, so if one is missing, 
    # the maximum potential number (N) is the length of the list + 1.
    n = len(arr) + 1
    
    # 1. Calculate the expected sum of all numbers from 1 to N 
    # using the formula for the sum of an arithmetic series: S = n * (n + 1) / 2
    expected_sum = (n * (n + 1)) // 2  # Use integer division
    
    # 2. Calculate the actual sum of the numbers in the input list
    actual_sum = sum(arr)
    
    # 3. The missing number is the difference between the expected sum 
    # and the actual sum.
    missing_number = expected_sum - actual_sum
    
    return missing_number

# --- Example Usage (from the prompt) ---

# Example 1: Missing number is 11
example_list_1 = [2, 5, 1, 4, 9, 6, 3, 7, 10, 8]
# The list length is 10, so N is 11.
# Expected sum (1 to 11): 11 * 12 / 2 = 66
# Actual sum: 2 + 5 + ... + 8 = 55
# Missing number: 66 - 55 = 11
missing_1 = find_missing_number(example_list_1)
print('example 1:')
print(f"Input: {example_list_1}")
print(f"Missing number: {missing_1}\n") # Output: Missing number: 11

# --- Usage for the main scenario (1 to 100) ---

# Create a list from 1 to 100 with a number (e.g., 57) intentionally removed
# to demonstrate the function's capability for the full problem.
original_list = list(range(1, 101))
missing_number_to_test = 57
test_list = [x for x in original_list if x != missing_number_to_test]
# The 'test_list' now has 99 numbers, ranging from 1 to 100, with 57 missing.

missing_2 = find_missing_number(test_list)
print('example 2:')
print(f"List length: {len(test_list)} (N=100)")
print(f"Missing number (1 to 100): {missing_2}") # Output: Missing number (1 to 100): 57


