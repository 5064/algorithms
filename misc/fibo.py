# nまでのフィボナッチ数列を出力する再帰関数


def recursive_fibo(n, a, b):
    if n < a:
        return
    print(a, end=' ')
    recursive_fibo(n, b, a+b)


if __name__ == "__main__":
    FIRST = 0
    SECOND = 1
    recursive_fibo(int(input()), FIRST, SECOND)
