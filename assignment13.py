def factorial(n):
    
    if n < 0:
        raise ValueError("Factorial doesn't exist for negative numbers")
    elif n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
   
    if n < 0:
        raise ValueError("Factorial doesn't exist for negative numbers")
    elif n == 0:
        return 0
    elif n == 1:
        return 1 
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
    


def gcd(a, b):
    
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b,a % b)
    


def compareTo(s1, s2):
   
    
    if len(s1) < len(s2):
        return -1
    elif len(s1) == len(s2):
        return 0
    elif len(s1) > len(s2):
        return 1
    else:
        return compareTo(s1[1],s2[1])


if __name__ == "__main__":
    for i in range(10):
        print(f"factorial({i}) = {factorial(i)}")

    # Fibonacci test
    print(f"fibonacci(10) = {fibonacci(10)}")
    print(f"fibonacci(12) = {fibonacci(12)}")

    # GCD test
    print(f"gcd(24, 56) = {gcd(24, 56)}")
    print(f"gcd(100, 45) = {gcd(100, 45)}")

    # compare strings test
    print(f"compareTo('Alain', 'Alan') = {compareTo('Alain', 'Alan')}")
    print(f"compareTo('Rocker', 'rocker') = {compareTo('Rocker', 'rocker')}")