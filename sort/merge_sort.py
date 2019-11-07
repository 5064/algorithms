def merge_sort(list_, left, right):
    if right - left == 1:
        return
    mid = left + (right-left) // 2

    # 左半分 [left, mid) をソート
    merge_sort(list_, left, mid)
    # 右半分 (mid, right] をソート
    merge_sort(list_, mid, right)

    # 左と右のソート結果をコピー（右はリバース）
    buffer = []
    i = left
    while i < mid:
        buffer.append(list_[i])
        i += 1

    i = right - 1
    while i >= mid:
        buffer.append(list_[i])
        i -= 1

    # merge
    iter_left = 0
    iter_right = len(buffer) - 1
    i = left
    while i < right:
        if buffer[iter_left] <= buffer[iter_right]:
            list_[i] = buffer[iter_left]
            iter_left += 1
        else:
            list_[i] = buffer[iter_right]
            iter_right -= 1
        i += 1


if __name__ == "__main__":
    list_ = [8, 2, 5, 9, 3, 6, 1, 4, 7, 0]
    merge_sort(list_, 0, len(list_))
    print(list_)
