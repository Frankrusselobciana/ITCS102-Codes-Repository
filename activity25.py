def taga_triangle(number):
    for x in range (number, 0, -1):
        for y in range (1, x+1):
            print("*", end=" ")
        print()

def sum(x, y):
    return x+y

taga_triangle(6)
taga_triangle(7)
taga_triangle(5)
taga_triangle(32)
taga_triangle(9)

print(sum(30, 2))
print(sum(14, 3) * 100)

def box(size):
    for x in range(size+1):
        for y in range(size+1):
            if y == 0 or x == 0 or x == size or y == size:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

box(3)
box(5)
box(12)
box(20)

def my_factorial(number):
    fact = 1
    for x in range(number, 0, -1):
        fact *= x
    return fact

print(my_factorial(4))