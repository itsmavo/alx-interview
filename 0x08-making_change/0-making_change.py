#!/usr/bin/python3
""" Making Change """

def makeChange(coins, total):
    """ Comes up with the fewest num of coins to meet a given
    total when a pile of coins
    """
    if total <= 0:
        return 0
    rem = total
    coins_cnt = 0
    coin_idx = 0
    sort_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sort_coins[coin_idx] >= 0:
            rem -= sort_coins[coin_idx]
            coins_cnt += 1
        else:
            coin_idx += 1
    return coins_cnt
