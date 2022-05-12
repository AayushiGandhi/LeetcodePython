def multiply(N):
    fact = 1
    for i in range(1, N+1):
        fact *= i
    return fact


def factorial(N):
    return str(multiply(N))


if __name__ == "__main__":
    print(factorial(5))












