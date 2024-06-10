#!/usr/bin/python3
'''
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the
other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
'''
from typing import List


def canUnlockAll(boxes: List[list]) -> bool:
    '''A function that checks if all boxes can be unlocked'''
    if not boxes:
        return False
    
    n = len(boxes)
    opened = set()
    keys = [0]
    
    while keys:
        current_key = keys.pop()
        if current_key not in opened:
            opened.add(current_key)
            for key in boxes[current_key]:
                if key not in opened and key < n:
                    keys.append(key)
    
    return len(opened) == n        
