def count_staircase_ways(N: int, X: list[int]) -> int:
    """
    Calculates the number of unique ways to climb a staircase of N steps,
    where you can climb any number of steps at a time specified in the set X.

    This problem is solved using dynamic programming.
    Let dp[i] be the number of unique ways to reach step i.

    The recurrence relation is:
    dp[i] = sum(dp[i - x] for x in X if i - x >= 0)

    Args:
        N: The total number of steps in the staircase (a positive integer).
        X: A list of allowed positive integer step sizes (e.g., [1, 2] or [1, 3, 5]).

    Returns:
        The total number of unique ways to reach the Nth step.
    """
    if N < 0:
        # Cannot climb a negative number of steps
        return 0
    if not X:
        # If no steps are allowed, only N=0 is possible
        return 1 if N == 0 else 0

    # dp[i] stores the number of ways to reach step i.
    # We need a size of N + 1 for indices 0 through N.
    dp = [0] * (N + 1)

    # Base case: There is exactly one way to be at step 0 (do nothing).
    dp[0] = 1

    # Iterate from step 1 up to N
    for i in range(1, N + 1):
        # The number of ways to reach step i is the sum of ways to reach all 
        # steps (i - x) from which we can take an allowed step 'x' to reach i.
        for step_size in X:
            # Check if the previous step (i - step_size) is valid (i.e., not negative)
            prev_step = i - step_size
            if prev_step >= 0:
                dp[i] += dp[prev_step]

    # The result is the number of ways to reach the Nth step.
    return dp[N]

# --- Examples ---

# Problem 1: N=4, X={1, 2}
N1 = 4
X1 = [1, 2]
ways1 = count_staircase_ways(N1, X1)
print(f"Case 1: N={N1}, X={X1}")
print(f"Number of unique ways: {ways1}")
# Expected output: 5

# Problem 2: N=10, X={1, 3, 5}
N2 = 10
X2 = [1, 3, 5]
ways2 = count_staircase_ways(N2, X2)
print(f"\nCase 2: N={N2}, X={X2}")
print(f"Number of unique ways: {ways2}")
# Expected output: 49 (Ways to reach 10 using steps of 1, 3, or 5)

# Problem 3: A basic check (Fibonacci sequence)
N3 = 7
X3 = [1, 2]
ways3 = count_staircase_ways(N3, X3)
print(f"\nCase 3: N={N3}, X={X3}")
print(f"Number of unique ways: {ways3}")
# Expected output: 21 (Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21)

# Problem 4: A single large step
N4 = 5
X4 = [5]
ways4 = count_staircase_ways(N4, X4)
print(f"\nCase 4: N={N4}, X={X4}")
print(f"Number of unique ways: {ways4}")
# Expected output: 1

