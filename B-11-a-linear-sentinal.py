a=[]
no=int(input("Enter the total no of students: "))
print("Enter the roll no of students: ")
for i in range(no):
    a.append(int(input()))

search=int(input("Enter the roll no you want to search:"))
#linear search
def linear(a,search):
    for i in a:
        if i==search:
            return 1
    return -1


#sentinal search
def sentinal(a,search,no):
    end=a[no-1]
    a[no-1]=search
    i=0

    while(a[i]!=search):
        i+=1
    a[no-1]=end
    if(i<no-1) or (search==a[no-1]):
        print("Entered roll no attended the program")
    else:
        print("Entered roll no does not attended the program")

print("1.Linear search")
print("2.Sentinal Search")
ch=int(input("Enter your choice: "))
if ch==1:
    check=linear(a,search)
    if check==-1:
        print("Entered roll no does not attended the program")
    else:
        print("Entered roll no attended the program")
if ch==2:
    sentinal(a,search,no)
