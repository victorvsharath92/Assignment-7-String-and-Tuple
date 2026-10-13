#1. String Concatenation

# Get the user's name
name = input("Enter your Name: ")

# Concatenate the strings
str1 = "Hello " + name
print(str1)

# Add the welcome message
str2 = str1 + ", welcome to Python programming"
print(str2)

#2. String Slicing and Indexing

# Create the concatenated string
str1 = "Hello " + name
str2 = str1 + ", welcome to Python programming"

# a. First character
print("First character:", str2[0])

# b. Last character
print("Last character:", str2[-1])

# c. First 5 characters
print("First 5 characters:", str2[:5])

# d. Last 11 characters
print("Last 11 characters:", str2[-11:])

# e. Reverse the string
print("Reversed string:", str2[::-1])

# f. Print the word Python using slicing
print("Word Python:", str2[23:29])

#3. String Methods

strM = "Python beginner tutorial"

# a. Convert to uppercase
print("Uppercase:", strM.upper())

# b. Convert to lowercase
print("Lowercase:", strM.lower())

# c. Capitalize the sentence
print("Capitalized:", strM.capitalize())

# d. Count occurrences of the character 't'
print("Count of t:", strM.count('t'))

# e. Replace Python with Machine Learning
print("Replaced string:", strM.replace("Python", "Machine Learning"))

#4. Tuples — Creation, Concatenation and Access

# Create two tuples
t1 = (10, 20, 30)
t2 = (40, 50, 60)

# a. Concatenate the two tuples
t_combine = t1 + t2
print("Combined tuple:", t_combine)

# b. Repeat the elements 3 times
print("Repeated tuple:", t_combine * 3)

# c. Access the 3rd element
print("Third element:", t_combine[2])

# d. Access the first three elements
print("First three elements:", t_combine[:3])

# e. Access the last three elements
print("Last three elements:", t_combine[-3:])

