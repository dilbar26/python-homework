## 1
def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
## 2
def check_weird(n):
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")
## 3
def evens_with_if(a: int, b: int) -> list[int]:
   
    if a > b:
        a, b = b, a

   
    if a % 2:          # a is odd
        a += 1
    if b % 2:          # b is odd
        b -= 1

   
    if a > b:
        return []

   
    return list(range(a, b + 1, 2))
