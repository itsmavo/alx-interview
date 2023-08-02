#!/usr/bin/python3
''' Working with lockboxes. '''

def canUnlockAll(boxes):
    ''' Checks all boxes in a list containing keys
    to other boxes can unlock if the first box is unlocked.'''
    n = len(boxes)
    seen = set([0])
    unseen = set(boxes[0]).difference(set([0]))
    while len(unseen) > 0:
        box_idx = unseen.pop()
        if not box_idx or box_idx >= n or box_idx < 0:
            continue
        if box_idx not in seen:
            unseen = unseen.union(boxes[box_idx])
            seen.add(box_idx)
    return n == len(seen)
