# Sorting (Selection+Bubble) and Top 5

marks=[]

# Function to enter marks of students
def input_marks():
	students=int(input("Enter the number of students:\t"))
	for i in range(students):
		marks_in=float(input("Enter the Percentage\t"))
		marks.append(marks_in)
	print("\nThe percentage you've entered for ", students, "students are: ", marks, "\n")

# Function for selection sort
def selection():
    for i in range(len(marks)):
        min_index=i
        for j in range(i+1, len(marks)):
            if marks[j] < marks[min_index]:
                min_index=j
        marks[i], marks[min_index] = marks[min_index], marks[i]
    print("Percentage sorted in ascending order using selection sort:\t", marks)
	
def bubble():
    for i in range(len(marks)):
        for j in range(0, len(marks)-i-1):
            if marks[j]>marks[j+1]:
                marks[j], marks[j+1] = marks[j+1], marks[j]
    print("Percentage sorted in ascending order using bubble sort:\t", marks)

def top5():
    for i in range(len(marks)):
        for j in range(0, len(marks)-i-1):
            if marks[j]>marks[j+1]:
                marks[j], marks[j+1] = marks[j+1], marks[j]
    print("Top 5 Percentage using bubble sorting:\t", marks[::-1])


def choose_optn():
	while True:
		print("Choose an option from the menu below:")
		print("1 -> Input Percentage")
		print("2 -> Selection Sorting")
		print("3 -> Bubble Sorting")
		print("4 -> Display top 5")
		print("5 -> Exit")
		optn=int(input("Choose an option (1-5):\t"))
		
		if optn==1:
			input_marks()
		elif optn==2:
			selection()
		elif optn==3:
			bubble()
		elif optn==4:
			top5()
		elif optn==5:
		    quit()
		else:
			print("\nPlease choose a valid option (1-5).\n")
			choose_optn()
choose_optn()
