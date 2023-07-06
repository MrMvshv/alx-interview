#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Return True if all boxes can be opened, else return False
    """
    num_boxes = len(boxes)  # Total number of boxes
    visited = [False] * num_boxes  # Track visited boxes
    visited[0] = True  # Mark the first box as visited
    queue = [0]  # Start BFS from the first box

    front = 0  # Pointer to the front of the queue
    rear = 1  # Pointer to the rear of the queue

    while front < rear:
        box = queue[front]
        front += 1

        for key in boxes[box]:
            if key >= 0 and key < num_boxes and not visited[key]:
                visited[key] = True
                queue.append(key)
                rear += 1

    return all(visited)
