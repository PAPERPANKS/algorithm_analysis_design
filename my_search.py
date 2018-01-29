# import the random module
import random
import time

t0 = time.process_time()
print (t0, "secs atart time")
arr=[]
num = 100000
def num_gen():
	for i in range(num):
		x = random.randint(i,num)
		arr.append(x)
	for i in range(num):
		print(arr[i])  

def lin_srch(x):
	found = False
  
	for i in range(num):
		if(arr[i]==x):
			print("value present at location : ", i)
			found = True
			break
	if (found == False):
		print("Not found")

def bin_srch(new_arr, l, r, x):
	if r >= l:
		mid = int(l + (r - l)/2)
		#print (mid)
		if new_arr[mid] == x:
			#print("found")
			return mid
		elif new_arr[mid] > x:
			return bin_srch(new_arr, l, mid-1, x)
		else:
			return bin_srch(new_arr, mid+1, r, x)
	else:
		return -1
# main  
print("1.Linear search 2.Binary Seacrh")
choice = int(input("Your Option"))
num_gen()
val = int(input("Enter Value : "))

if choice == 1:
	lin_srch(val)

elif choice == 2:
	#print(val)
	arr.sort()
	result = bin_srch(arr, 0, num-1, val)
	print(result)
	if result != -1:
		print("Value present at location", result)
	else:
		print("Not Found")

t1 = time.process_time()-t0
print (t1, "time elapsed")
