#Solving a code challenge from HackeRank
def Median(n,arr):
    arr.sort()
    # print(arr)
    l = len(arr)
    middle = int(l/2)
    a =arr[middle]
    b =  arr[middle +1]
    if( l % 2 != 0):
        med = arr[middle]
        print(med)
        return med
    else:
        med = ( a + b ) /2
        print(med)
        return med




Median(7,[1,2,3,4,5,6,7,8])