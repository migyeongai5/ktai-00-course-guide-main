print("start1")
num1 = 100
print("start2")
num2 = input("Enter an integer or decimal number: ")
print("start3")
try:result = num1 + float(num2)
except ValueError:
    print("Invalid input. Please enter a valid number.")
    else:print ("The result is:", result)
print("end")
