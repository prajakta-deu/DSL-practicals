a=[]
no=int(input("Enter the no of students who attended the program:"))
print("Enter the roll no who attended the program:")
for i in range(no):
    a.append(int(input()))
search=int(input("Enter the roll no that you want to search:"))
start=0
end=len(a)-1
n=len(a)

#binary search
def binary(a,search,start,end):
    while start<=end:
        mid=start+(end-start)//2
        if a[mid]==search:
            return mid
        elif a[mid]<search:
            start=mid+1
        else:
            end=mid-1
    return -1

#fibonacci search
def fibonacci(a,n,search):
    offset=-1
    fm2=0
    fm1=1
    fm=fm2+fm1
    while(fm<n):
        fm2=fm1
        fm1=fm
        fm=fm2+fm1
    while(fm>1):
        i=min(offset+fm2,n-1)
        if(a[i]<search):
            fm=fm1
            fm1=fm2
            fm2=fm-fm1
            offset=i
        elif(a[i]>search):
            fm=fm2
            fm1=fm1-fm2
            fm2=fm-fm1
        else:
            return i
    if(fm1==1 and a[offset+1]==search):
        return offset+1
    return -1

print("1.Binary Search")
print("2.Fibonacci Search")
ch=int(input("Enter Your Choice:"))
if ch==1:
    check=binary(a,search,start,end)
    if check== -1:
        print("Entered roll no does not attended the program")
    else:
        print("Entered roll no attended the program")
elif ch==2:
    result=fibonacci(a,n,search)
    if result== -1:
        print("Entered roll no does not attended the program")
    else:
        print("Entered roll no attended the program")

