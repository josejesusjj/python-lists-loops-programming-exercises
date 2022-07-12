arr = [45, 67, 87, 23, 5,  32, 60]
new_list = []
#your code below:
for i in range(0,len(arr), 1):
	new_list.append(arr[len(arr)-1-i])
    
print("initial list:", arr)
print("final list:", new_list)

