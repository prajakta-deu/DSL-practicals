# Function for quick sort:
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

# Function for displaying top scores:
def top5(arr):
    sorted_arr = quicksort(arr)
    top_scores = sorted_arr[-5:][::-1]
    return top_scores

# Defining main function:
def main():
    total=int(input("Total number of students are:\t"))
    percent=[]
    for i in range(total):
        percent_in=float(input(f"Enter percentage for student {i+1}:\t"))
        percent.append(percent_in)
    print(f"\nPercentages of students are:\t {percent}")
    print(f"\n------------------\nSorted marks (using quick sort algorithm):\t{quicksort(percent)}\n------------------")
    print(f"\n------------------\nTop five scores are:\t{top5(percent)}\n------------------\n")

# Calling main function:
main()
