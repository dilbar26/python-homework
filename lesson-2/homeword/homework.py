## 1 

name = input("What is your name? ")

year = int(input("What year were you born? "))

age = 2025 - year

print("Hello, " + name + "! You are " + str(age) + " years old.")

## 2


## 3

## 4 

txt = "I'am John. I am from London"

residence = txt.split("I am from ")[1].split()[0]
print("Residence area:", residence)

## 5 

user_input = input("Enter a string: ")

reversed_string = user_input[::-1]

print("Reversed string:", reversed_string)

## 6 

text = input("Enter a string: ")
count = sum(1 for char in text.lower() if char in "aeiou")
print("Number of vowels:", count)

## 7 

numbers = input("Enter numbers separated by space: ").split()

numbers = [int(num) for num in numbers]

print("Maximum value:", max(numbers))

## 8 

word = input("Enter a word: ")
if word == word[::-1]:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")
  
## 9 
email = input("Enter your email address: ")

domain = email.split('@')[1] if '@' in email else None

if domain:
    print("Domain:", domain)
else:
    print("wrong email address.")
  ## 10




