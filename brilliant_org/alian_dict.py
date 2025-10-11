'''
Alien Dictionary Ordering
Imagine you have a dictionary from an alien language, but the words are sorted like in English.
Your task is to figure out the order of letters in the alien language and write it down as a string.
'''

from collections import defaultdict, deque

def alien_order(words: list[str]) -> str:
    """
    Determines the alien alphabetical order from a list of sorted words.

    The logic involves two main steps:
    1. Graph Construction: Compare adjacent words to find the required letter order (edges).
    2. Topological Sort (Kahn's Algorithm): Use in-degrees and a queue to find the final order.

    Args:
        words: A list of strings sorted according to the alien language rules.

    Returns:
        A string representing the alphabet in the correct order, or an empty string
        if the order is invalid (a cycle exists).
    """
    # 1. Initialization
    # Adjacency list: maps char -> set of chars that must come after it
    adj = defaultdict(set)
    # In-degree map: maps char -> count of chars that must come before it
    in_degree = {}

    # Initialize all unique characters found in the dictionary
    for word in words:
        for char in word:
            if char not in in_degree:
                in_degree[char] = 0

    # 2. Graph Construction: Find constraints (edges)
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i+1]
        min_len = min(len(word1), len(word2))

        # Check for the invalid case: 'abc' followed by 'ab'
        if len(word1) > len(word2) and word1.startswith(word2):
            # This indicates an invalid, contradictory ordering (e.g., 'apple' then 'app')
            return ""

        # Find the first differing character to establish the order
        for j in range(min_len):
            char1 = word1[j]
            char2 = word2[j]

            if char1 != char2:
                # We found the constraint: char1 MUST come before char2
                if char2 not in adj[char1]:
                    # Only add the edge (and update in_degree) once to prevent double counting
                    adj[char1].add(char2)
                    in_degree[char2] += 1
                # Once the first difference is found, we stop comparing this pair.
                break

    # 3. Topological Sort (Kahn's Algorithm)
    queue = deque()
    # Start with all characters that have no dependencies (in_degree of 0)
    for char, degree in in_degree.items():
        if degree == 0:
            queue.append(char)

    result = []
    while queue:
        # Dequeue the current character and add it to the result
        u = queue.popleft()
        result.append(u)

        # For every character 'v' that comes immediately after 'u'...
        for v in adj[u]:
            # ...we have now fulfilled one of 'v's prerequisites, so decrement its in-degree
            in_degree[v] -= 1
            # If 'v' now has no remaining prerequisites, it can be added to the queue
            if in_degree[v] == 0:
                queue.append(v)

    # 4. Cycle Detection (Check for consistency)
    # If the length of the result is less than the total number of unique characters,
    # it means there was a cycle (e.g., a->b and b->a), so the ordering is impossible.
    if len(result) == len(in_degree):
        return "".join(result)
    else:
        # Cycle detected, invalid dictionary
        return ""

# --- Example Usage ---
# Example 1: Basic ordering
words1 = ["wrt", "wrf", "er", "ett", "rftt"]
# Expected order: w -> e, r -> t, t -> f
# Final result: w, e, r, t, f
print(f"Input: {words1}")
print(f"Alien Order: {alien_order(words1)}")

# Example 2: Simple chain
words2 = ["z", "x"]
# Expected order: z -> x
# Final result: z, x
print(f"\nInput: {words2}")
print(f"Alien Order: {alien_order(words2)}")

# Example 3: Cycle detected (invalid)
words_cycle = ["abc", "bca", "cab"] # Should result in a cycle (a->b, b->c, c->a)
print(f"\nInput: {words_cycle}")
print(f"Alien Order: {alien_order(words_cycle)}")

# Example 4: Invalid prefix
words4 = ["apple", "app"]
print(f"\nInput: {words4}")
print(f"Alien Order: {alien_order(words4)}")

# Example 5: Multiple letters with degree 0
words5 = ["a", "b"]
print(f"\nInput: {words5}")
print(f"Alien Order: {alien_order(words5)}")

# Example 6: Multiple letters with degree 0
# TODO this does not look correct.
words6 = ["house", "mum", "mouse"]
print(f"\nInput: {words6}")
print(f"Alien Order: {alien_order(words6)}")

# Example 7: Multiple letters with degree 0 
# TODO this does not look correct.
words7 = ["house", "mouse", "mum"]
print(f"\nInput: {words7}")
print(f"Alien Order: {alien_order(words7)}")



