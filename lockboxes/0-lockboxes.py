#!/usr/bin/python3
"""an algrathem for unlocking boxes"""


def canUnlockAll(boxes):
    """Determines if all boxes can be opened."""
    n = len(boxes)
    unlocked = set()  # To track unlocked boxes
    unlocked.add(0)   # Box 0 is initially unlocked
    stack = [0]       # Stack for DFS (start with box 0)

    while stack:
        current_box = stack.pop()  # Take a box to process
        for key in boxes[current_box]:
            if key not in unlocked and 0 <= key < n:
                unlocked.add(key)
                stack.append(key)  # Add new box to explore

    # If the number of unlocked boxes equals total boxes, return True
    return len(unlocked) == n
