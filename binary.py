
def  search(arr, l, u,n):
    if u>=l:

        mid = l+(u-1)//2
        if arr[mid] == n:
            return mid
        #if element is smaller than mid_value,then it can only present in left subarray
        elif arr[mid] > n :
            return search(arr,l,mid_value-1,n)
        #Else the element can only present in the right subarray
        else:
            return search(arr, mid+1,u,n)
    else:#Element is not present in the array
        return-1



    arr = [1,3,5,7,9,11,14]
    n = 9
    result = search(arr,0,l,len(arr)-1,n)

    if result != -1:
        print("Element is present at index %d" %result)
    else:
        print("element is not present in array")






