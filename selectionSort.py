a=[]
length=int(input("Enter the length of the list: "))
for i in range(length):
    a.append(int(input("Enter array elements : ")))
for i in range(length-1):
    min_index=i
    for j in range(i+1,length):
        if a[j]<a[min_index]:
            min_index=j

    a[min_index],a[i]=a[i],a[min_index]
print("Sorted list is as follows: ")
print(a)
