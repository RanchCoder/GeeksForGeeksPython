#ask for number of elements in the array from the user

n = int(input('No of elements : '))

#ask for number of rotation in clockwise direction from the user

d = int(input('No of rotation : '))
arr = []


#take input for the array elements
for i in range(0,n):
    print('element ', i , ' :')
    arr.append(int(input()))

print(arr)
#now for rotation we will using nesting of loops concept
for i in range(0,d):
    temp = arr[len(arr)-1]
    for j in range(0,n):
        arr[len(arr)-(j+1)] = arr[len(arr) - (j+2)]
    arr[0] = temp
    print('array after rotation no : ',i + 1 ,' ',arr)
print('Final array : ' , arr)        
        

    


