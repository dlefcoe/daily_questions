

# wrapper function to check the type of the input
def validate_input(func):
    def wrapper(rows):
        if not isinstance(rows, int):
            print("Input must be an integer.")
            return
        if rows < 1:
            print("Number of rows must be at least 1.")
            return
        return func(rows)
    return wrapper


@validate_input
def print_pyramid(rows:int):
    ''' Print a pyramid of stars with the given number of rows.'''

    # check input value
    if rows < 1:
        print("Number of rows must be at least 1.")
        return
    
    for i in range(1, rows + 1):
        print(' ' * (rows - i), end='')
        print('*' * (2 * i - 1))

# Example usage:
rows = int(input("Enter the number of rows: "))
print_pyramid(rows)
