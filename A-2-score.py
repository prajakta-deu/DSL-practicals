marks = []
total = int(input("Total number of students are:\t"))

# Input marks
def marksInput():
    print("\n----------\nNOTE: PLEASE ENTER MARKS OUT OF 50. ENTER '-1' FOR ABSENT STUDENTS.\n----------\n")
    for i in range(total):
        enterMarks = int(input(f"Enter marks for student {i+1}:\t"))
        marks.append(enterMarks)
    print(f"\n-----\nMarks of {total} students are:\t{marks}\n-----")

# Option 1 = Average score
def average_marks():
    marks_withoutAbsent = []
    for i in marks:
        if (i >= 0):
            marks_withoutAbsent.append(i)
        else:
            continue
    average_calc = sum(marks_withoutAbsent) / total
    print(f"\n------\nAverage score of {total} students is:\t{average_calc}\n-----")

# Option 2 = High and low marks
def high_low():
    maxi = marks[0] # Initialise maxi with the first element of the marks list
    mini = marks[0] # Initialise mini with the first element of the marks list
    for i in range(len(marks)):
        if (maxi < marks[i] and marks[i] > -1):
            maxi = marks[i]
    for j in range(len(marks)):
        if (mini > marks[j] and marks[j] > -1):
            mini = marks[j]
    print(f"\n-----\nHighest score is:\t{maxi}\nLowest score is:\t{mini}\n-----")

# Option 3 = Absent count
def absent():
    absent_count = 0;
    for i in marks:
        if (i < 0):
            absent_count+=1
        else:
            continue
    print(f"\n-----\nTotal absent students are:\t{absent_count}\n-----")

# Option 4 = Highest frequency
def high_freq():
    freq_count = 0 # Initialise frequency counter
    for i in range(len(marks)): # Iterate through marks list using i
        if (marks[i] >= 0): # Only consider non-negative marks (since -1 is absent)
            temp_count = 0 # Initialise temporary counter
            for j in range(len(marks)): # Iterate through marks list using j again
                if (marks[i] == marks[j]):
                    temp_count+=1
                    if (freq_count < temp_count): # If temp_count is greater than freq_count value, then
                        freq_count = temp_count # Make freq_count equal to temp_count
    print(f"\n-----\nHighest frequency is:\t{freq_count}\n-----")


marksInput()
average_marks() 
high_low()
absent()
high_freq()
