HISTORY_FILE = "calc_history.txt"

def show_history():
    file = open(HISTORY_FILE, "r")
    lines = file.readlines()
    if len(lines) == 0:
        print("No history available.")
    else:
        for line in reversed(lines):
            print(line.strip())
            file.close()

def clear_history():
    file = open(HISTORY_FILE, "w")
    file.close()
    print("History cleared.")

def save_to_history(equation, result):
    file = open(HISTORY_FILE, "a")
    file.write(equation + " = " + str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Use: (number1) space (operator) space (number2)")
        return None
    
    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero.")
            return None
        return num1 / num2
    else:
        print("Invalid operator. Use +, -, *, or /")
        return None

def main():
    print('---SIMPLE CALCULATOR(type history, clear, or exit)---')
    while True:
        user_input = input("Enter calculation: ")
        if user_input.lower() == 'exit':
            print("Exiting calculator.")
            break
        elif user_input.lower() == 'history':
            show_history()
        elif user_input.lower() == 'clear':
            clear_history()
        else:
            result = calculate(user_input)
            if result is not None:
                print("Result:", result)
                save_to_history(user_input, result)
               

if __name__ == "__main__":
    main()