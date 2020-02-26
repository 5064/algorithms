def hanoi(n, f, h, t):
    """
    n : int
        number of disks
    f : str
        from position
    h : str
        helper position
    t : str 
        target position
    """
    if n==0:
        pass
    else:
        hanoi(n-1, f, t, h)
        print('Move disk from {} to {}!'.format(f, t))
        hanoi(n-1, h, f, t)


if __name__ == "__main__":
    hanoi(3, "A", "B", "C")