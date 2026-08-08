class Solution(object):
    def matrixBlockSum(self, mat, k):
        m = len(mat)
        n = len(mat[0])

        # Prefix sum matrix
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    mat[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )

        answer = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # Block boundaries, clipped to matrix
                r1 = max(0, i - k)
                r2 = min(m - 1, i + k)
                c1 = max(0, j - k)
                c2 = min(n - 1, j + k)

                # Rectangle sum using prefix sum
                answer[i][j] = (
                    prefix[r2 + 1][c2 + 1]
                    - prefix[r1][c2 + 1]
                    - prefix[r2 + 1][c1]
                    + prefix[r1][c1]
                )

        return answer