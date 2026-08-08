word = "amazing8"
print(word[1:6:2]) #print from index 1 to 5 with step 2
print(len(word)) #print the length of the word
print(word.endswith("ng")) #check if the word ends with "ng"
print(word.replace("a","o")) #replace "a" with "o" in the word
print(word.count("a")) #count the number of "a" in the word
print(word.upper()) #convert the word to uppercase
print(word.lower()) #convert the word to lowercase
print(word.capitalize()) #capitalize the first letter of the word
print(word.isalpha()) #check if the word contains only alphabets
print(word.isdigit()) #check if the word contains only digits
# a = "my naman and i am  a good boy\'don\'" 
a = "my naman and i am  a good boy\"don\""
print(a) #print the string with escape character
print(a.split()) #split the string into a list of words
name = input("Enter your name: ")
print(f"hello {name}!, welcome to python programming.") #print a formatted string with the name entered by the user
print("hello " + name + "!") #print a string with the name entered by the user
print("hello {}!".format(name)) #print a formatted string with the name entered by the user using format method
print("hello {0}!".format(name)) #print a formatted string with the name entered by the user using format method with index