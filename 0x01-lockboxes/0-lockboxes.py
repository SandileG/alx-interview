#!/usr/bin/python3
"""
Solves lockboxes puzzle
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    :param boxes: A list of lists where each sublist represents a box
                  and contains keys to other boxes.
    :return: True if all boxes can be unlocked, otherwise False.
    """
    if not boxes:
        return False

    n = len(boxes)  # Number of boxes
    opened_boxes = set([0])  # Start with box 0, which is already unlocked
    keys = set(boxes[0])  # Collect the keys in box 0

    # While there are still keys to check
    while keys:
        new_key = keys.pop()  # Take a key from the set of available keys

        # If the key opens a box that has not yet been opened
        if new_key not in opened_boxes and new_key < n:
            opened_boxes.add(new_key)  # Mark the box as opened
            keys.update(boxes[new_key])  # Add the keys found in this new box

    # If the number of opened boxes equals the total number of boxes, return True
    return len(opened_boxes) == n

# Test cases
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Expected output: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Expected output: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Expected output: False
