# Python Dictionary and Set Exercises

## 1 
my_dict = {'apple': 3, 'banana': 1, 'cherry': 5, 'date': 2}

print(dict(sorted(my_dict.items(), key=lambda x: x[1])))

print(dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True)))

## 2 
my_dict = {'name': 'Alice', 'age': 25}


my_dict['city'] = 'New York'

print(my_dict)

## 3
result = dic1.copy()
result.update(dic2)
result.update(dic3)

print(result)

## 4

n = 5  # You can change this value

result = {x: x*x for x in range(1, n+1)}

print(result)

## 5
n = 15

squares_dict = {x: x*x for x in range(1, n+1)}

print(squares_dict)

## Set Exercises

## 1
my_set = {1, 2, 3, 4, 5}

print(my_set)

## 2 
my_set = {'apple', 'banana', 'cherry'}

for item in my_set:
    print(item)

## 3

my_set = {1, 2, 3}

my_set.add(4)

## 4

my_set = {1, 2, 3, 4, 5}

my_set.remove(3)

##5 

my_set = {1, 2, 3, 4, 5}

item = 3

my_set.discard(item)

print(my_set)





