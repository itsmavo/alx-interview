#!/usr/bin/python3
""" Prime Game """

def isWinner(x, nums):
    """Determines the winner in 'x' rounds """
    if x < 1 or not nums:
        return None
    mw, bw = 0, 0
    # creating primes with a max limit
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + 1, n + 1, i):
            primes[j - 1] = False
    # filters the num of primes less than n in nums each round
    for _, n in zip(range(x), nums):
        primes_cnt = len(list(filter(lambda x: x, primes[0: n])))
        mw += primes_cnt % 2 == 0
        bw += primes_cnt % 2 == 1
        if mw == bw:
            return None
        return 'Maria' if mw > bw else 'Ben'
