def get_student_list(game):
    lst = []
    n = int(input(f"Enter Number of Students Playing {game} :"))
    for i in range(n):
        roll_no = int(input(f"Enter roll no.({i+1}):"))
        lst.append(roll_no)
    print(f"{game} players are : ", lst)
    return lst

def union(x, y):
    unionist = x + y
    for i in x:
        if i in y:
            unionist.remove(i)
    return unionist

def intersection(x, y):
    inter_list = []
    for i in x:
        if i in y:
            inter_list.append(i)
    return inter_list


def list_difference(list_a, list_b):
    result = []
    for i in list_a:
        if i not in list_b:
            result.append(i)
    return result

def display_lists():
    print("Cricket :", group_a)
    print("Badminton :", group_b)
    print("Football :", group_c)

total_students = int(input("Enter Total Number of Students :"))
group_a = get_student_list("Cricket")
group_b = get_student_list("Badminton")
group_c = get_student_list("Football")



print("1.Display Players lists")
display_lists()
    
print("2.List of Student playing both cricket and badminton")
a=intersection(group_a, group_b)
print(a)
    
print("3.List of Student playing either cricket or badminton but not both")
b=list_difference(union(group_a, group_b), intersection(group_a, group_b))
print(b)

print("4.Number of students who play neither cricket nor badminton")
c=total_students - len(union(group_a, group_b))
print(c)
    
print("5.Number of students who play cricket and football but not badminton")
d=list_difference(union(group_a, group_c), group_b)
print(d)   
