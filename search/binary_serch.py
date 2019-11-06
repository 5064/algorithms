# left と right の初期値の定め方に注意する
# 条件判定を変えても探索の実装は不変
from math import floor, ceil


def isOK(list_, index, key):
    return True if list_[index] >= key else False


def binary_search(sorted_list, key):
    ng = -1  # index = 0 が条件を満たすこともあるので-1
    ok = len(sorted_list)  # index = len(list)-1 が条件を満たさないこともあるので

    while(abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if isOK(sorted_list, mid, key):
            ok = mid
        else:
            ng = mid
    return ok


if __name__ == "__main__":
    L = [1, 2, 4, 8, 16, 32]
    print(binary_search(sorted_list=L, key=int(input())))
