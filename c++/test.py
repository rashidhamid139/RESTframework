a = [4,5,6,1,2,3]


def findPivot(A, l, h):
    print(l, h)
    if (l>h):
        return -1
    if (l == h):
        return l
    mid = int((l+h)/2)
    print(mid)
    if (A[l]<A[mid]):
        l=mid+1
    elif A[mid]< A[h]:
        h =  mid
    return findPivot(A, l, h)

print(findPivot(a, 0,5))