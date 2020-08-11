"""
String Assignment : Level-I
Author: Digvijay Ukirde
"""

'''
Question 1
Ask the user to enter their first name and then display the length of their name.
'''
print("Length of Name: ", len(input("Please enter First name: ")))


'''
Question 2
Ask the user to enter their first name and then ask them to enter their surname. Join them together with a
space between and display the name and the length of whole name.
'''
first_name = input("Please enter First Name: ")
last_name = input("Please enter Last Name: ")
if first_name.isalpha() and last_name.isalpha():
    full_name = first_name + " " + last_name
    print("Full Name: ", full_name, "\nLength of Name: ", len(full_name))
else:
    print("Invalid Name")


'''
Question 3
Ask the user to enter their first name and surname in lower case. Change the case to title case and join them
together. Display the finished result
'''
first_name = input("Please enter First Name (lower case): ")
last_name = input("Please enter Last Name (lower case): ")
if first_name.islower() and last_name.islower():
    print("Full Name:", first_name.title(), last_name.title())
else:
    print("Invalid Input")


'''
Question 4
Ask the user to type in any word and display it in upper case.
'''
word = input("Please enter any word: ")
if word.isalpha():
    print(word.upper())
else:
    print("Invalid Input")


'''
Question 5
Ask the user to type in the first line of a nursery rhyme and display the length of the string. Ask for a starting
number and an ending number and then display just that section of the text. (remember Python starts
counting from 0 and not 1).
'''
nursery_rhyme = input("Please enter first line of a nursery rhyme: ")
print(nursery_rhyme, "\nLength of nursery rhyme:", len(nursery_rhyme))
start_index = input("Please enter starting position: ")
end_index = input("Please enter ending position: ")
if start_index.isnumeric() and end_index.isnumeric():
    print(nursery_rhyme[int(start_index)-1:int(end_index)])
else:
    print("Invalid Input")


'''
Question 6
Ask the user to enter their first name. If the length of their first name is under five characters, ask them to
enter their surname and join them together (without a space) and display the name in upper case. If the
length of the first name is five or more characters, display their first name in lower case.
'''
first_name = input("Please enter First Name: ")
if first_name.isalpha():
    if len(first_name) < 5:
        last_name = input("Please enter Last Name: ")
        if last_name.isalpha():
            print(first_name.upper(), last_name.upper(), sep='')
        else:
            print("Invalid Last Name")
    else:
        print(first_name.lower())
else:
    print("Invalid First Name")


'''
Question 7
Pig Latin takes the first consonant of a word, moves it to the end of the word and adds on an “ay”. If a word
begins with a vowel you just add “way” to the end. For example, pig becomes igpay, banana becomes
ananabay, and aadvark becomes aadvarkway. Create a program that will ask the user to enter a word and
change it into Pig Latin. Make sure the new word is displayed in lower case.
'''
VOWEL = "aeiou"
word = input("Please enter word to convert it into Pig Latin: ")
if word.isalpha():
    if word[0].lower() in VOWEL:
        print("Pig Latin Word: ", word.lower(), "way", sep='')
    else:
        print("Pig Latin Word: ", word[1:].lower(), word[0].lower(), "ay", sep='')
else:
    print("Invalid Input")