def fib(n):
    """
    Calculate and return the nth term in the Fibonacci sequence iteratively.
    """
    if n <= 0:
        raise ValueError("Enter a positive integer.")
    
    if n == 1:
        return 0
    
    prev_term = 0
    current_term = 1

    for _ in range(2, n):
        next_term = prev_term + current_term
        prev_term, current_term = current_term, next_term

    return current_term


def validate_positive_integer():
    """
    Ask the user for input and only return when a positive integer is given.
    """
    while True:
        try:
            n = int(input("Which term in the Fibonacci sequence do you want to see? "))
            if n <= 0:
                print("Enter a positive integer.")
            else:
                return n
        except ValueError:
            print("Enter a positive integer.")


def main():
    n = validate_positive_integer()
    result = fib(n)
    print(f"The {n}th term in the Fibonacci sequence is: {result}")


if __name__ == "__main__":
    main()
