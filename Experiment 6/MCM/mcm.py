def matrix_chain_multiplication(N, arr):
    dp = [[0 for _ in range(N)] for _ in range(N)]

    for L in range(2, N):
        for i in range(1, N - L + 1):
            j = i + L - 1
            dp[i][j] = float('inf')
            
            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                dp[i][j] = min(dp[i][j], q)
    
    return dp[1][N - 1]

def tests():
    test_cases = [
        [7, 3, 7, 4, 7, 5, 7, 6],
        [7, 5, 7, 6, 7, 7, 7, 8],
        [7, 4, 7, 8, 7, 3, 7, 9],
        [7, 2, 7, 10, 7, 4, 7, 5],
        [7, 6, 7, 3, 7, 8, 7, 2],
        [7, 9, 7, 5, 7, 10, 7, 3],
        [7, 7, 7, 8, 7, 6, 7, 4],
        [7, 10, 7, 3, 7, 9, 7, 5],
        [7, 8, 7, 2, 7, 6, 7, 4],
        [7, 4, 7, 10, 7, 5, 7, 6]
    ]
    for tc in test_cases:
        print(matrix_chain_multiplication(len(tc), tc))
    
tests()

