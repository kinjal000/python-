def dp_coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1, 5, 10, 25]
amount = 63
print("Minimum coins needed:", dp_coin_change(coins, amount))


























# Explanation: This dynamic programming solution fills an array where each entry
# represents the minimum number of coins needed to make that amount.