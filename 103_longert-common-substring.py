def longest_common_substring(str1, str2):
    max_len = 0
    end = 0
    dp = [[0] * (len(str2) + 1) for i in range(len(str1) + 1)]
    
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end = i
    return str1[end - max_len:end]

print("Longest common substring:", longest_common_substring("abcdef", "zcdemf"))

















# Explanation: Uses dynamic programming to find the longest common substring