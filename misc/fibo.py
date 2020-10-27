# 計算量膨大 O(2**n)くらい
def bad_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return bad_fibo(n-1) + bad_fibo(n-2)


# メモ化を使う
def fibo(n, memo):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # メモをチェック
    if memo[n] != -1:
        return memo[n]
    else:
        memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
        return memo[n]


if __name__ == "__main__":
    # N項目を表示する
    N = int(input())

    memo = [-1] * (N+1)
    print(fibo(N, memo))

    # print(bad_fibo(N), end=' ')
