import random

 
def generate_random_number(num1, num2) -> float:
    """
    Generate random integer.
    
    Arguments:
    num1: Lower bound
    num2: Higher bound
    
    returns: a random integer between num1 and num2
    """

    if isinstance(num1, int) and isinstance(num2, int):
        return random.randint(num1, num2)
    else:
        return random.uniform(num1, num2)



def randomize_operator() -> str:
    """
    Generates a random mathematical operator
    
    returns: one of random symbol from (+, -, *)
    """
    return random.choice(['+', '-', '*'])


def operate(n1, n2, o):
    """
    Performs operation on the input integers
    
    Arguments:
    n1: first number
    n2: second number
    o: arithmetic symbol
    
    returns: generated problem and the result
    """
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, round(a, 3)

def math_quiz():
    """"
    Integrates the entire program by interacting with the user for inputs.
    It also calculates the score for each correct answer of the user.
    
    """
    
    s = 0 
    t_q = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(int(t_q)):
        n1 = generate_random_number(1, 10) #stores a random number between 1 and 10
        n2 = generate_random_number(1, 5.5) #stores a random number between 1 and 5.5
        o = randomize_operator()

        problem, result = operate(n1, n2, o)
        print(f"\nQuestion: {problem}")
        user_result = input("Your answer: ")
        if '.' in user_result:
            user_answer = float(user_result)
        else:
            user_answer = int(user_result)


        if user_answer == result: #checks if users' answer is correct or not
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {result}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
