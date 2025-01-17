def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

weights = [1, 2, 3]
values = [10, 20, 30]
capacity = 3
print("Maximum value:", knapsack(weights, values, capacity))


















# Explanation: The dynamic programming table (dp) tracks the maximum value
# for each weight limit. If the current item's weight fits into the remaining capacity, 
#     we choose between including it or not