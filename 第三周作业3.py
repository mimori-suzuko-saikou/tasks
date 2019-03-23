def pown(n,m):
    if m == 0:
        return 1
    else:
        return n*pown(n,m-1)

print(pown(2,3))
