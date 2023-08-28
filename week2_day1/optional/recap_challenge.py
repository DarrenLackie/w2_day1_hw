"""
Exercise 1:
Write a program that takes a list of numbers and prints the sum of all the numbers in the list.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
running_total = 0

for number in numbers:
    running_total += number

print(running_total)


"""
Exercise 2:
Write a program that takes a list of strings and prints the length of each string in the list.
"""

names = ["Darren", "Meaghan", "Maeby"]

for name in names:
    print(len(name))

"""
Exercise 3:
Write a program that prompts the user to enter 5 names and stores them in a list. Then, print the list in alphabetical order.
HINT: Use a range(5) with a for loop to loop 5 times
HINT: To get user input and store it in a variable: name = input("Enter a name: ") 
"""

user_names = []
for _ in range(5):
    name = input("Enter a name: ")
    user_names.append(name)

print(user_names)
"""
Exercise 4:
Write a program that takes a list of numbers and prints the largest and smallest numbers in the list.
HINT: min and max are built-in Python functions
"""

numbers = [2, 5, 2, 17, 88, 42, 16, 1]

print(min(numbers))
print(max(numbers))

"""
Exercise 5:
Write a program that takes a list of integers and prints the average of the numbers in the list.
"""

list_of_integers = [13, 66, 16, 35, 47, 28]
total_of_integers = sum(list_of_integers)
average_of_list = total_of_integers / len(list_of_integers)
average_to_2_decimals = round(average_of_list, 2)

print(average_to_2_decimals)

"""
Exercise 6:
Write a program that takes a list of integers and removes all the duplicates, printing the updated list.
HINT: Python's in-built set function will remove duplicates from a list
"""

numbers = [15, 15, 3, 43, 12, 44, 35, 64, 3]
duplicates_removed_from_list = set(numbers)

print(duplicates_removed_from_list)

"""
Exercise 7:
Write a program that prompts the user to enter a sentence and prints the sentence in reverse order.
"""

user_sentence = input("Write any sentence: ")
print(user_sentence[::-1])

"""
BONUS CHALLENGE!
Write a program that prompts the user to enter a sentence and counts the frequency of each word in the sentence using a dictionary.
HINT: Python's split() method will turn a set into a List
"""


user_sentence = input("Enter a sentence: ")
word_counts = {}
words = user_sentence.split()

for word in words:
    if word in word_counts:
            word_counts[word] += 1
    else:
            word_counts[word] = 1

print(word_counts)

