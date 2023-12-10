str1 = input("Enter string: ")
substr1 = input("Enter substring: ")
occur2 = str1.split()
index1 = []
for i in occur2:
    for j in occur2:
        if(i == j and j not in index1):
            index1.append(i)
        else:
            continue

def longestWord():
    globalMax = 0
    currentMax = 0
    list1 = []
    for i in str1:
        if (i != " "):
            currentMax = currentMax + 1
            list1.append(i)
        else:
            if (currentMax > globalMax):
                globalMax = currentMax
                temp = list1
            currentMax = 0
            list1 = []
        if (i == str1[len(str1) - 1]):
            if (currentMax > globalMax):
                globalMax = currentMax
                temp = list1
    print("Longest word is: ", "".join(temp))
    print("Length of largest word is: ", globalMax)


def palindrome():
    rev1 = str1
    if (str1[::-1] == rev1):
        print("String is palindrome")
    else:
        print("String is not palindrome")


def charfrequency():
    temp = 0
    for i in str1:
        max1 = 0
        for j in range(0, len(str1)):
            if (str1[j] != " " and str1[j] == occur1):
                max1 = max1 + 1
            else:
                continue
        if (max1 > temp):
            temp = max1
        else:
            continue
    print("Number of times the character '", occur1, "' occurs: ", temp)


def indexSubstring():
    for i in range(len(str1) - len(substr1) + 1):
        if str1[i:i + len(substr1)] == substr1:
            print("Substring present in string at index: ", i)
            break
    else:
        print('Substring not present')

def occurWord():
    for i in index1:
        max1 = 0
        for j in occur2:
            if(i == j):
                max1 = max1 + 1
            else:
                continue
        print("The number of times '",i,"' is repeated is: ",max1)

longestWord()
occur1 = input("Enter character whose occurence is to be calculated: "
charfrequency()
palindrome()
indexSubstring()
occurWord()
