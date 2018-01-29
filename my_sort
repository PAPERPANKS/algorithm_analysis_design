# import the random module
import random
import time

t0 = time.process_time()
print (t0, "secs atart time")
arr=[]
num = 10000	#values in array

def num_gen():
	i=1
	for i in range(num):
		val = random.randint(i,num)
		arr.append(val)
	i=0
	for i in range(num):
		print(arr[i])  
		
def bubbleSort(new_arr):
    for i in range(num):
        for j in range(0, num-i-1):
            if new_arr[j] > new_arr[j+1] :
                new_arr[j], new_arr[j+1] = new_arr[j+1], new_arr[j]
                
def selectionsort(new_arr):
	for i in range(num):
	    min_idx = i
	    for j in range(i+1, len(new_arr)):
	        if new_arr[min_idx] > new_arr[j]:
	            min_idx = j
	    new_arr[i], new_arr[min_idx] = new_arr[min_idx], new_arr[i]
	    
def insertionsort(new_arr):
    for i in range(1, num):
        key = new_arr[i]
        j = i-1
        while j >=0 and key < new_arr[j] :
                new_arr[j+1] = new_arr[j]
                j -= 1
        new_arr[j+1] = key

def merge(new_arr, l, m, r):
    n1 = m - l + 1
    n2 = r- m
    #print(n1,n2)
    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0 , n1):
        L[i] = new_arr[l + i]
 
    for j in range(0 , n2):
        R[j] = new_arr[m + 1 + j]
 
    i = j = 0     
    k = l     
 
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            new_arr[k] = L[i]
            i += 1
        else:
            new_arr[k] = R[j]
            j += 1
        k += 1
 
    while i < n1:
        new_arr[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        new_arr[k] = R[j]
        j += 1
        k += 1
 

def mergeSort(new_arr,l,r):
    if l < r:
        m = int((l+(r-1))/2)
        mergeSort(new_arr, l, m)
        mergeSort(new_arr, m+1, r)
        merge(new_arr, l, m, r)
 
def partition(new_arr,low,high):
    i = ( low-1 )  
    m = int((low+(high-1))/2) #middle pivot
    pivot = new_arr[m]     
 
    for j in range(low , high):
 
        if   new_arr[j] <= pivot:
            i = i+1
            new_arr[i],new_arr[j] = new_arr[j],new_arr[i]
 
    new_arr[i+1],new_arr[high] = new_arr[high],new_arr[i+1]
    return ( i+1 )
 

def quickSort(new_arr,low,high):
    if low < high:
 
        pi = partition(new_arr,low,high)
 
        quickSort(new_arr, low, pi-1)
        quickSort(new_arr, pi+1, high)

def countingsort(new_arr, exp1):
 
    n = len(new_arr)
 
    output = [0] * (n)
 
    count = [0] * (n)
 
    for i in range(0, n):
        index = int(new_arr[i]/exp1)
        count[ (index)%10 ] += 1
 
    for i in range(1,n):
        count[i] += count[i-1]
 
    
    i = n-1
    while i>=0:
        index = int(new_arr[i]/exp1)
        output[ count[ (index)%10 ] - 1] = new_arr[i]
        count[ (index)%10 ] -= 1
        i -= 1
 
    i = 0
    for i in range(0,len(new_arr)):
        new_arr[i] = output[i]
 
def radixsort(new_arr):

    max1 = max(new_arr)
    exp = 1
    while max1/exp > 0:
        countingsort(new_arr,exp)
        exp *= 10
 
# main  
print("1.BUbble Sort 2.Selection Sort 3.Insertion sort 4.Merge Sort 5.Quick Sort 6. Count Sort 7.Radix Sort")

choice = int(input("\nYour Option : "))

print("\nUnsorted Array : ")
num_gen()

if choice == 1:
	bubbleSort(arr)
elif choice == 2:	
	selectionsort(arr)
elif choice == 3:
	insertionsort(arr)
elif choice == 4:
	mergeSort(arr,0,num-1)
elif choice == 5:
	quickSort(arr,0,num-1)
elif choice == 6:
	#arr=[4,7,8,9,9,6,8,8,8,9]
	temp = 10000
	countingsort(arr,temp)
elif choice == 7:
	radixsort(arr)
else:
	print(exit)

print("\nSorted Array : ")
for x in range(num):
	print(arr[x])
t1 = time.process_time()-t0
print (t1, "secs time elapsed")
