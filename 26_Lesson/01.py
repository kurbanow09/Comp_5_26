try:
    num1 = int(input("Enter 1 number: "))
    num2 = int(input("Enter 2 number: "))
    print(num1 / num2)
except ValueError:
    print("Harp bilen yazman")
except ZeroDivisionError:
    print("Sany 0-a bolup bolanok")