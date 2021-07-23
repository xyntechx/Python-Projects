def build_fib_recursive(n):
    """
    n: number of elements in the sequence
    Returns a Fibonacci sequence of n elements by recursive method
    """
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        last_elem = build_fib_recursive(n-1)[-1] + build_fib_recursive(n-2)[-1]
        return build_fib_recursive(n-1) + [last_elem]


def build_fib_iterative(n):
    """
    n: number of elements in the sequence
    Returns a Fibonacci sequence of n elements by iterative method
    """
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        count = 2

        while count < n:
            last_elem = fib[-1] + fib[-2]
            fib.append(last_elem)
            count += 1
            
        return fib


def find_index(n):
    """
    n: an integer whose index in the Fibonacci sequence is to be found
    Returns the index of n in the Fibonacci sequence, a 404 message otherwise

    Note: n may or may not be in the Fibonacci sequence
    """
    if n == 0:
        return "Index of n (0-indexed): 0"
    elif n == 1:
        return "Index of n (0-indexed): 1 or 2"

    fib = [0, 1] # base case of Fibonacci sequence

    while n > fib[-1]:
        new_elem = fib[-1] + fib[-2]
        fib.append(new_elem)
        print(fib)

        if new_elem == n:
            return "Index of n (0-indexed): " + str(fib.index(n))
    
    return "404 Not Found: n is not in the Fibonacci sequence!"