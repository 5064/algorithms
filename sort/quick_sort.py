def quick_sort(list_):
    if len(list_) < 2:
        return list_

    pivot = list_[0]
    rest = list_[1:]
    smaller = [x for x in rest if x < pivot]
    larger = [x for x in rest if x >= pivot]

    return quick_sort(smaller) + [pivot] + quick_sort(larger)


if __name__ == "__main__":
    list_ = [1, 3, 5, 4, 2, 9, 8, 7, 6]
    print(quick_sort(list_))
