# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# k = 12
# l = 0
# r = len(arr) - 1

# while(l < r):
#     if(arr[l]+arr[r] == k):
#         print('Yes',arr[l],arr[r])
#         break
#     elif(arr[l]+arr[r] > k):
#         r -= 1
#     elif(arr[l]+arr[r] < k):
#         l += 1
n = 6
r = n-1
x = 16
arr = [1, 11, 12, 14, 6, 7, 8, 4]
arr.sort()


# def hasArrayTwoCandidates(arr, n, x):
#     arr.sort()
#     l = 0
#     r = n-1
#     while(l < r):
#         if(arr[l] + arr[r] == x):
#             print(arr[l], arr[r])
#             return(True)
#         elif(arr[l]+arr[r] > x):
#             r -= 1
#         elif(arr[l]+arr[r] < x):
#             l += 1
#     return(False)


# print(hasArrayTwoCandidates(arr, 8, 16))


# print(findSum(arr, x, n, l, r))



def swap(arr,p,k):
    temp = arr[p]
    arr[p] = arr[k]
    arr[k] = temp


# import sys
# inputarr = sys.stdin.readlines()



# inputarr = input('input here:')
inputarr = '''4
1 2 3 4
4 2 3 1'''
inputarr = inputarr.split('\n')
thelist = inputarr[1].split(' ')
queue = inputarr[2].split(' ')
moves = 0
for i in range(len(thelist)):
    nextPerson = thelist[i]
    for j in range(len(queue)):
        moves+=1
        if (queue[j] == nextPerson):
            queue.pop(j)
            break

print(moves-1)



# for i in range(len(arr)):
#     indexArr.append(str(i))



# for i in range(len(arr)):
#     max = int(arr[0])
#     j = 0
#     ind = 0
#     for j in range(len(arr)-i):
#         if(max < int(arr[j])):
#             max = int(arr[j])
#             ind = j
#     if(max > int(arr[j])):
#         swap(arr,j,ind)
#         swap(indexArr,j,ind)

# print (' '.join(indexArr))

