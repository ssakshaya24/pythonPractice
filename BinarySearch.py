n=[]
ans=-1

 
length=int(input('Enter length: '))
print('Enter the elements: ')

for i in range(length):
              n.append(int(input()))   
ele= int(input("Enter the element to be searched for: "))
low=0
high=length-1
while(low<=high):
    mid=(low+high)//2

    if(int(n[mid])==ele):
        ans=mid
        break
    elif(ele>int(n[mid])):
        low=mid+1
    else:
        high=mid-1

print(ans)
