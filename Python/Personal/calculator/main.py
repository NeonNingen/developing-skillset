import calc

def start_calc(state, num1, num2):
        if state == True:
            pass
        else:
             num_set()

        calculator = calc.calc(num1, num2)

        operator = input("Which you like to plus, minus, times or subtract: ")
        calculator.add()
        state = False
        return True, False

def num_set():
     num1 = int(input("Input your first number: "))
     num2 = int(input("Input your second number: "))
     return True, num1, num2


if __name__ == "__main__":
    print("Welcome to the calculator application, please input your two numbers then operator.")

    while True:
        try:
            _break, state = start_calc(False, 0, 0)
            if _break: break
        except Exception as e:
            print("Error Occured: ", e)

'''
An array for multiple numbers?

Rework the idea that num_set and the operators have their own looped exception using the one exception in __main__
'''