import random


def function_number(min_value, max_value):
    """
    Random integer.
    """
    return random.randint(min_value, max_value)


def function_operator():
    return random.choice(['+', '-', '*'])


def function_math_problem(number1, number2, operator):
    problem_text = f"{number1} {operator} {number2}"
    if operator == '+': answer = number1 + number2
    elif operator == '-': answer = number1 - number2
    elif operator == '*': answer = number1 * number2
    else: raise ValueError("Invalid operator")
    return problem_text, answer

def math_quiz_game():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        number1 = function_number(1, 10)
        number2 = function_number(1, 5)
        operator = function_operator()

        problem, correct_answer = function_math_problem(number1, number2, operator)
        print(f"\nQuestion: {problem}")
        myanswer = input("My answer: ")
        myanswer = int(myanswer)

        if myanswer == correct_answer:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz_game()
