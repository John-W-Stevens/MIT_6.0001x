# Write a program that examines three variables - x, y, and z - and prints
# the largest odd number among them. If none of them are odd, it shiould
# print a message to that effect.

# solution 1
def print_largest_odd_1(x,y,z):
    if (x % 2 == 0 and y % 2 == 0 and z % 2 == 0):
        print("No odd number provided!")
        return

    provided_numbers = [x,y,z]
    odd_numbers_list = []
    
    for number in provided_numbers:
        if number % 2 != 0:
            odd_numbers_list.append(number)

    print(max(odd_numbers_list))

# solution 2
def print_largest_odd_2(x,y,z):
    def is_even(n):
        return n % 2 == 0;

    if is_even(x) and is_even(y) and is_even(z):
        print("No odd number provided!")
        return

    print(max([n for n in [x,y,z] if not is_even(n)]))

# solution 3
def print_largest_odd_3(x,y,z):
    if x % 2 != 0 and x > y and x > z:
        print(x)
        return

    if y % 2 != 0 and y > x and y > z:
        print(y)
        return

    if z % 2 != 0 and z > x and z > y:
        print(z)
        return
    
    print("No odd number provided!")

# solution 4
def print_largest_odd_4(x,y,z):
    all_odds = [n for n in [x,y,z] if n % 2 != 0]
    print("No odd number provided!") if all_odds == [] else print(max(all_odds))

print_largest_odd_1(5,7,11) # expect: 11
print_largest_odd_1(19,12,5) # expect: 19
print_largest_odd_1(6,4,2) # expect: No odd number provided!

print_largest_odd_2(5,7,11) # expect: 11
print_largest_odd_2(19,12,5) # expect: 19
print_largest_odd_2(6,4,2) # expect: No odd number provided!

print_largest_odd_3(5,7,11) # expect: 11
print_largest_odd_3(19,12,5) # expect: 19
print_largest_odd_3(6,4,2) # expect: No odd number provided!

print_largest_odd_4(5,7,11) # expect: 11
print_largest_odd_4(19,12,5) # expect: 19
print_largest_odd_4(6,4,2) # expect: No odd number provided!