"""
# Strings

import math
course = "Python Programming "
print(len(course))
print(course[-1])
print(course[0:3])
print(course)

first = "Asif Hasan"
last = "Rokon"
# full = first + " " + last
full = F"{first} {last}"
print(full)

print(course.upper())
print(course.lower())print(course.title())
print(course.strip())                  # Strip removes space
print(course.find("Pro"))
print(course.replace("P", "C"))
print("Pro" in course)
print("Cython" not in course)


# Numbers
x = 10
print(x // 3)                              # Return integer
x += 3                                     # Augmented assignment operator
print(x)

print(math.ceil(4.3))
print(math.factorial(5))
print(math.gcd(4, 5))


# Typecast

x = input("x :")                           # Takes input as string
y = int(x) + 1
print(f"x: {x}, y: {y}")


# Conditional Stateament

# Watermelon
w = int(input())
if ((w) % 2 != 0) or (w <= 2):
    print("NO\n")
else:
    print("YES\n")


# Ternary Operator

w = int(input())                                                # Watermelon(CODEFORCES)
message = "NO" if w % 2 != 0 or w <= 2 else "YES"
print(message)

# Short circuit Evaluation

high_income = False
good_credit = True
student = True
message = "Eligible" if high_income or good_credit or not student else "Not Eligible"
print(message)

age = 22
if 18 <= age < 65:
    print("Eligible")


# For loops

for number in range(5):
    print("Attempt ", (number + 1), (number + 1) * " *")
    """

for number in range(1, 6):
    print("Attempt ", number, number * " *")

print("\n")

for number in range(1, 10, 2):
    print("Attempt ", number, number * " *")

print("\n")

for x in range(5):
    for y in range(3):
        print(f"({x},{y})")
