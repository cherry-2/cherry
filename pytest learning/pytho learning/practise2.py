# Python Program for n-th Fibonacci number
'''def fibonacci(n):
    if n<0:
        print("incorrect input")
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))'''

'''def sum_of_cubes(n):
    sum=0
    for i in range(1,n+1):
        sum =+ i*i*i
    return sum
print(sum_of_cubes(10))'''


'''def largest(arri, n):
    maxi = arri[0]
    for i in range(1,n):
        if arri[i] > maxi:
            maxi = arri[i]
    return maxi


arri = [10,20,12,8]
n=len(arri)

print(len(arri))
print(largest(arri,n))'''


'''def largest(arr, n):
    # Initialize maximum element
    max = arr[0]

    # Traverse array elements from second
    # and compare every element with 
    # current max
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max


# Driver Code
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array is", Ans)'''


'''def rotateArray(arr, n, d):
    temp = []
    i = 0
    while i < d:
        temp.append(arr[i])
        i = i + 1
    i = 0
    while d < n:
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr


arr = [1,2,3,4,5,6,7,8]

print(rotateArray(arr,8,2)'''


newlist = [12,13,15,16,28,65,98]

size = len(newlist)
temp, tamp = newlist[0], newlist[1]
newlist[0],newlist[1] = newlist[size-1], newlist[size-2]
newlist[size-1], newlist[size-2] = temp, tamp





print (newlist)