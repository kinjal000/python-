def greedy_coin_change(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        count += amount // coin
        amount %= coin
    return count

coins = [1, 5, 10, 25]
amount = 63
print("Minimum coins needed:", greedy_coin_change(coins, amount))























# Explanation: The greedy approach selects the largest coin possible at each step