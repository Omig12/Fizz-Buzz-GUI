# Fizz Buzz

def fizz_buzz(x):
    """Returns fizz if x is divisible by 2, buzz if x is divisible by 3 and fizz_buzz if x is divisible by both. """
    y = []
    if (x % 6) == 0 :
        return "fizz_buzz"
    elif (x % 3) == 0:
        return "buzz"
    elif (x % 2) == 0:
        return "fizz"
    else:
        return "fish"

# print (fizz_buzz(input("number: ")))

if __name__ == '__main__':
    import sys
    fizz_buzz(int(sys.argv[1]))
