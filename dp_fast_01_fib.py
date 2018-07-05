def fib(n):
    if n < n:
        return n
    cache = [-1] * (n + 1)
    cache[0] = 0
    cache[1] = 1
    return helper(n, cache)
def helper(n, cache):
    if cache[n] >= 0:
        return cache[n]
    cache[n] = helper(n - 1, cache) + helper(n - 2, cache)
    return cache[n]

def fib2(n):
    cache = [0] * (n + 1)
    cache[1] = 1
    for i in range(2, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[i]

def fib3(n):
    dp0, dp1 = 0, 1
    for i in range(2, n + 1):
        dp0, dp1 = dp1, dp0 + dp1
    return dp1

def makeChange(c):
    if c == 0:
        return 0
    min_coin = float('inf')
    coins = [10, 6, 1]
    for coin in coins:
        if c >= coin:
            cur_min_coin = makeChange(c - coin)
            if cur_min_coin < min_coin:
                min_coin = cur_min_coin
    return min_coin + 1

def makeChange2(c):
    cache = [-1] * (c + 1)
    cache[0] = 0
    return helper2(c, cache)
def helper2(c, cache):
    if cache[c] >= 0:
        return cache[c]
    min_coin = float('inf')
    coins = [10, 6, 1]
    for coin in coins:
        if c >= coin:
            cur_min_coin = helper2(c - coin, cache)
            if cur_min_coin < min_coin:
                min_coin = cur_min_coin
    cache[c] = min_coin + 1
    return cache[c]

def makeChange3(c):
    cache = [0] * (c + 1)
    cache[0] = 0
    for i in range(1, c + 1):
        min_coin = float('inf')
        coins = [10, 6, 1]
        for coin in coins:
            if i >= coin:
                cur_min_coin = cache[i - coin] + 1
                if cur_min_coin < min_coin:
                    min_coin = cur_min_coin
        cache[i] = min_coin
    return cache[c]

# print fib3(15)
print makeChange3(12)