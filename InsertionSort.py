#InsertionSort

a=[]
n=int(input('Enter the length of the array: '))
for i in range(n):
    a.append(int(input('Enter the element: ')))

for i in range(1,n):
                for j in range(i-1,-1,-1):
                     if a[j]>a[j+1]:
                         a[j],a[j+1]=a[j+1],a[j]
                     else:
                         break
print(a)
