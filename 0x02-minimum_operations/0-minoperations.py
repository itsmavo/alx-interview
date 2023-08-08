#!/usr/bin/python3
''' Min operations '''

def minOperations(n):
    ''' Computes the fewest num of operations to get
    n H characters '''
    if not isinstance(n, int):
        return 0
    ops_cnt = 0
    clipboard = 0
    ops_done = 1

    while ops_done < n:
        if clipboard == 0:
            clipboard = ops_done
            ops_done += clipboard
            ops_cnt += 2

        elif n - ops_done > 0 and (n - ops_done) % ops_done == 0:
            clipboard = ops_done
            ops_done += clipboard
            ops_cnt += 2

        elif clipboard > 0:
            ops_done += clipboard
            ops_cnt += 1

    return ops_cnt
