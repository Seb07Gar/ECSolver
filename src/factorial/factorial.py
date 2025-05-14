import sys
def fact(n):
    return n*fact(n-1) if n>=1 else 1


def main():
    if len(sys.argv) != 2:
        print("Usage: python test.py <number>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        if number < 0:
            raise ValueError("Number must be non-negative")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    print(f"The factorial of {number} is {fact(number)}")

if __name__ == "__main__":
    print(fact(5))