def makeFibonacciSeries(n):
    """ Generate a Fibonacci series up to n."""

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        
        while True:
            next_fib = fib_series[-1] + fib_series[-2]
            if (next_fib > n):
                break
            else:
                fib_series.append(next_fib)

        return fib_series

print("fibonacci initialized")

if __name__ == "__main__":
    import sys
    
    max = 10
    if len(sys.argv) > 1:
        max = int(sys.argv[1])

    print(makeFibonacciSeries(max))