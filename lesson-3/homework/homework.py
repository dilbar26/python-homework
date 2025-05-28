## 1 
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[2])  # prints the third fruit (index 2)

## 2 
list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined_list = list1 + list2
print(combined_list)

## 3
numbers = [10, 20, 30, 40, 50]  # example list

first = numbers[0]
middle = numbers[len(numbers) // 2]
last = numbers[-1]

new_list = [first, middle, last]
print(new_list)

 ## 4 
favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight", "Parasite"]
movies_tuple = tuple(favorite_movies)
print(movies_tuple)

## 5
cities = ["London", "New York", "Paris", "Tokyo"]

if "Paris" in cities:
    print("Paris is in the list.")
else:
    print("Paris is not in the list.")

## 6 
numbers = [1, 2, 3, 4, 5]
duplicated = numbers * 2
print(duplicated)

## 7 
numbers = [10, 20, 30, 40, 50]

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print(numbers)

## 8 
numbers = tuple(range(1, 11))  

slice_part = numbers[3:7]

print(slice_part)

## 9 
colors = ["red", "blue", "green", "blue", "yellow", "blue"]

count_blue = colors.count("blue")
print("Number of times blue appears:", count_blue)

## 10

animals = ("tiger", "elephant", "lion", "giraffe")

index_lion = animals.index("lion")
print("Index of 'lion':", index_lion)

## 11

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

merged_tuple = tuple1 + tuple2
print(merged_tuple)

## 12

my_list = [10, 20, 30, 40]
my_tuple = (5, 15, 25)

print("Length of list:", len(my_list))
print("Length of tuple:", len(my_tuple))

## 13 
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print(my_list)

## 14 
numbers = (10, 20, 5, 40, 15)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

 ## 15 
words = ("apple", "banana", "cherry", "date")

reversed_words = words[::-1]

print(reversed_words)



