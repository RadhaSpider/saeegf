def add(P, Q):
    return P + Q
def subtract(P, Q):
    return P - Q
def multiplication(P, Q):
    return P * Q
def devide(P, Q):
    return P / Q
print("Please select a Operator")
print("a. ADD")
print("b. SUBTRACT")
print("c. MULTIPLICATION")
print("d. DEVIDE")
choice = input("Please Enter Choice (a/b/c/d): ")
num_1 = int(input("Please Enter the First Number: "))
num_2 = int(input("Please Enter the Second Numbe: "))
if choice == 'a':
    print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice == 'b':
    print(num_1, "-", num_2, "=", subtract(num_1, num_2))
elif choice == 'c':
    print(num_1, "*", num_2, "=", multiplication(num_1, num_2))
elif choice == 'd':
    print(num_1, "/", num_2, "=", devide(num_1, num_2))
else:
    print("This is an invalid input")