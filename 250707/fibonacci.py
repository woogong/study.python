def makeFibonacciSeries(max_val):
    """ Generate a Fibonacci series up to max_val."""
    a, b = 0, 1
    result = []
    while a <= max_val:
        result.append(a)
        a, b = b, a + b
    return result

if __name__ == "__main__":
    import sys
    
    max_val = 10
    if len(sys.argv) > 1:
        max_val = int(sys.argv[1])

    print(makeFibonacciSeries(max_val))